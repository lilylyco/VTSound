import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QListWidget, QInputDialog, QListWidgetItem,
                             QComboBox, QSlider, QFileDialog, QLineEdit)


class VTSoundUI(QWidget):
    def __init__(self):
        super().__init__()
        self.listWidget = None
        self.initUI()

    def initUI(self):
        self.listWidget = QListWidget()
        addButton = QPushButton('Add')
        removeButton = QPushButton('Remove')

        hbox = QHBoxLayout()
        hbox.addWidget(addButton)
        hbox.addWidget(removeButton)

        vbox = QVBoxLayout()
        vbox.addWidget(self.listWidget)
        vbox.addLayout(hbox)

        self.setLayout(vbox)

        addButton.clicked.connect(self.addItem)
        removeButton.clicked.connect(self.removeItem)

    def addItem(self):
        item = QListWidgetItem()
        paramDropdown = QComboBox()
        paramDropdown.addItems(['Option 1', 'Option 2', 'Option 3'])
        comparatorDropdown = QComboBox()
        comparatorDropdown.addItems(['>', '<', '==', '>=', '<='])
        slider = QSlider(Qt.Orientation.Horizontal)
        sliderValue = QLineEdit()
        sliderValue.setText(str(slider.value()))
        self.slider = slider
        self.sliderValue = sliderValue
        uploadButton = QPushButton('Choose file')
        playButton = QPushButton('Play')
        stopButton = QPushButton('Stop')

        hbox = QHBoxLayout()
        hbox.addWidget(paramDropdown)
        hbox.addWidget(comparatorDropdown)
        hbox.addWidget(slider)
        hbox.addWidget(sliderValue)
        hbox.addWidget(uploadButton)
        hbox.addWidget(playButton)
        hbox.addWidget(stopButton)

        widget = QWidget()
        widget.setLayout(hbox)

        item.setSizeHint(widget.sizeHint())
        self.listWidget.addItem(item)
        self.listWidget.addItem(item)
        self.listWidget.setItemWidget(item, widget)

        slider.valueChanged.connect(self.updateLineEdit)
        sliderValue.editingFinished.connect(self.updateSlider)
        uploadButton.clicked.connect(self.openFileDialog)

    def updateLineEdit(self):
        self.sliderValue.setText(str(self.slider.value()))

    def updateSlider(self):
        self.slider.setValue(int(self.sliderValue.text()))

    def openFileDialog(self):
        fileName, _ = QFileDialog.getOpenFileName(self, 'Open file', '', '', options=QFileDialog.Option.ReadOnly)
        if fileName:
            print(fileName)

    def removeItem(self):
        for item in self.listWidget.selectedItems():
            self.listWidget.takeItem(self.listWidget.row(item))
