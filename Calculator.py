import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QGroupBox, QDialog, QVBoxLayout, QGridLayout,QMainWindow, QApplication, QWidget, QPushButton, QAction, QLineEdit, QMessageBox
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot

class App(QDialog):

    def __init__(self):
        super().__init__()
        self.title = 'Calculator'
        self.left = 10
        self.top = 10
        self.width = 640
        self.height = 480
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.createGridLayout()
        
        windowLayout = QVBoxLayout()
        windowLayout.addWidget(self.horizontalGroupBox)
        self.setLayout(windowLayout)

        self.textbox = QLineEdit(self)
        self.textbox.move(20, 40)
        self.textbox.resize(600,35)

        # Original Approach
        # buttonp = QPushButton('+', self)
        # buttonp.setToolTip('Addition Operator')
        # buttonp.move(100,70)
        # buttonp.clicked.connect(self.on_click)
        
        # buttonm = QPushButton('-', self)
        # buttonm.setToolTip('Subtraction Operator')
        # buttonm.move(100,100)
        # buttonm.clicked.connect(self.on_click)
        self.show()
    def createGridLayout(self):
        self.horizontalGroupBox = QGroupBox("Grid")
        layout = QGridLayout()
        # layout.setColumnStretch(1, 2)
        # layout.setColumnStretch(2, 4)
        
        layout.addWidget(QPushButton('1'),0,0)
        layout.addWidget(QPushButton('2'),0,1)
        layout.addWidget(QPushButton('3'),0,2)
        layout.addWidget(QPushButton('4'),1,0)
        layout.addWidget(QPushButton('5'),1,1)
        layout.addWidget(QPushButton('6'),1,2)
        layout.addWidget(QPushButton('7'),2,0)
        layout.addWidget(QPushButton('8'),2,1)
        layout.addWidget(QPushButton('9'),2,2)
        layout.addWidget(QPushButton('0'),3,1)
        layout.addWidget(QPushButton('.'),3,0)
        layout.addWidget(QPushButton('='),3,2)
        layout.addWidget(QPushButton('+'),0,4)
        layout.addWidget(QPushButton('-'),1,4)
        layout.addWidget(QPushButton('*'),2,4)
        layout.addWidget(QPushButton('/'),3,4)

        self.horizontalGroupBox.setLayout(layout)

    # @pyqtSlot()
    # def on_click(self):
    #     print('Button click')

    @pyqtSlot()
    def on_click(self):
        textboxValue = "Good"
        QMessageBox.question(self, 'Message - pythonspot.com', "You typed: " + textboxValue, QMessageBox.Ok, QMessageBox.Ok)
        self.textbox.setText("Good")
    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())