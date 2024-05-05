import gradio as gr
from PIL import Image

def display_image(image_path):
    try:
        img = Image.open(image_path)
        return img
    except Exception as e: 
        return f"Error: {e}"

iface = gr.Interface(
    fn=display_image,
    inputs="text",
    outputs="image",
    live=True,
    title="Image Display",
    description="Enter the path of an image to display it.",
)

iface.launch(share=True)

