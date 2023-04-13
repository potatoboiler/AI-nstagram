from base64 import encodebytes
from flask_cors import CORS, cross_origin
import random
import PIL
from asgiref.wsgi import WsgiToAsgi
from flask import Flask, jsonify
import torch
from diffusers import StableDiffusionPipeline, DPMSolverMultistepScheduler
from xformers.ops import MemoryEfficientAttentionFlashAttentionOp
import io


batch_size = 3
num_inference_steps = 20

model_id = "stabilityai/stable-diffusion-2-1"

pipe = StableDiffusionPipeline.from_pretrained(model_id, torch_dtype=torch.float16)
pipe.scheduler = DPMSolverMultistepScheduler.from_config(pipe.scheduler.config)
pipe = pipe.to("cuda")
pipe.enable_xformers_memory_efficient_attention(
    attention_op=MemoryEfficientAttentionFlashAttentionOp
)
# Workaround for not accepting attention shape using VAE for Flash Attention
pipe.vae.enable_xformers_memory_efficient_attention(attention_op=None)

prompts = ["school", "beach", "forest"]

app = Flask(__name__)
cors = CORS(app)
app.config["CORS_HEADERS"] = "Content-Type"


def pil_to_jpg(pil_img: PIL.Image.Image):
    byte_arr = io.BytesIO()
    pil_img.save(byte_arr, format="JPEG")
    return encodebytes(byte_arr.getvalue()).decode("ascii")


@app.route("/", methods=["GET"])
@cross_origin()
def get_data():
    images = pipe(
        random.choice(prompts),
        num_inference_steps=num_inference_steps,
        num_images_per_prompt=batch_size,
    ).images
    return jsonify({"data": [pil_to_jpg(image) for image in images]})


# asgi_app = WsgiToAsgi(app)
