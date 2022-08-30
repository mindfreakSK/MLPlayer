from tkinter import *
from tkinter import Tk
from tkinter import ttk, filedialog
from pygame import mixer
from PIL import ImageTk, Image
from mutagen.mp3 import MP3
import os


#creating the root window
root = Tk()
root.title('SK Player')
root.geometry("920x670+290+85")
root.configure(bg="#0f1a2b")
root.resizable(False, False)


mixer.init()

def Add_Music():
    path = filedialog.askdirectory()
    if path:
        os.chdir(path)
        songs = os.listdir(path)

        for song in songs:
            if song.endswith(".mp3"):
                Playlist.insert(END, song)


def Play_Music():
    Music_Name = Playlist.get(ACTIVE)
    audio = MP3(Music_Name)
    print(audio.info.length)
    print(Music_Name[0:-4])
    mixer.music.load(Playlist.get(ACTIVE))
    mixer.music.play()
    my_progress.start(10)

#def steps():
#  my_progress.start(10)


#Progress Bar
my_progress = ttk.Progressbar(
    root, orient=HORIZONTAL, length=300, mode='determinate')
my_progress.pack(pady=20)

#my_button = Button(root, text='Progress', command=steps)
#my_button.pack(pady=20)


#icon
image_icon = PhotoImage(file="images/logo.png")
root.iconphoto(False, image_icon)


# Play Button
Play = Image.open("images/play button.png")
Play = Play.resize((50, 50), Image.ANTIALIAS)
Button_Play = ImageTk.PhotoImage(Play)
Button(root, image=Button_Play, bg="#0f1a2b", bd=0,
       command=Play_Music).place(x=100, y=400)

# Stop Button
Stop = Image.open("images/stop button.png")
Stop = Stop.resize((50, 50), Image.ANTIALIAS)
Button_Stop = ImageTk.PhotoImage(Stop)
Button(root, image=Button_Stop, bg="#0f1a2b", bd=0,
       command=mixer.music.stop).place(x=30, y=500)

# Resume Button
Resume = Image.open("images/resume button.png")
Resume = Resume.resize((50, 50), Image.ANTIALIAS)
Button_Resume = ImageTk.PhotoImage(Resume)
Button(root, image=Button_Resume, bg="#0f1a2b", bd=0,
       command=mixer.music.unpause).place(x=115, y=500)

# Pause Button
Pause = Image.open("images/pause button.png")
Pause = Pause.resize((50, 50), Image.ANTIALIAS)
Button_Pause = ImageTk.PhotoImage(Pause)
Button(root, image=Button_Pause, bg="#0f1a2b", bd=0,
       command=mixer.music.pause).place(x=200, y=500)

#music

Frame_Music = Frame(root, bd=2, relief=RIDGE)
Frame_Music.place(x=330, y=350, width=500, height=200)

Button(root, text="Add Music", width=15, height=2, font=("times new roman",
       12, "bold"), fg="Black", bg="#21b3de", command=Add_Music).place(x=330, y=300)

Scroll = Scrollbar(Frame_Music)
Playlist = Listbox(Frame_Music, width=100, font=("Times new roman", 10), bg="#333333",
                   fg="grey", selectbackground="lightblue", cursor="hand2", bd=0, yscrollcommand=Scroll.set)
Scroll.config(command=Playlist.yview)
Scroll.pack(side=RIGHT, fill=Y)
Playlist.pack(side=LEFT, fill=BOTH)

root.mainloop()
