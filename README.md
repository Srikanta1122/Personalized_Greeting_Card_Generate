
# Personalized_Greeting_Card_Generate: Step-By-Step guide for use this project

## Libraries Used: 

I have used some python libraries to complete the project , the libraries and what the
libraries does in my project is given below…

• torch: PyTorch library, commonly used for deep learning tasks. In this case, it seems to
be utilized for the Stable Diffusion XL model.

• Diffusers.:- Diffusers is the go-to library for state-of-the-art pre-trained diffusion
models for generating images, audio, and even 3D structures.

• PIL (Python Imaging Library): Used for image processing tasks. It's employed for
opening, manipulating, and saving images.

• pandas: A powerful data manipulation library used to read data from an Excel file into a Data-Frame.

• OS: The Python os module provides a way to interact with the operating system. It's 
used here to create directories and handle file operations.

• time: The time module is used for generating a timestamp that's appended to the
generated image filenames.

• rembg (Remove Background): A library for removing the background from images. It
seems to be applied to a personal photo in the project.

• numpy: A library for numerical operations. In this case, it's used to convert images to
arrays for processing.

• gradio: A library , used for generating a interface for the user to give input and take
output.

## Model Details: 

1) Model Description:
• Developed by: Segmind 
• Developers: Yatharth Gupta and Vishnu Jaddipal.
• Model type: Diffusion-based text-to-image generative model
• License: Apache 2.0
• Distilled From stabilityai/stable-diffusion-xl-base-1.0

SSD-1B can support the following output resolutions.

1024 x 1024 (1:1 Square)
1152 x 896 (9:7)
896 x 1152 (7:9)
1216 x 832 (19:13)
832 x 1216 (13:19)
1344 x 768 (7:4 Horizontal)
768 x 1344 (4:7 Vertical)
1536 x 640 (12:5 Horizontal)
640 x 1536 (5:12 Vertical)




[](https://github.com/Srikanta1122/Personalized_Greeting_Card_Generate/assets/105414609/03399c5a-9500-4e35-9d96-a1806225a831) 


## Model Architecture:

The SSD-1B Model is a 1.3B Parameter Model which has 
several layers removed from the Base SDXL Model.

![](https://github.com/Srikanta1122/Personalized_Greeting_Card_Generate/assets/105414609/03399c5a-9500-4e35-9d96-a1806225a831)

