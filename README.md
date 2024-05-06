
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

Use this pre-train text-to-image generative model: [Hugging Face model link](https://huggingface.co/segmind/SSD-1B) 

#### This model totally run on the local machine for image generation. 

[](https://github.com/Srikanta1122/Personalized_Greeting_Card_Generate/assets/105414609/03399c5a-9500-4e35-9d96-a1806225a831) 


## Model Architecture:

The SSD-1B Model is a 1.3B Parameter Model which has 
several layers removed from the Base SDXL Model.

![](https://github.com/Srikanta1122/Personalized_Greeting_Card_Generate/assets/105414609/03399c5a-9500-4e35-9d96-a1806225a831)

## WorkFlow:

1) User Input:
The process begins when a user interacts with the Gradio interface. The interface
prompts the user to input an employee ID and specify the number of personalized
greeting cards they want to generate.

2) Excel Data Extraction:
The process begins with extracting information from an Excel spreadsheet. It
extracts information according to NGS that we put in gradio. This spreadsheet likely
contains data about individuals, including attributes like their name, birthday,
preferences (season, colour, food, travel, flower, music , activity ), and paths to
their personal photos.

3) Prompt Construction:
Once the relevant information is extracted by Unique NGS from the Excel sheet,
the code constructs a personalized message for each individual based on their
attributes. This message serves as a prompt for generating the greeting card. And
According to the prompt greetings card will generate.

4) Background Image Generation:
A Stable Diffusion XL Pipeline is initialized using a pre-trained model. This pipeline
is responsible for generating images based on textual prompts provided to it. Using
a pre-trained stablediffusionXL model (segmind/Segmind-Vega) that is taken form
hugging face , the code generates an image based on the constructed prompt. The
diffusion model is a deep learning model capable of generating high-quality images
conditioned on textual prompts. It also specifies the device to be used for
computation. In this case, the device is set to “cpu” for local machine.

5) Function Definition:-
‘add_text_to_image’: A function that adds text to an image using PIL’s ImageDraw
module.
‘extract_info_from_excel’: This function reads data from an Excel file located at a
specific path . It searches for a specific employee ID (target ID) in the Excel file.
If the ID is found: It extracts various attributes associated with the ID from the
Excel row (e.g., name, season, travel, colour, etc.). If the ID is not found then it
shows error.

6) Personalization:
After generating the base image, the code personalizes it further by: Adding the
individual’s personal photo onto the generated image. This personal photo is
retrieved from the provided path in the Excel spreadsheet . Adding additional text
elements such as the individual’s name and birthday onto the image.

7) Image Saving:
Once personalized, the generated greeting card images are saved to a specified
directory with unique filenames using timestamp and files are not replaced. This
ensures that each card is uniquely identifiable and can be retrieved later.

8) Output to Gradio Interface:
The function returns the constructed prompt and a list of generated images to the
Gradio interface. The prompt may include details about the employee’s
preferences and characteristics. The interface displays the generated images in a
gallery format, allowing users to preview and download them.


## Run Locally:

Clone the repository

```bash
  git clone https://github.com/Srikanta1122/Personalized_Greeting_Card_Generate.git
```

Install dependencies

```bash
  install all the required libery that I mention on the top. 
```

Edit the file path for xlsx data

```bash
  give your actual path. I provided the file into the Excel_data folder 
```

Go to the Greeting_Card.py file 

```bash
  run this file. 
```

Wait 

```bash
  it's takes lot of time for pre-train model successfully install in your local machine.  
```

click the IP link that show in the terminal

```bash
  enter the emp_id and number of images that you have to generate, then click the submit button. 
  it will also take some time for generate the images. 
```

## Final Output:

![Image](https://github.com/Srikanta1122/Personalized_Greeting_Card_Generate/assets/105414609/1aa73f89-91dc-4877-b45f-0de19b149b1a)  

