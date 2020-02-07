from tkinter import *
import tkinter as tk
import tkinter.ttk
from PIL import Image, ImageTk
import os.path


root = tk.Tk()

root.geometry("{}x{}".format(965, 600))
root.minsize(250, 100)


class puhlayer:
    def __init__(self):
        self.status = tk.Label(root, text="    loading..", bd=1, relief=SUNKEN, anchor=W)
        self.status.pack(side=BOTTOM, fill=X, )

        self.framey = tk.Frame(root)
        self.imglist = []    #CHECK

        self.flag = False
        root.bind("<space>",self.space_key)
        root.bind("<Right>",self.Right_key)
        root.bind("<Left>",self.Left_key)

        self.load_img()     #CHECK

        self.new_width , self.new_height = self.imglist[0].size

        previous_track_icon = tk.PhotoImage(
            file='C:\\Users\\pinto\\Documents\\GitHub\\tkinter_player\\player_icons\\previous_track.gif')
        previous_track_button = tk.Button(
            self.framey, image=previous_track_icon, borderwidth=0, padx=0,
            command=self.on_previous_track_button_clicked)
        previous_track_button.image = previous_track_icon
        previous_track_button.pack(side=LEFT)

        play_icon = tk.PhotoImage(file='C:\\Users\\pinto\\Documents\\GitHub\\tkinter_player\\player_icons\\play.gif')
        play_stop_button = tk.Button(
            self.framey, image=play_icon, borderwidth=0, padx=0, command=self.on_play_button_clicked)
        play_stop_button.image = play_icon
        play_stop_button.pack(side=LEFT)

        pause_icon = tk.PhotoImage(file='C:\\Users\\pinto\\Documents\\GitHub\\tkinter_player\\player_icons\\pause.gif')
        pause_unpause_button = tk.Button(
            self.framey, image=pause_icon, borderwidth=0, padx=0, command=self.on_pause_button_clicked)
        pause_unpause_button.image = pause_icon
        pause_unpause_button.pack(side=LEFT)

        next_track_icon = tk.PhotoImage(
            file='C:\\Users\\pinto\\Documents\\GitHub\\tkinter_player\\player_icons\\next_track.gif')
        next_track_button = tk.Button(
            self.framey, image=next_track_icon, borderwidth=0, padx=0, command=self.on_next_track_button_clicked)
        next_track_button.image = next_track_icon
        next_track_button.pack(side=LEFT)

        self.scrollbar = tkinter.ttk.Scale(
            self.framey, from_=1, to=int(len(self.imglist)), command=self.on_scrollbar_changed)
        self.scrollbar.pack(side=RIGHT, fill=X, expand=YES, padx=5)

        self.framey.pack(side=BOTTOM, fill=X)

        self.img =self.imglist[0]
        self.background_image = ImageTk.PhotoImage(self.img)
        self.img_copy = self.img.copy()
        self.background_label = tk.Label(root, image=self.background_image)
        self.background_label.pack(side=BOTTOM, fill=BOTH, expand=YES)
        self.background_label.bind('<Configure>', self._resize_image)

    def on_previous_track_button_clicked(self):
        self.scrollbar.set(1)

    def on_play_button_clicked(self):
        self.flag = True
        self.i = int(self.scrollbar.get())
        self.fps = 24

        self.all_jobs = []

        for i in range(int(self.i), len(self.imglist)):
            self._job = self.background_label.after(round(1000 / self.fps) * (i + 1), self._change_image)
            self.all_jobs.append(self._job)

    def on_pause_button_clicked(self):
        self.flag = False
        if self.all_jobs is not None:
            for job in self.all_jobs:
                self.background_label.after_cancel(job)
            self._job = None
        self.all_jobs.clear()


    def on_next_track_button_clicked(self):
        self.scrollbar.set(int(len(self.imglist)))

    def on_scrollbar_changed(self,e=None):
        value = self.scrollbar.get()
        if int(value) != value:
            self.scrollbar.set(round(value))

        self.image = self.imglist[round(value)-1]
        self.img_copy = self.image.copy()

        self.img = self.img_copy.resize((self.new_width, self.new_height))

        self.background_image = ImageTk.PhotoImage(self.img)
        self.background_label.configure(image=self.background_image)
        self.background_label.pack(side=BOTTOM,fill=BOTH, expand=YES)
        self.background_label.bind('<Configure>', self._resize_image)
        text = "playing image " + str(round(value))
        self.status.configure(text=text)

    def load_img(self):
        ################################_LOADING_THE IMAGES_########################################
        # this will be passed on application usage

        Video_path = "C:\\Users\\pinto\\Documents\\GitHub\\tkinter_player\\compressed_images"

        for file in os.listdir(Video_path):
            if file.endswith(".jpg"):
                img = Image.open(Video_path + '/' + file)
                self.imglist.append(img)
                #print("loading ", len(self.imglist))    #FOR DEBUGGING

        ############################################################################################

    def _resize_image(self, event):
        self.new_width = event.width
        self.new_height = event.height
        #print(self.new_width, self.new_height)   #FOR DEBUGGING
        self.img = self.img_copy.resize((self.new_width, self.new_height))

        self.background_image = ImageTk.PhotoImage(self.img)
        self.background_label.configure(image=self.background_image)

    def _change_image(self):
        self.i = self.i + 1
        self.scrollbar.set(self.i)

    def space_key(self,event):
        if self.flag:
            self.on_pause_button_clicked()
        else:
            self.on_play_button_clicked()

    def Right_key(self,event):
        value = self.scrollbar.get()
        self.scrollbar.set(round(value)+1)
    def Left_key(self,event):
        value = self.scrollbar.get()
        self.scrollbar.set(round(value)-1)


e = puhlayer()
root.mainloop()
