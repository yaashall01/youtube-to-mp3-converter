import tkinter as tk
from tkinter import messagebox, filedialog
from threading import Thread
import os
import sys

# Importing the downloader and converter modules
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))
from downloader import download_video
from converter import convert_to_mp3

def start_conversion_process(url, save_path):
    status_label.config(text="Downloading...")
    video_path = download_video(url, save_path)
    if video_path:
        status_label.config(text="Converting to MP3...")
        success = convert_to_mp3(os.path.join(save_path, video_path))
        if success:
            status_label.config(text="Conversion Completed Successfully.")
        else:
            status_label.config(text="Error in conversion.")
    else:
        status_label.config(text="Download failed.")

def on_convert_button_click():
    url = url_entry.get()
    if not url.strip():
        messagebox.showerror("Error", "Please enter a YouTube URL")
        return
    save_path = filedialog.askdirectory()
    if not save_path:
        messagebox.showerror("Error", "Please select a save path")
        return
    Thread(target=start_conversion_process, args=(url, save_path)).start()

# Setting up the GUI
root = tk.Tk()
root.title("YouTube to MP3 Converter")

frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

url_label = tk.Label(frame, text="Enter YouTube URL:")
url_label.pack()

url_entry = tk.Entry(frame, width=50)
url_entry.pack()

convert_button = tk.Button(frame, text="Convert", command=on_convert_button_click)
convert_button.pack(pady=10)

status_label = tk.Label(frame, text="")
status_label.pack()

root.mainloop()
