from tkinter import *
import tkinter as tk
import tkinter.ttk
from PIL import Image,ImageTk

root = Tk()
root.geometry("{}x{}".format(965, 600))
def on_previous_track_button_clicked():
    pass


def on_rewind_button_clicked():
    pass


def on_play_stop_button_clicked():
    pass


def on_pause_unpause_button_clicked():
    pass


def on_mute_unmute_button_clicked():
    pass


def on_fast_forward_button_clicked():
    pass


def on_next_track_button_clicked():
    pass


def on_volume_scale_changed(value):
    pass


def on_add_file_button_clicked():
    pass


def on_remove_selected_button_clicked():
    pass


def on_add_directory_button_clicked():
    pass

def on_clear_play_list_button_clicked():
    pass


def on_remove_selected_context_menu_clicked():
    pass


def on_play_list_double_clicked(event=None):
    pass

frame = tk.Frame(root)
Video_path = "/Users/plangle-08/Player/compressed_images/Compressed_scene_04_shot_10_0053.jpg"
img = Image.open(Video_path)
background_image = ImageTk.PhotoImage(img)
background = tk.Label(frame,image=background_image)
background.grid(row=0,columnspan=7)

previous_track_icon = tk.PhotoImage(file='/Users/plangle-08/Player/player_icons/previous_track.gif')
previous_track_button = tk.Button(
    frame, image=previous_track_icon, borderwidth=0, padx=0, command=on_previous_track_button_clicked)
previous_track_button.image = previous_track_icon
previous_track_button.grid(row=1, column=0, sticky='we')

rewind_icon = tk.PhotoImage(file='/Users/plangle-08/Player/player_icons/rewind.gif')
rewind_button = tk.Button(
    frame, image=rewind_icon, borderwidth=0, padx=0, command=on_rewind_button_clicked)
rewind_button.image = rewind_icon
rewind_button.grid(row=1, column=1, sticky='we')

play_icon = tk.PhotoImage(file='/Users/plangle-08/Player/player_icons/play.gif')
stop_icon = tk.PhotoImage(file='/Users/plangle-08/Player/player_icons/stop.gif')
play_stop_button = tk.Button(
    frame, image=play_icon, borderwidth=0, padx=0, command=on_play_stop_button_clicked)
play_stop_button.image = play_icon
play_stop_button.grid(row=1, column=2,sticky='we')

pause_icon = tk.PhotoImage(file='/Users/plangle-08/Player/player_icons/pause.gif')
pause_unpause_button = tk.Button(
    frame, image=pause_icon, borderwidth=0, padx=0, command=on_pause_unpause_button_clicked)
pause_unpause_button.image = pause_icon
pause_unpause_button.grid(row=1, column=3,sticky='we')

fast_forward_icon = tk.PhotoImage(file='/Users/plangle-08/Player/player_icons/fast_forward.gif')
fast_forward_button = tk.Button(
    frame, image=fast_forward_icon, borderwidth=0, padx=0, command=on_fast_forward_button_clicked)
fast_forward_button.image = fast_forward_icon
fast_forward_button.grid(row=1, column=4,sticky='we')

next_track_icon = tk.PhotoImage(file='/Users/plangle-08/Player/player_icons/next_track.gif')
next_track_button = tk.Button(
    frame, image=next_track_icon, borderwidth=0, padx=0, command=on_next_track_button_clicked)
next_track_button.image = next_track_icon
next_track_button.grid(row=1, column=5,sticky='we')

volume_scale = tkinter.ttk.Scale(
    frame, from_=0.0, to=1.0, length=960, command=on_volume_scale_changed)
volume_scale.set(0.6)
volume_scale.grid(row=2, columnspan=6,sticky='we')

frame.grid(row=1, columnspan=5, sticky='we')


root.mainloop()