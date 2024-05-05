from diffusers import StableDiffusionXLPipeline
import torch
import gradio as gr
import pandas as pd

# Load data from Excel
excel_file_path = "D:\Greeting\EmployeeDatabase.xlsx"
df = pd.read_excel(excel_file_path)

def generate_image_and_prompt(emp_id_input):
    try:
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

            # Get the image path from the DataFrame
            image_path = f"image_{emp_id_input}.png"
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
        else:
            return f"No data found for ID {emp_id_input}", None
    except Exception as e:
        return f"Error: {str(e)}", None

# Create a Gradio interface
iface = gr.Interface(
    fn=generate_image_and_prompt,
    inputs=["number"],  # Employee ID as number
    outputs=["text", "image"],  # Outputs include text and image
    live=True,
    title="Employee Information Extractor",
    description="Enter Employee ID to generate image and extract information."
)

# Launch the Gradio interface 
iface.launch()




