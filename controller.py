from PyQt5.QtWidgets import *
from gui import Ui_MainWindow
from classes import *
import csv

class Controller(QMainWindow, Ui_MainWindow):
    def __init__(self, TV, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)

        
        def save(self):
            TV.channel_down