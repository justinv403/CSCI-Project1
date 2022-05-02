from gui import *

def main():
    """
    Main function for the program - launches the GUI contained in gui.py
    """
    window = Tk()
    widgets = GUI(window)
    window.title("TV Remote")
    window.geometry("300x700")
    window.resizable(False,False)
    window.mainloop()


if __name__ == "__main__":
    main()

# NOTE:
# image for channel?
# volume bar?