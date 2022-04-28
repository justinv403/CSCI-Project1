from PyQt5.QtWidgets import *
from gui import Ui_MainWindow
import csv

class Controller(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)


        def save(self):
            