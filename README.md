# Overview

Include a brief overview of the project, include:

- How do you deploy and run the project?

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




- Who is it for and why?
