from PIL import Image
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from diffusers import StableDiffusionXLPipeline
import torch
import pandas as pd
from datetime import datetime
import gradio as gr
import io
import os  # Add this import statement
import rembg  # Import the rembg module

# Load data from Excel
excel_file_path = "D:\Greeting\EmployeeDatabase1.xlsx"
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
                # Generate image for the specified emp_id
                prompt = ' '.join(map(str, prompts))  # Combine 7 prompts into a single string
                
                generated_image = pipe(prompt=prompt).images[0]

                # Save the generated image with a unique filename based on timestamp
                timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
                temp_image_path = f"temp_image_{emp_id_input}_{timestamp}_{i + 1}.png"
                generated_image.save(temp_image_path)


                # Load the image paths from the Excel file
                image_path_1 = df.loc[df['Id'] == emp_id_input, 'Image_path_for_birthday'].values[0]
                image_path_2 = df.loc[df['Id'] == emp_id_input, 'Image_path_for_profile_pic'].values[0]

                # Open the images
                img = Image.open(temp_image_path)
                img_to_paste_1 = Image.open(image_path_1).convert("RGBA")
                img_to_paste_2 = Image.open(image_path_2).convert("RGBA")

                # Resize the image (adjust the width and height as needed)
                new_size = (1000, 1000)  # Specify the new size (width, height)
                img_resized = img.resize(new_size)

                # Get the width and height of the resized background image
                img_width, img_height = img_resized.size

                # Define the relative coordinates and size of the first box (left, top, width, height) as percentages
                if i % 6 == 0:
                    box_coords_1 = (0.15 * img_width, 0.10 * img_height, 0.6 * img_width, 0.2 * img_height)
                elif i % 6 == 1:
                    box_coords_1 = (0.20 * img_width, 0.15 * img_height, 0.5 * img_width, 0.2 * img_height)
                elif i % 6 == 2:
                    box_coords_1 = (0.5 * img_width, 0.12 * img_height, 0.4 * img_width, 0.3 * img_height)
                elif i % 6 == 3:
                    box_coords_1 = (0.20 * img_width, 0.30 * img_height, 0.5 * img_width, 0.4 * img_height)
                elif i % 6 == 4:
                    box_coords_1 = (0.10 * img_width, 0.20 * img_height, 0.3 * img_width, 0.4 * img_height)
                else:
                    box_coords_2 = (0.25 * img_width, 0.25 * img_height, 0.4 * img_width, 0.5 * img_height)

                img_to_paste_resized_1 = img_to_paste_1.resize((int(box_coords_1[2]), int(box_coords_1[3])))
                img_to_paste_resized_1 = rembg.remove(img_to_paste_resized_1)  # Make the image transparent
                img_resized.paste(img_to_paste_resized_1, (int(box_coords_1[0]), int(box_coords_1[1])), mask=img_to_paste_resized_1)

                # Define the relative coordinates and size of the second box (left, top, width, height) as percentages
                if i % 6 == 0:
                    box_coords_2 = (0.35 * img_width, 0.25 * img_height, 0.5 * img_width, 0.7 * img_height)
                elif i % 6 == 1:
                    box_coords_2 = (0.15 * img_width, 0.20 * img_height, 0.4 * img_width, 0.5 * img_height)
                elif i % 6 == 2:
                    box_coords_2 = (0.25 * img_width, 0.30 * img_height, 0.5 * img_width, 0.4 * img_height)
                elif i % 6 == 3:
                    box_coords_1 = (0.30 * img_width, 0.35 * img_height, 0.6 * img_width, 0.6 * img_height)
                elif i % 6 == 4:
                    box_coords_1 = (0.10 * img_width, 0.15 * img_height, 0.3 * img_width, 0.3 * img_height)
                else:
                    box_coords_2 = (0.20 * img_width, 0.10 * img_height, 0.6 * img_width, 0.5 * img_height)

                img_to_paste_resized_2 = img_to_paste_2.resize((int(box_coords_2[2]), int(box_coords_2[3])))
                img_to_paste_resized_2 = rembg.remove(img_to_paste_resized_2)  # Make the image transparent
                img_resized.paste(img_to_paste_resized_2, (int(box_coords_2[0]), int(box_coords_2[1])), mask=img_to_paste_resized_2)

                # Create a subplot
                fig, ax = plt.subplots()

                # Display the resized image using Matplotlib
                ax.imshow(img_resized)
                ax.axis('off')  # Hide axis labels and ticks

                # Define the rectangles (boxes) to be drawn
                box_1 = patches.Rectangle((box_coords_1[0], box_coords_1[1]), box_coords_1[2], box_coords_1[3], linewidth=1, facecolor='none')  #edgecolor='red')
                box_2 = patches.Rectangle((box_coords_2[0], box_coords_2[1]), box_coords_2[2], box_coords_2[3], linewidth=1, facecolor='none')  #edgecolor='green')

                # Add the boxes to the plot
                ax.add_patch(box_1)
                ax.add_patch(box_2)

                # Show the plot
                plt.show()
                

                # Save the generated image with a unique filename based on timestamp
                timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
                image_path = f"final_image_{emp_id_input}_{timestamp}_{i + 1}.png"
                img_resized.save(image_path)
                print(f"Image {i + 1} for emp_id {emp_id_input} generated successfully.")

                generated_image_paths.append(image_path)

                # Remove the temporary image file
                os.remove(temp_image_path)    

            output_prompt = (
                    f"Make a greeting card for the person who likes the season {prompts[0]}, "
                    f"likes to visit {prompts[1]}, "
                    f"favourite colour is {prompts[2]}, "
                    f"likes to eat {prompts[3]} food, "
                    f"likes flower {prompts[4]}, "
                    f"listens to {prompts[5]} music, "
                    f"and likes to do {prompts[6]}."
                )
            print(output_prompt)             

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
    outputs=["text", gr.Gallery(label="Generated Images")],  # Outputs include text and multiple images
    title="Greeting Card Generator",
    description="Enter an employee ID and the number of images to generate personalized greeting cards."

)

# Launch the Gradio interface
iface.launch(share=True)





