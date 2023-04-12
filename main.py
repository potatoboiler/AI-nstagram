import torch
from diffusers import StableDiffusionPipeline, DPMSolverMultistepScheduler

model_id = "stabilityai/stable-diffusion-2-1"

# Use the DPMSolverMultistepScheduler (DPM-Solver++) scheduler here instead
pipe = StableDiffusionPipeline.from_pretrained(model_id, torch_dtype=torch.float16)
pipe.scheduler = DPMSolverMultistepScheduler.from_config(pipe.scheduler.config)
pipe = pipe.to("cuda")
pipe.enable_attention_slicing()

prompt = "mdjrny-v4 style portrait of high elf, intricate, elegant, highly detailed, digital painting, artstation, concept art, smooth, sharp focus, illustration, realistic, 8k"
images = pipe(prompt).images
    
for i, image in enumerate(images):
    image.save(f"astronaut_rides_horse_{i}.png")