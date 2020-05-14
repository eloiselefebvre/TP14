from PySide2.QtWidgets import QProgressBar, QLineEdit, QVBoxLayout, QLabel, QWidget, QFileIconProvider, QPushButton, QApplication, QTextEdit

class HelloWorld(QWidget):

    def __init__(self):
        QWidget.__init__(self)

        mainWidget = QWidget()
        mainWidget.setFixedSize(400,300)
        mainWidget.setWindowTitle('IHM')
        mainWidget.setWindowIcon(self.icon)

        self.icon = QFileIconProvider('https://drive.google.com/file/d/1rRc9g8vKTRm5GZGAh68T0Izv2kwM2A7l/view')

        self.layout = QVBoxLayout()

        self.label = QLabel('Hello World')
        self.label.setAlignment(Qt.AlignCenter)

        self.bar = QProgressBar()
        self.bar.setValue(50)

        self.linedit = QLineEdit

        self.button = QPushButton()
        self.button.setToolTip('Welcome !')

        self.layout.addWidget(self.icon)
        self.layout.addWidget(self.label)
        self.layout.addWidget(self.bar)
        self.layout.addWidget(self.linedit)
        self.layout.addWidget(self.button)

        self.setLayout(self.layout)

if __name__ == '__main__' :
    app = QApplication([])
    hw = HelloWorld()
    hw.show()
    app.exec_()









