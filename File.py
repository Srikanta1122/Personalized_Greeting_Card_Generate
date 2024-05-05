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
        # Initialize a list to store generated images
        generated_image_paths = [] 

        # Check if the entered emp_id exists in the DataFrame
        if emp_id_input in df['Id'].values: 
            # Retrieve prompts for the specified emp_id
            prompts = df.loc[df['Id'] == emp_id_input, ['SEASON', 'TRAVEL', 'COLOUR', 'FOOD', 'FLOWER', 'MUSIC', 'ACTIVITY']].values.flatten()

            # Initialize the pipeline
            pipe = StableDiffusionXLPipeline.from_pretrained("segmind/SSD-1B", torch_dtype=torch.float32)
            pipe.to("cpu")

            # Generate images for the specified emp_id based on the user input
            for i in range(num_generations): 
                # Combine 7 prompts into a single string
                prompt = ' '.join(map(str, prompts))
                image = pipe(prompt=prompt).images[0] 

                # Include timestamp in the image filename to avoid overwriting
                timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
                image_path = f"image_{emp_id_input}_{timestamp}_{i + 1}.png"
                image.save(image_path)

                # Append the generated image path to the list
                generated_image_paths.append(image_path)

            # Generate the output prompt
            output_prompt = (
                f"Make a greeting card for someone who likes the season {prompts[0]}, "
                f"likes to visit {prompts[1]},"
                f" favourite colour is {prompts[2]}, "
                f"likes to eat {prompts[3]} food,"
                f" likes flower {prompts[4]}, "
                f"listens to {prompts[5]} music, "
                f"and likes to do {prompts[6]}."
            )

            return output_prompt, generated_image_paths

        else:
            # Return a message if emp_id is not found
            output_prompt = f"Emp_id {emp_id_input} not found in the dataset."
            return output_prompt, []

    except Exception as e:
        # Return an error message if an exception occurs
        output_prompt = f"Error: {str(e)}"
        return output_prompt, []

# Create a Gradio interface with a submit button
iface = gr.Interface(
    fn=generate_image_and_prompt,
    inputs=["number", "number"],
    outputs=["text", gr.Gallery(label="Generated Images")],  
    title="Greeting Card Generator",
    description="Enter an employee ID and the number of images to generate personalized greeting cards."
)

# Launch the Gradio interface
iface.launch(share=True)




