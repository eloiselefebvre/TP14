from PySide2.QtWidgets import QLabel, QWidget, QPushButton, QApplication, QGridLayout, QTextEdit

class Com(QWidget):

    def __init__(self):
        QWidget.__init__(self)

        mainWidget = QWidget()
        mainWidget.setWindowTitle('IHM')

        self.layout = QGridLayout()

        self.label=QLabel('Rédigez un comentaire')

        self.label2=QTextEdit()

        self.button = QPushButton('success')
        self.button2 = QPushButton('cancel')

        self.layout.addWidget(self.label)
        self.layout.addWidget(self.label2)
        self.layout.addWidget(self.button)
        self.layout.addWidget(self.button2)

        self.setLayout(self.layout)

if __name__=='__main__' :
    app = QApplication([])
    com = Com()
    com.show()
    app.exec_()

