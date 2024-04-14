# PDF2Notes
## Introduction
* PDF2Notes is a simple Python application that utilizes OpenAI's GPT API to quickly convert PDF's into notes. Simply select a PDF from within your filesystem and a location to store the document that will be created when ChatGPT has finished extracting the important details from your PDF.
## Getting Started
* Before using the application you'll need to have an OpenAI API key. If you don't already have one, see OpenAI's API documentation for instructions on this step.
## Dependencies
* You'll need the following dependencies installed in order for this application to function. (_**Note:** Later this repository will be updated to include a makefile and handle dependency installation in a simpler way. For now, manual installation is the only option_)
*
    ###Python >v3.10
    Debian
    ```bash
        apt-get install python3 python3-dev
    ```
    ###OpenAI
    ```bash
        pip install openai
    ```
    ###dotenv v1.0.1
    ```bash
        pip install python-dotenv
    ```
    ###tkinter v8.5
    ```bash
        pip install tk
    ```
    ###customtkinter v5.2.2
    ```bash
        pip install customtkinter
    ```
    ```bash
        pip install customtkinter --upgrade
    ```
    ###docx v1.1.0
    ```bash
        pip install python-docx
    ```
