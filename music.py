from tkinter import *
from PIL import ImageTk, Image
import os
from pygame import mixer
co1= "#ffffff" #white
co2 = "3C1DC6" #purple
co3 = "black" #black
co4 = "black"

window= Tk()
window.title("Grim Music Player")
window.geometry('352x255')
window.configure(background=co1)
window.resizable(width=FALSE, height=FALSE)

#events
def play_music():
    running = listbox.get(ACTIVE)
    running_song['text'] =running
    mixer.music.load(running)
    mixer.music.play()

#frames
left_frame = Frame(window, width=150, height=150, bg=co1)
left_frame.grid(row=0, column=0, padx=1, pady=1)

right_frame = Frame(window, width=150, height=150, bg=co3)
right_frame.grid(row=0, column=1, padx=0, pady=0)

down_frame = Frame(window, width=400, height=100, bg=co4)
down_frame.grid(row=1, column=0, columnspan=3, padx=0, pady=0)

#list_music
listbox= Listbox(right_frame, selectmode=SINGLE, font=("Arial 9 bold"), width=22, bg=co3,fg=co1)
listbox.grid(row=0, column=0)

w = Scrollbar(right_frame)
w.grid(row=0,column=1)

listbox.config(yscrollcommand=w.set)
w.config(command=listbox.yview)
#images'
img_1 = Image.open('Icons/PlayerIcon.png')
img_1 = img_1.resize((130,130))
img_1 = ImageTk.PhotoImage(img_1)
app_image = Label(left_frame, height=130, image=img_1, padx=10)
app_image.place(x=24, y=15)

img_2 = Image.open('Icons/Rewind.png')
img_2 = img_2.resize((30,30))
img_2 = ImageTk.PhotoImage(img_2)
app_image = Button(down_frame, height=40, width=40, image=img_2, padx=10, bg=co1, font=("Ivy 10"))
app_image.place(x=10+28, y=35)

img_3 = Image.open('Icons/Play_Button.png')
img_3 = img_3.resize((30,30))
img_3 = ImageTk.PhotoImage(img_3)
app_image = Button(down_frame, height=40, width=40, image=img_3, padx=10, bg=co1, font=("Ivy 10"), command=play_music)
app_image.place(x=56+28, y=35)

img_4 = Image.open('Icons/forward.png')
img_4 = img_4.resize((30,30))
img_4 = ImageTk.PhotoImage(img_4)
app_image = Button(down_frame, height=40, width=40, image = img_4, padx=10, bg=co1, font=("Ivy 10"))
app_image.place(x=102+28, y=35)

img_5 = Image.open('Icons/Pause.png')
img_5 = img_5.resize((30,30))
img_5 = ImageTk.PhotoImage(img_5)
app_image = Button(down_frame, height=40, width=40, image = img_5, padx=10, bg=co1, font=("Ivy 10"))
app_image.place(x=148+28, y=35)

img_6 = Image.open('Icons/Repeat.png')
img_6 = img_6.resize((30,30))
img_6 = ImageTk.PhotoImage(img_6)
app_image = Button(down_frame, height=40, width=40, image = img_6, padx=10, bg=co1, font=("Ivy 10"))
app_image.place(x=194+28, y=35)

line = Label(left_frame, width=200, height=1,padx=10, bg= co3)
line.place(x=0,y=1)

line = Label(left_frame, width=200, height=1,padx=10, bg=co1)
line.place(x=0,y=3)

#Line_for_
running_song = Label(down_frame, text="Choose a Song", font=("Ivy 10"), width=44, height=1,padx=10,bg=co1, fg=co3, anchor=NW)
running_song.place(x=0, y=1)



os.chdir(r'C:\Users\jenyx\OneDrive\Desktop\Music_Player_Assets\songs')
songs = os.listdir()
def show():
    for i in songs:
        listbox.insert(END, i)
show()

mixer.init()
music_state = StringVar()
music_state.set("Choose one!")
window.mainloop()