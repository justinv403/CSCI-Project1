from PyQt5.QtWidgets import *
from view import Ui_Remote
import csv

class Controller(QMainWindow, Ui_Remote):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)

        self.volumeDownButton.clicked(lambda : self.volumeDown())

    def volumeDown(self):
        self.volumeDownButton.setText("Test")