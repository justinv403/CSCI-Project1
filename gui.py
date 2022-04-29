from tkinter import *
from classes import *

class GUI:
    def __init__(self, window):
        self.my_tv = Television()
        self.window = window

        self.frame_power = Frame(self.window)
        self.powerButton = Button(self.frame_power, text="■",font=("Segoe UI", 15), height=1,width=2,bg="red", command=self.powerClicked)
        self.powerButton.pack(side="left")
        self.frame_power.pack(anchor="n", pady=15)
        
        self.frame_volume = Frame(self.window)
        self.volumeUpButton = Button(self.frame_volume, text="+",font=("Segoe UI", 20), height=1,width=4, command=self.volumeUpClicked)
        self.volumeDownButton = Button(self.frame_volume, text="-",font=("Segoe UI", 20), height=1,width=4, command=self.volumeDownClicked)
        self.volumeUpButton.pack(side="top")
        self.volumeDownButton.pack(side="bottom")
        self.frame_volume.pack(anchor="n", pady=15)

        self.frame_channel = Frame(self.window)
        self.channelUpButton = Button(self.frame_channel, text="CH+",font=("Segoe UI", 20), height=1,width=4, command=self.channelUpClicked)
        self.channelDownButton = Button(self.frame_channel, text="CH-",font=("Segoe UI", 20), height=1,width=4, command=self.channelDownClicked)
        self.channelUpButton.pack(side="top")
        self.channelDownButton.pack(side="bottom")
        self.frame_channel.pack(anchor="n", pady=15)        
        
        self.frame_status = Frame(self.window)
        self.status_var = StringVar()
        self.label_status = Label(self.frame_status, text="Off",font=("Segoe UI",20))
        self.label_status2 = Label(self.frame_status, text="",font=("Segoe UI",20))
        self.label_status3 = Label(self.frame_status, text="",font=("Segoe UI",20))
        self.label_status.pack()
        self.label_status2.pack(side="bottom")
        self.label_status3.pack(side="bottom")
        self.frame_status.pack(anchor="n", pady="50")

    def powerClicked(self):
        self.my_tv.power()
        self.updateLabel()
    
    def volumeUpClicked(self):
        self.my_tv.volume_up()
        self.updateLabel()

    def volumeDownClicked(self):
        self.my_tv.volume_down()
        self.updateLabel()

    def channelUpClicked(self):
        self.my_tv.channel_up()
        self.updateLabel()

    def channelDownClicked(self):
        self.my_tv.channel_down()
        self.updateLabel()

    # this updates the labels to display to the user
    # reduces the amount of times this code has to be written   
    def updateLabel(self):
        if self.my_tv.get_status()[0] == 1:
            self.powerButton.configure(bg="green")
            self.label_status.configure(text="On")
            self.label_status2.configure(text="Channel = " + str(self.my_tv.get_status()[1]))
            self.label_status3.configure(text="Volume = " + str(self.my_tv.get_status()[2]))
        else:
            self.powerButton.configure(bg="red")
            self.label_status.configure(text="Off")
            self.label_status2.configure(text="")
            self.label_status3.configure(text="")