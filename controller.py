from PyQt5.QtWidgets import *
from gui import Ui_MainWindow

class Controller(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)

        
        self.volumeDownButton.clicked(lambda : self.volumeDown())

    def volumeDown(self):
        self.volumeDownButton.setText("Test")