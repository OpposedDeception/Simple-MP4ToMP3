from tkinter import *
from tkinter import filedialog
from tkinter import ttk
import moviepy.editor as mp
from tkinter import messagebox

window = Tk()
window.title("Mp4 To Mp3")
upload = ttk.Label(window, text="Upload your file.")
upload.place(x=150, y=20)
def converter():
    try:
        videoname = filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("mp4 files","*.mp4"),("all files","*.*")))
        filename = videoname.replace("\\","/")
        clip = mp.VideoFileClip(filename)
        audio_name = filename.replace(".mp4",".mp3")
        clip.audio.write_audiofile(audio_name)
    except:
        messagebox.showwarning(title="Error", message="An error has been occured!")
    else:
        messagebox.showinfo(title="Succeed", message="Your file has been converted successfully.")
        upload_button = ttk.Button(window, text="Click To Upload", command=action)
        upload_button.place(x=50, y=20)
        
help_text = """
Help:
1 — Wait until app asks to choose file.
2 — Choose the video you want to convert.
3 — Wait for some seconds.
4 — You’ll find the audio within the video’s folder I guess.
"""
upload = ttk.Button(window, text="Click To Choose", command=converter())
help = ttk.Label(window, text=help_text)
help.place(x=20, y=50)

window.resizable(True,True)
window.geometry('500x500')
window.mainloop()
