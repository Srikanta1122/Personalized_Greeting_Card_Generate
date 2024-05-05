from diffusers import StableDiffusionXLPipeline
import torch
import pandas as pd

# Load data from Excel
excel_file_path = "D:\Greeting\EmployeeDatabase.xlsx"
df = pd.read_excel(excel_file_path)

# Get emp_id input from the user 
emp_id_input = int(input("Enter emp_id: "))

# Check if the entered emp_id exists in the DataFrame
if emp_id_input in df['Id'].values:
    # Retrieve prompts for the specified emp_id
    prompts = df.loc[df['Id'] == emp_id_input, ['NAME', 'SEASON', 'TRAVEL', 'COLOUR', 'FOOD', 'FLOWER', 'MUSIC', 'ACTIVITY']].values.flatten()

    # Initialize the pipeline 
    pipe = StableDiffusionXLPipeline.from_pretrained("segmind/SSD-1B", torch_dtype=torch.float32)#, use_safetensors=True)
    pipe.to("cpu") 
    # if using torch < 2.0  
    # pipe.enable_xformers_memory_efficient_attention()  

    # Generate image for the specified emp_id
    prompt = ' '.join(map(str, prompts))  # Combine 8 prompts into a single string
    image = pipe(prompt=prompt).images[0]
    image.save(f"image_{emp_id_input}.png")
    print(f"Image for emp_id {emp_id_input} generated successfully.")
else:
    print(f"Emp_id {emp_id_input} not found in the dataset.")




