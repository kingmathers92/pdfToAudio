import tkinter as tk
import tkinter.ttk as ttk
from tkinter import filedialog
from tkinter import StringVar
import PyPDF2
from tqdm import tqdm
import time
from gtts import gTTS
import os
import threading

window = tk.Tk()
window.resizable(width=False, height=False)
window.title("PDF To Audio Converter")
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
position_x = (screen_width - 400) // 2
position_y = (screen_height - 300) // 2
window.geometry("400x300+{}+{}".format(position_x, position_y))

progress_lock = threading.Lock()

# Calculations
percent_var = StringVar()
percent_var.set("{percent}% ({value}/{max})")
bar_width = 200
bar_height = 30
bar_x = (window.winfo_width() - bar_width) // 2
bar_y = (window.winfo_height() - bar_height) // 2

# progress bar
progress_bar = ttk.Progressbar(master=window, length=200, variable=percent_var)
progress_bar.pack(side="top")
progress_bar.place(x=bar_x, y=bar_y, width=bar_width, height=bar_height)

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
button.pack(side="bottom")

window.mainloop()


