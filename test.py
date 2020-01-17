from tkinter import *
import tkinter as tk
import tkinter.ttk
from PIL import Image, ImageTk

root = tk.Tk()

root.geometry("{}x{}".format(965, 600))
root.minsize(250, 100)

class puhlayer:

    def on_previous_track_button_clicked(self):
        pass


    def on_rewind_button_clicked(self):
        pass


    def on_play_stop_button_clicked(self):
        pass


    def on_pause_unpause_button_clicked(self):
        pass


    def on_mute_unmute_button_clicked(self):
        pass


    def on_fast_forward_button_clicked(self):
        pass


    def on_next_track_button_clicked(self):
        pass

    def on_volume_scale_changed(self,value):
        pass

    def __init__(self):
        status = tk.Label(root, text="    testing..", bd=1, relief=SUNKEN, anchor=W)
        status.pack(side=BOTTOM, fill=X, )

        self.framey = tk.Frame(root)

        previous_track_icon = tk.PhotoImage(file='/Users/plangle-08/Player/player_icons/previous_track.gif')
        previous_track_button = tk.Button(
            self.framey, image=previous_track_icon, borderwidth=0, padx=0, command=self.on_previous_track_button_clicked)
        previous_track_button.image = previous_track_icon
        previous_track_button.pack(side=LEFT)

        rewind_icon = tk.PhotoImage(file='/Users/plangle-08/Player/player_icons/rewind.gif')
        rewind_button = tk.Button(
            self.framey, image=rewind_icon, borderwidth=0, padx=0, command=self.on_rewind_button_clicked)
        rewind_button.image = rewind_icon
        rewind_button.pack(side=LEFT)

        play_icon = tk.PhotoImage(file='/Users/plangle-08/Player/player_icons/play.gif')
        stop_icon = tk.PhotoImage(file='/Users/plangle-08/Player/player_icons/stop.gif')
        play_stop_button = tk.Button(
            self.framey, image=play_icon, borderwidth=0, padx=0, command=self.on_play_stop_button_clicked)
        play_stop_button.image = play_icon
        play_stop_button.pack(side=LEFT)

        pause_icon = tk.PhotoImage(file='/Users/plangle-08/Player/player_icons/pause.gif')
        pause_unpause_button = tk.Button(
            self.framey, image=pause_icon, borderwidth=0, padx=0, command=self.on_pause_unpause_button_clicked)
        pause_unpause_button.image = pause_icon
        pause_unpause_button.pack(side=LEFT)

        fast_forward_icon = tk.PhotoImage(file='/Users/plangle-08/Player/player_icons/fast_forward.gif')
        fast_forward_button = tk.Button(
            self.framey, image=fast_forward_icon, borderwidth=0, padx=0, command=self.on_fast_forward_button_clicked)
        fast_forward_button.image = fast_forward_icon
        fast_forward_button.pack(side=LEFT)

        next_track_icon = tk.PhotoImage(file='/Users/plangle-08/Player/player_icons/next_track.gif')
        next_track_button = tk.Button(
            self.framey, image=next_track_icon, borderwidth=0, padx=0, command=self.on_next_track_button_clicked)
        next_track_button.image = next_track_icon
        next_track_button.pack(side=LEFT)

        volume_scale = tkinter.ttk.Scale(
            self.framey, from_=0.0, to=1.0, command=self.on_volume_scale_changed)
        volume_scale.set(0.6)
        volume_scale.pack(side=RIGHT,fill=X , expand=YES , padx =5 )

        self.framey.pack(side=BOTTOM,fill=X)


        Video_path = "/Users/plangle-08/Documents/GitHub/tkinter_player/100_jpg_images/shot_01_v010593.jpg"
        self.img = Image.open(Video_path)
        self.background_image = ImageTk.PhotoImage(self.img)
        self.imkge = self.img.copy()
        self.trying = tk.Label(root, image=self.background_image)
        self.trying.pack(side=BOTTOM, fill=BOTH,expand=YES)
        self.trying.bind('<Configure>', self._resize_image)

    def _resize_image(self,event):
        new_width = event.width
        new_height = event.height
        print(new_width, new_height)
        self.img = self.imkge.resize((new_width, new_height))

        self.background_image = ImageTk.PhotoImage(self.img)
        self.trying.configure(image=self.background_image)

e = puhlayer()
root.mainloop()
