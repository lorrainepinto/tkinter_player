from tkinter import *
from PIL import Image, ImageTk
import os.path

################################_LOADING_THE IMAGES_########################################
# this will be passed on application usage

Video_path = "/Users/plangle-08/Player/compressed_images"

doctor = []

for file in os.listdir(Video_path):
    img = Image.open(Video_path + '/' + file)
    doctor.append(img)
    print("loading ", len(doctor))

############################################################################################

root = Tk()
root.title("Title")

# root.geometry("{}x{}".format(960, 540))
root.configure(background="black")


class Example(Frame):
    def __init__(self, master, *pargs):
        Frame.__init__(self, master, *pargs)

        self.i = 0
        self.fps = 24
        self.image = doctor[self.i]

        self.img_copy = self.image.copy()

        self.background_image = ImageTk.PhotoImage(self.image)

        self.background = Label(self, image=self.background_image)

        self.background.pack(fill=BOTH, expand=YES)
        self.background.bind('<Configure>', self._resize_image)

        for i in range(0, len(doctor) - 1):
            self.background.after(round(1000 / self.fps) * (i + 1), self._change_image)

    def _resize_image(self, event):
        new_width = event.width
        new_height = event.height

        self.image = self.img_copy.resize((new_width, new_height))

        self.background_image = ImageTk.PhotoImage(self.image)
        self.background.configure(image=self.background_image)

    def _change_image(self):
        self.i = self.i + 1
        print(self.i)  # FOR DEBUGGING
        self.background.bind('<Configure>', self._resize_image)
        self.image = doctor[self.i]
        self.img_copy = self.image.copy()

        self.background_image = ImageTk.PhotoImage(self.image)
        self.background.configure(image=self.background_image)
        self.background.pack(fill=BOTH, expand=YES)


e = Example(root)
e.pack(fill=BOTH, expand=YES)

root.mainloop()
