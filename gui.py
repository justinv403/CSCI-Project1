from tkinter import *
from classes import *

class GUI:
    def __init__(self, window):
        self.my_tv = Television
        self.window = window

        self.frame_power = Frame(self.window)
        self.powerButton = Button(self.frame_power, text="■",font=("Segoe UI", 15), height=1,width=2,bg="red")
        self.powerButton.pack(side="left")
        self.frame_power.pack(anchor="n", pady=15)
        
        self.frame_volume = Frame(self.window)
        self.volumeUpButton = Button(self.frame_volume, text="+",font=("Segoe UI", 20), height=1,width=4)
        self.volumeDownButton = Button(self.frame_volume, text="-",font=("Segoe UI", 20), height=1,width=4)
        self.volumeUpButton.pack(side="top")   # anchor='w' helps to change the frame position from center to west.
        self.volumeDownButton.pack(side="bottom")
        self.frame_volume.pack(anchor="n", pady=15)

        self.frame_channel = Frame(self.window)
        self.channelUpButton = Button(self.frame_channel, text="CH+",font=("Segoe UI", 20), height=1,width=4)
        self.channelDownButton = Button(self.frame_channel, text="CH-",font=("Segoe UI", 20), height=1,width=4)
        self.channelUpButton.pack(side="top")   # anchor='w' helps to change the frame position from center to west.
        self.channelDownButton.pack(side="bottom")
        self.frame_channel.pack(anchor="n", pady=15)        
        
        self.frame_status = Frame(self.window)
        self.status_var = StringVar()
        self.label_status = Label(self.frame_status, text=self.my_tv.get_status(),font=("Segoe UI",20))
        self.label_status.pack()
        self.frame_status.pack(anchor="n")

    def volumeUpClicked(self):
        pass