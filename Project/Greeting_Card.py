'''
from diffusers import StableDiffusionXLPipeline
import torch
pipe = StableDiffusionXLPipeline.from_pretrained("segmind/SSD-1B", torch_dtype=torch.float16, use_safetensors=True, variant="fp16")
pipe.to("cuda")
# if using torch < 2.0
# pipe.enable_xformers_memory_efficient_attention()
prompt = "Design a greeting card for a Swaziland-loving desert summer enthusiast who favors blue." # Your prompt here
neg_prompt = "human, rainy, animal" # Negative prompt here
image = pipe(prompt=prompt, negative_prompt=neg_prompt).images[0]
image.save("image.png") 

'''
from diffusers import StableDiffusionXLPipeline
import torch

pipe = StableDiffusionXLPipeline.from_pretrained("segmind/SSD-1B", torch_dtype=torch.float16, use_safetensors=True, variant="fp16", force_download=True, resume_download=False)
pipe.to("cuda")

prompt = "Design a greeting card for a Swaziland-loving desert summer enthusiast who favors blue."  # Your prompt here
neg_prompt = "human, rainy, animal"  # Negative prompt here
image = pipe(prompt=prompt, negative_prompt=neg_prompt).images[0]
image.save("image.png")


