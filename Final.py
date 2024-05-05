from diffusers import StableDiffusionXLPipeline
import torch
import pandas as pd
from datetime import datetime
import gradio as gr
from PIL import Image

# Load data from Excel
excel_file_path = "D:\Greeting\EmployeeDatabase.xlsx"
df = pd.read_excel(excel_file_path)

# Define a function to generate image and prompt
def generate_image_and_prompt(emp_id_input, num_generations):
    try:
    # Initialize output_prompt with a default value
   # output_prompt = ""
    
    # Check if the entered emp_id exists in the DataFrame
        if emp_id_input in df['Id'].values:
            # Retrieve prompts for the specified emp_id
            prompts = df.loc[df['Id'] == emp_id_input, ['NAME','SEASON', 'TRAVEL', 'COLOUR', 'FOOD', 'FLOWER', 'MUSIC', 'ACTIVITY']].values.flatten()

            # Initialize the pipeline
            pipe = StableDiffusionXLPipeline.from_pretrained("segmind/SSD-1B", torch_dtype=torch.float32) #, use_safetensors=True, variant="fp16")
            pipe.to("cpu")

        # generated_images = []

            # Generate images for the specified emp_id based on the user input 
            for i in range(num_generations):
                # Combine 7 prompts into a single string
                prompt = ' '.join(map(str, prompts))
                image = pipe(prompt=prompt).images[0]
                
                # Include timestamp in the image filename to avoid overwriting
                timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
                image_path=f"image_{emp_id_input}_{timestamp}_{i + 1}.png"
                image.save(image_path)
                
                # Generate the output prompt
                output_prompt = (
                    f"Make a greeting card for {prompts[0]} who likes the season {prompts[1]}, "
                    f"likes to visit {prompts[2]},"
                    f" favourite colour is {prompts[3]}, "
                    f"likes to eat {prompts[4]} food,"
                    f" likes flower {prompts[5]}, "
                    f"listens to {prompts[6]} music, "
                    f"and likes to do {prompts[7]}."
                )

                return output_prompt, image_path 
                #print(output_prompt)
            # generated_images.append(image)

            
            # print(f"Image {i + 1} for emp_id {emp_id_input} generated successfully.")

        else:
            return f"Emp_id {emp_id_input} not found in the dataset.", None
        
    except Exception as e:
        return f"Error: {str(e)}", None

   # return output_prompt, generated_images

# Define a function to display images
# def display_images(output_prompt, generated_images):
#     return output_prompt, [Image.fromarray(image) for image in generated_images]

# Create a Gradio interface
iface = gr.Interface(
    fn=generate_image_and_prompt,
    inputs=["number", "number"],  # Employee ID as number, Number of generations as number
    outputs=["text", "image", "image", "image", "image"],  # Outputs include text and image
    live=True,
    title="Employee Information Extractor",
    description="Enter Employee ID and number of generations to generate image and extract information."
)

# Set the display_images function as the Gradio display function
#iface.func = display_images

# Launch the Gradio interface 
iface.launch()


