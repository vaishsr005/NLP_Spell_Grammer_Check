# Grammar and Spell Checker Application
## Overview
The Grammar and Spell Checker application is a web-based tool designed to help users identify and correct grammatical errors and spelling mistakes in their text. The application provides a user-friendly interface for both typing text directly and uploading text files for correction.

## How It Works
The application consists of two main components:

- Text Input and Correction: Users can type or paste their text into a provided textarea and submit it for grammar and spell checking.
- File Upload and Correction: Users can upload text files which are then processed to identify and correct any grammar or spelling mistakes.

Ran on host: http://127.0.0.1:5000

### Screenshots for demo:
#### 1. Webpage: 

    ![Webpage](https://github.com/user-attachments/assets/f5793b3b-ee5f-4072-a150-22bc79814756)   

#### 2. Input Text: 

    ![Input](https://github.com/user-attachments/assets/c802d95d-afda-4a76-b453-20565f969d24)

#### 3. Correct Text: 

    ![Result](https://github.com/user-attachments/assets/e4ff1d2e-1eb9-45d3-9af9-bf158976282d)

#### 4. Text file with grammer errors: 

    ![Text file](https://github.com/user-attachments/assets/822a2f4d-b8d1-4176-a0bd-e0287e667fc9)

#### 5. Text file corrected: 

    ![File text corrected](https://github.com/user-attachments/assets/60b23b9a-0592-4ea1-8d75-992c6909bb1d)

## Workflow
### User Interface: 
- The interface is built using HTML, CSS, and Bootstrap for styling.
- Users can input text directly into a textarea or upload a file using the provided form.
- The results, including corrected text and identified grammar mistakes, are displayed on the same page.

### Backend Processing:
- The backend is developed using Python and Flask, which handles form submissions and file uploads.
- Text processing for grammar and spelling corrections is performed using natural language processing (NLP) libraries.
- Libraries and Technologies Used

### Frontend:
- HTML: Provides the structure of the web page.
- CSS: Custom styles are added for better user experience.
- Bootstrap: Used for responsive design and styling of forms and buttons.
- JavaScript: Utilized for handling form submissions and integrating Bootstrap functionalities.

### Backend:
- Python: The primary programming language for backend development.
- Flask: A micro web framework for Python used to create the web server and handle requests.
- Natural Language Toolkit (nltk): A library used for text processing and grammar checking.
- TextBlob: Simplifies text processing tasks like part-of-speech tagging, noun phrase extraction, and sentiment analysis.
- Flask-WTF: An extension of Flask for handling web forms.
