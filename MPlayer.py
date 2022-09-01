from ast import Lambda
from tkinter import *
from tkinter import filedialog
import tkinter
import pygame


#creating the root window
root = Tk()
root.title('SK Player')
root.iconbitmap("images\logo.ico")
root.geometry("500x300")

#Add song function


def add_song():
    song = filedialog.askopenfilename(
        initialdir='C:/Users/Shahbaz/Downloads/Songs', title='Choose song', filetypes=(('mp3 Files', '*.mp3'),))
    song = song.replace("C:/Users/Shahbaz/Downloads/Songs/", "")
    song_box.insert(END, song)

#Add many song


def add_many_song():
    songs = filedialog.askopenfilenames(
        initialdir='C:/Users/Shahbaz/Downloads/Songs', title='Choose song', filetypes=(('mp3 Files', '*.mp3'),))
    for song in songs:
        song = song.replace("C:/Users/Shahbaz/Downloads/Songs/", "")
        song_box.insert(END, song)

#Play Song function


def play():
    song = song_box.get(ACTIVE)
    song = f'C:/Users/Shahbaz/Downloads/Songs/{song}'

    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)


#Stop playing current song
def stop():
    pygame.mixer.music.stop()
    song_box.selection_clear(ACTIVE)


#Create global pause variable
global paused
paused = False

#Delete song
def delete_songs():
       song_box.delete(ANCHOR)
       pygame.mixer.music.stop()


def delete_all_songs():
       song_box.config(state=NORMAL)
       song_box.delete(0, END)
       pygame.mixer.music.stop()

#Pause playing current song
def pause(is_paused):
    global paused
    paused = is_paused

    if paused:
        #pause song
        pygame.mixer.music.unpause()
        paused = False
    else:
        #unpause
        pygame.mixer.music.pause()
        paused = True


#Next Song play function
def next_song():
    next_one = song_box.curselection()
    next_one = next_one[0]+1
    song = song_box.get(next_one)
    song = f'C:/Users/Shahbaz/Downloads/Songs/{song}'
    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)
    song_box.selection_clear(0, END)
    song_box.activate(next_one)
    song_box.selection_set(next_one, last=None)

#Previous Song play function


def prev_song():
    next_one = song_box.curselection()
    next_one = next_one[0]-1
    song = song_box.get(next_one)
    song = f'C:/Users/Shahbaz/Downloads/Songs/{song}'
    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)
    song_box.selection_clear(0, END)
    song_box.activate(next_one)
    song_box.selection_set(next_one, last=None)


#Initialize Pygame Mixer
pygame.mixer.init()

song_box = Listbox(root, bg='black', fg='green', width=60,
                   selectbackground='gray', selectforeground='black')
song_box.pack(pady=20)


#Define Player Control Buttons Images

back_btn_img = PhotoImage(file="images/back_btn.png")
forward_btn_img = PhotoImage(file="images/forward_btn.png")
play_btn_img = PhotoImage(file="images/play_btn.png")
pause_btn_img = PhotoImage(file="images/pause_btn.png")
stop_btn_img = PhotoImage(file="images/stop_btn.png")

#Create Player Control Frame
controls_frame = Frame(root)
controls_frame.pack()


#Create Player Control Button
back_btn = Button(controls_frame, image=back_btn_img,
                  border=0, command=prev_song)
forward_btn = Button(controls_frame, image=forward_btn_img,
                     border=0, command=next_song)
play_btn = Button(controls_frame, image=play_btn_img, border=0, command=play)
pause_btn = Button(controls_frame, image=pause_btn_img,
                   border=0, command=lambda: pause(paused))
stop_btn = Button(controls_frame, image=stop_btn_img, border=0, command=stop)

back_btn.grid(row=0, column=1)
forward_btn.grid(row=0, column=2)
play_btn.grid(row=0, column=3)
pause_btn.grid(row=0, column=4)
stop_btn.grid(row=0, column=5)

#Create Menu
my_menu = Menu(root)
root.config(menu=my_menu)

#Add song Menu
add_song_menu = Menu(my_menu)
my_menu.add_cascade(label="Add Song", menu=add_song_menu)
add_song_menu.add_command(label='Add one song to playlist', command=add_song)

#Add many song to playlist
add_song_menu.add_command(
    label='Add many song to playlist', command=add_many_song)

#Delete song menu
remove_song_menu=Menu(my_menu)
my_menu.add_cascade(label='Remove Songs',menu=remove_song_menu)
remove_song_menu.add_command(label='Delete a Song From Playlist',command=delete_songs)
remove_song_menu.add_command(label='Delete a All Song From Playlist', command=delete_all_songs)

root.mainloop()
