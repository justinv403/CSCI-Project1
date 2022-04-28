from gui import *

def main():
    """
    - Change the window title to 'TV Remote'.
    - Set its length to 300 and height to 600.
    - Make the window non-resizable.
    """
    window = Tk()
    widgets = GUI(window)
    window.title("TV Remote")
    window.geometry("300x600")
    window.resizable(False,False)
    window.mainloop()


if __name__ == "__main__":
    main()