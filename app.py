import tkinter as tk
import tkinter.ttk as ttk
from tkinter import filedialog
from tkinter import StringVar
from tkinter import PhotoImage
import PyPDF2
from tqdm import tqdm
import time
from gtts import gTTS
import os
import threading
from PIL import Image


window = tk.Tk()
window.resizable(width=False, height=False)
window.title("PDF To Audio Converter")
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
position_x = (screen_width - 400) // 2
position_y = (screen_height - 300) // 2
window.geometry("600x400+{}+{}".format(position_x, position_y))

# Background
image = PhotoImage(file="logo-color.png")
background_label = tk.Label(image=image)
background_label.grid(row=0, column=0, sticky="nsew")

window.grid_rowconfigure(0, weight=1)
window.grid_columnconfigure(0, weight=1)

progress_lock = threading.Lock()

# Calculations
percent_var = StringVar()
percent_var.set("0%")
bar_width = 200
bar_height = 30

# progress bar
progress_bar = ttk.Progressbar(master=window, length=200, variable=percent_var, maximum=100)
percent_label = ttk.Label(master=window, textvariable=percent_var)
progress_bar.place(x=200, y=0, width=200, height=30)
percent_label.place(x=400, y=0, width=30, height=30)


def process_pdf(filelocation):
    # Open the selected file and extract the text using PyPDF2
    with open(filelocation, "rb") as f:
        pdf = PyPDF2.PdfFileReader(f)
        myText = ""
        progress_bar.config(maximum=pdf.numPages)
        for pageNum in tqdm((range(pdf.numPages))):
            time.sleep(0.3)
            pageObj = pdf.getPage(pageNum)
            myText += pageObj.extractText()
            progress_bar.step()

    fileOutput = gTTS(text=myText, lang="en")
    print("Generating Speech...")
    value = fileOutput.save("audio.mp3").time()

    os.system("start audio.mp3")
    print("Successfully Generated!!")

def btn():
    print("Button clicked!")

    filelocation = filedialog.askopenfilename()
    print("Selected file: ", filelocation)

    # Create a new thread and start running the code in the separate thread
    thread = threading.Thread(target=process_pdf, args=(filelocation,))
    thread.start()

button = tk.Button(master=window, text="Select File", command=btn)
button.grid(row=1, column=0, sticky="nsew")

window.mainloop()


