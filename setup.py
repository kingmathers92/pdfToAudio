from setuptools import setup

setup(
    name="PDF To Audio Converter",
    version="1.0",
    description="A simple PDF to audio converter app",
    author="Khaled Ben Yahya",
    author_email="khaledb.yahya@gmail.com",
    packages=["PyPDF2", "gtts", "tqdm", "tkinter", "Pillow"],
    entry_points={
        "console_scripts": [
            "pdf-to-audio=pdf_to_audio:process_pdf"
        ]
    }
)
