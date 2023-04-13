import random
from typing import Union, List

from fastapi import FastAPI
from pydantic import BaseModel
from diffusers import StableDiffusionPipeline, DPMSolverMultistepScheduler
import torch
from PIL import Image
import numpy as np

post_size = 5

sd_prompts = ['orchestra', 'vacation', 'school']
gpt_prompts = ['bleh']
gpt_captions = ['out on vacation!']

model_id = "stabilityai/stable-diffusion-2-1"

pipe = StableDiffusionPipeline.from_pretrained(model_id, torch_dtype=torch.float16)
pipe.scheduler = DPMSolverMultistepScheduler.from_config(pipe.scheduler.config)
pipe = pipe.to("cuda")

class Post(BaseModel):
    caption: str
    images: List[Image.Image | np.ndarray]

class PostCollection(BaseModel):
    posts: List[Post]

app = FastAPI()

@app.get("/")
async def get_posts():
    prompts = [random.choice(sd_prompts)] * post_size
    num_inference_steps = 10
    images = pipe(prompts, num_inference_steps=num_inference_steps).images
    return {images}