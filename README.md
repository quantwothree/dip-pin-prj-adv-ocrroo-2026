# Overview

The OCR Video Player is a full-stack, client-server web application designed to extract text directly from video files besides standard video playback. 

This project is built for students, software developers, researchers, data analysts or anyone who frequently consume educational content, coding tutorials or lecture recordings. 
Additionally, it serves as a foundational framework for accessibility advocates and vision-impaired users where this project could be made into a more inclusive media experience.

This project was developed to bridge the gap between visual media and text-based workflows. 
In educational and professional environments, users often need to extract information, such as code snippets, lecture slides, or any texts from videos.

Traditionally, this required manual transcription. This application automates that workflow by utilizing OCR. By reducing transcription time and human error, it significantly enhances user productivity and accessibility.

Beyond productivity, a major driving factor for this project is its potential to be extended into a highly accessible video player. 
Currently, text embedded inside videos is completely invisible to standard screen readers. 
By extracting this on-screen text via our backend OCR, future iterations can route this data into Text-to-Speech (TTS) engines or braille displays.
This could, theoretically transform an otherwise inaccessible video into a fully inclusive media experience.

# How to deploy:

1. Install Pytesseract using the instructions in the Dependencies section below.
2. Install Astral's uv with this instructions: https://docs.astral.sh/uv/#installation
3. Make sure that you have a folder called 'resources' at the root of this project and inside it you have a video called 'oop.mp4'
4. Run `uv sync` from the root folder of the project 
5. Now you can run the project using `uv run fastapi dev preliminary/simple_api.py`

# Dependencies:

## TESSERACT

This project relies on Tesseract engine to process OCR function, because it's written in C++, we will need to use a Python Wrapper 
called Pytesseract.

Here is how to install Pytesseract:
1. ### On Windows
    - Go to this link and download the .exe file:
        - https://github.com/UB-Mannheim/tesseract/wiki
    - Install the downloaded .exe, note that this installer also include the training data so we don't need to manually include it
    - It's important to **note down the install location** for it as we will need it in the project code
    - After installation, **go directly into your project folder** and run this command, it will add Pytesseract to your virtual enviroment and update your **pyproject.toml**:
      -       uv add pytesseract
    - Go into your Python scripts where you would like to use Pytesseract and add:
      -       import pytesseract 
      -       pytesseract.pytesseract.tesseract_cmd = r'YOUR TESSERACT.EXE LOCATION'

2. ### On MacOS (using Homebrew)

   - Run this command in your terminal:
      -       brew install tesseract
    - After installation, **go directly into your project folder** and run this command, it will add Pytesseract to your virtual enviroment and update your **pyproject.toml**:
      -       uv add pytesseract
    - Go into your Python scripts where you would like to use Pytesseract and add:
      -       import pytesseract 


