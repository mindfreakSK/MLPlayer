#Import libraries
from ast import Lambda
from cgitb import text
from tkinter import *
from tkinter import filedialog
import tkinter.ttk as ttk 
import pygame
import time
from mutagen.mp3 import MP3

#Creating the root window
root = Tk()
root.title('SK Player')
root.iconbitmap("images\logo.ico")
root.geometry("500x400")

#Initialize Pygame Mixer
pygame.mixer.init()

#Song length information
def play_time():
       
       if stopped:
            return
       
       current_time=pygame.mixer.music.get_pos()/1000

       #through temp label
       converted_current_time=time.strftime('%M:%S',time.gmtime(current_time))       

       #Current playing song
       #current_song = song_box.curselection()
       song = song_box.get(ACTIVE)
       song = f'C:/Users/Shahbaz/Downloads/Songs/{song}'
       song_mut=MP3(song)

       global song_length
       song_length=song_mut.info.length
       converted_song_length = time.strftime('%M:%S', time.gmtime(song_length))

       current_time +=1
       if int(my_slider.get()) == int(song_length):
           status_bar.config(text=f'Time Elapsed: {converted_song_length} of {converted_song_length} ')

       elif paused:
            pass

       elif int(my_slider.get()) == int(current_time):
           #Update slider to position
            slider_position = int(song_length)
            my_slider.config(to=slider_position, value=int(current_time))

            
       else:
            slider_position = int(song_length)
            my_slider.config(to=slider_position, value=int(my_slider.get()))
            converted_current_time = time.strftime('%M:%S', time.gmtime(int(my_slider.get())))
            status_bar.config(text=f'Time Elapsed: {converted_current_time} of {converted_song_length} ')
            next_time=int(my_slider.get())+1
            my_slider.config(value=next_time)
            
       #update time
       status_bar.after(1000,play_time)

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
    global stopped
    stopped=False
    song = song_box.get(ACTIVE)
    song = f'C:/Users/Shahbaz/Downloads/Songs/{song}'

    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)

    #Calling Play Time Function
    play_time()   

    #Update Slider to position
    """slider_position=int(song_length)
    my_slider.config(to=slider_position,value=0)"""

global stopped
stopped=False

#Stop playing current song
def stop():
    #Reset slider bar
    status_bar.config(text='')
    my_slider.config(value=0)
    #Stop song
    pygame.mixer.music.stop()
    song_box.selection_clear(ACTIVE)
    status_bar.config(text='')   

    global stopped
    stopped=True

#Create global pause variable
global paused
paused = False

#Delete song
def delete_songs():
       stop() 
       song_box.delete(ANCHOR)
       pygame.mixer.music.stop()


#Delete all songs
def delete_all_songs():
       stop() 
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

#Slider function
def slide(x):

    #slider_label.config(text=f'{int(my_slider.get())} of {int(song_length)}')
    song = song_box.get(ACTIVE)
    song = f'C:/Users/Shahbaz/Downloads/Songs/{song}'

    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0,start=int(my_slider.get()))



#Next Song play function
def next_song():
    
    #Reset Status and slider Bar
    status_bar.config(text='')
    my_slider.config(value=0)

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

    #Reset Status and slider Bar
    status_bar.config(text='')
    my_slider.config(value=0)

    next_one = song_box.curselection()
    next_one = next_one[0]-1
    song = song_box.get(next_one)
    song = f'C:/Users/Shahbaz/Downloads/Songs/{song}'
    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)
    song_box.selection_clear(0, END)
    song_box.activate(next_one)
    song_box.selection_set(next_one, last=None)




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

#Create Status Bar
status_bar=Label(root,text='', bd=1, relief=GROOVE, anchor=E)
status_bar.pack(fill=X,side=BOTTOM,ipady=2)

#Time/Music slider
my_slider=ttk.Scale(root,from_=0,to_=100, orient=HORIZONTAL,value=0,command=slide,length=360)
my_slider.pack(pady=30)

root.mainloop()
