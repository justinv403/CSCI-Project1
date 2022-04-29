from gui import *

def main():
    """
    Main function for the program - launches the GUI contained in gui.py
    """
    window = Tk()
    window.title("TV Remote")
    window.geometry("300x700")
    window.resizable(False,False)
    window.mainloop()


if __name__ == "__main__":
    main()