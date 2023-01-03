import sys

from PyQt6.QtWidgets import QApplication

from VTSoundUI import VTSoundUI

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = VTSoundUI()
    window.setWindowTitle("VTSound")
    window.resize(640, 480)
    window.show()
    sys.exit(app.exec())
