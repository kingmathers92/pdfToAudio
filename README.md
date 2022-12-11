# PDF 2 Audio Converter

### Description:

This is a simple Python program that converts a PDF file to audio using the Tkinter, PyPDF2, and gTTS libraries.

To use this program, users can select a PDF file using the "Select File" button. The program will then extract the text from the PDF file and convert it to audio using the gTTS library. The resulting audio file will be saved as an MP3 and played automatically.

The program also includes a progress bar that shows the progress of the conversion process. This is implemented using the ttk.Progressbar and tqdm libraries.

Overall, this program provides a simple and easy-to-use interface for converting PDF files to audio. It started when my girlfriend asked me if I can find her an audio version of a book she was reading so I thought of making this for her.

### Libraries used:

> PyPDF2 to extract, loop and read through pdf's text

> gTTS (Google-To-Text-Speech) that allows you to generate speech from text

> tqdm for creating the progress bar so the user can see visually how long it's taking

> I also used threading because my app froze at first, it's a way to run multiple threads in a single app. Which can make it run faster and make it more responsive to user input.

## Usage:

To run this program in the terminal, you will first need to make sure that you have installed the required libraries in the requirements file using the following commands:

<pre>
pip install -r requirements.txt
</pre>
<pre>
python app.py
</pre>
<pre>
python app.py /path/to/file.pdf
</pre>
