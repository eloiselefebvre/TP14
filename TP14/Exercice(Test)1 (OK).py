from PySide2.QtWidgets import QLabel, QWidget, QPushButton, QApplication, QVBoxLayout
app = QApplication([])
mainWidget = QWidget()


layout = QVBoxLayout()


label = QLabel("Ceci est un QLabel")
button = QPushButton("Ceci est un QPushButton")


layout.addWidget(label)
layout.addWidget(button)


mainWidget.setLayout(layout)



mainWidget.show()
app.exec_()
