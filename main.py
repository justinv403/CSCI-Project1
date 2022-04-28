# this is the main program file for the tv remote w/ gui

from controller import *

def main():
    my_TV = Television()
    
    app = QApplication([])
    window = Controller(my_TV)
    window.show()
    app.exec_()

if __name__ == "__main__":
    main()