from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("TV Remote")

img = ImageTk.PhotoImage(Image.open("./channelImages/tile000.png"))
imageLabel = Label(image=img)
imageLabel.pack()

root.mainloop()