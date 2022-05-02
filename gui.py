from tkinter import *
from classes import *
from PIL import ImageTk, Image

class GUI:
    def __init__(self, window):
        """
        Initializes the GUI for display to the user

        :param window: This is the window for the GUI passed from main.py (or any program of your choosing)
        """
        
        self.my_tv = Television()
        self.window = window

        self.frame_power = Frame(self.window)
        self.powerButton = Button(self.frame_power, text="■",font=("Segoe UI", 15), height=1,width=2,bg="red", command=self.powerClicked)
        self.powerButton.pack(side="left")
        self.frame_power.pack(anchor="n", pady=15)
        
        self.frame_volume = Frame(self.window)
        self.volumeLabel = Label(self.frame_volume, text="Vol:", font=("Segoe UI", 20))
        self.volumeStatus = Label(self.frame_volume, text = "[----------]", font=("Segoe UI", 20))
        self.volumeLabel.pack(side="left")
        self.volumeStatus.pack(side="top")
        self.frame_volume.pack(anchor="n", pady=15)
        
        self.frame_image = Frame(self.window)
        self.img = ImageTk.PhotoImage(Image.open("./channelImages/tile000.png"))
        self.imageLabel = Label(self.frame_image, image=self.img)
        self.imageLabel.pack(side="top")
        self.frame_image.pack(anchor="n", pady=15)
        
        self.frame_up = Frame(self.window)
        self.channelUpButton = Button(self.frame_up, text="CH+",font=("Segoe UI", 20), height=1,width=4, command=self.channelUpClicked)
        self.volumeUpButton = Button(self.frame_up, text="+",font=("Segoe UI", 20), height=1,width=4, command=self.volumeUpClicked)
        self.volumeUpButton.pack(side="left")
        self.channelUpButton.pack(side="right")
        self.frame_up.pack(anchor="n", pady=15, padx=15)

        self.frame_down = Frame(self.window)
        self.channelDownButton = Button(self.frame_down, text="CH-",font=("Segoe UI", 20), height=1,width=4, command=self.channelDownClicked)
        self.volumeDownButton = Button(self.frame_down, text="-",font=("Segoe UI", 20), height=1,width=4, command=self.volumeDownClicked)
        self.volumeDownButton.pack(side="left")
        self.channelDownButton.pack(side="right")
        self.frame_down.pack(anchor="n", padx=15)        
        
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
        """
        This method toggles the power state using the method in the Television object,
        then calls the updateLabel() method to change the status displayed in the GUI
        """
        self.my_tv.power()
        self.updateLabel()
    
    def volumeUpClicked(self):
        """
        This method increases the volume using the method in the Television object,
        then calls the updateLabel() method to change the status displayed in the GUI
        """
        self.my_tv.volume_up()
        self.updateLabel()

    def volumeDownClicked(self):
        """
        This method decreases the volume using the method in the Television object,
        then calls the updateLabel() method to change the status displayed in the GUI
        """
        self.my_tv.volume_down()
        self.updateLabel()

    def channelUpClicked(self):
        """
        This method increases the channel using the method in the Television object,
        then calls the updateLabel() method to change the status displayed in the GUI
        """
        self.my_tv.channel_up()
        self.updateLabel()

    def channelDownClicked(self):
        """
        This method decreases the channel using the method in the Television object,
        then calls the updateLabel() method to change the status displayed in the GUI
        """
        self.my_tv.channel_down()
        self.updateLabel()

    def updateLabel(self):
        """
        This method updates the labels for the power status, channel, and volume
        It will "hide" the volume and channel text boxes when the TV is off
        """
        if self.my_tv.get_status()[0] == 1:
            self.powerButton.configure(bg="green")
            self.label_status.configure(text="On")
            self.label_status2.configure(text="Channel = " + str(self.my_tv.get_status()[1]))
            self.label_status3.configure(text="Volume = " + str(self.my_tv.get_status()[2]))
            channel = self.my_tv.get_status()[1]
            
            # volume graphic
            volume = self.my_tv.get_status()[2]
            if volume == 0:
                self.volumeStatus.configure(text="[----------]")
            elif volume == 1:
                self.volumeStatus.configure(text="[x---------]")
            elif volume == 2:
                self.volumeStatus.configure(text="[xx--------]")
            elif volume == 3:
                self.volumeStatus.configure(text="[xxx-------]")
            elif volume == 4:
                self.volumeStatus.configure(text="[xxxx------]")
            elif volume == 5:
                self.volumeStatus.configure(text="[xxxxx-----]")
            elif volume == 6:
                self.volumeStatus.configure(text="[xxxxxx----]")
            elif volume == 7:
                self.volumeStatus.configure(text="[xxxxxxx---]")
            elif volume == 8:
                self.volumeStatus.configure(text="[xxxxxxxx--]")
            elif volume == 9:
                self.volumeStatus.configure(text="[xxxxxxxxx-]")
            elif volume == 10:
                self.volumeStatus.configure(text="[xxxxxxxxxx]")

            # image changer
            if channel < 10 and channel >= 0:
                self.img = ImageTk.PhotoImage(Image.open("./channelImages/tile00"+str(self.my_tv.get_status()[1])+".png"))
            elif channel < 100 and channel >= 10:
                self.img = ImageTk.PhotoImage(Image.open("./channelImages/tile0"+str(self.my_tv.get_status()[1])+".png"))
            else:
                self.img = ImageTk.PhotoImage(Image.open("./channelImages/blank.png"))
            self.imageLabel.configure(image=self.img)
        
        else:
            self.powerButton.configure(bg="red")
            self.label_status.configure(text="Off")
            self.label_status2.configure(text="")
            self.label_status3.configure(text="")
            self.img = ImageTk.PhotoImage(Image.open("./channelImages/blank.png"))
            self.imageLabel.configure(image=self.img)
            self.volumeStatus.configure(text="[----------]")