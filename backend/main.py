import random
from typing import Union, List

from fastapi import FastAPI
from pydantic import BaseModel
from diffusers import StableDiffusionPipeline, DPMSolverMultistepScheduler
import torch
from PIL import Image
import numpy as np

post_size = 5

sd_prompts = ["orchestra", "vacation", "school"]
gpt_prompts = ["bleh"]
gpt_captions = ["out on vacation!"]

model_id = "stabilityai/stable-diffusion-2-1"

pipe = StableDiffusionPipeline.from_pretrained(model_id, torch_dtype=torch.float16)

app = FastAPI()

class PostResponse(BaseModel):
    urls: List[List[str]]

    class Config:
        orm_mode = True

@app.on_event("startup")
async def startup_event():
    pipe.scheduler = DPMSolverMultistepScheduler.from_config(pipe.scheduler.config)
    pipe = pipe.to("cuda")

@app.get("/")
async def get_posts():
    pass

if __name__ == '__main__':
    import uvicorn

    