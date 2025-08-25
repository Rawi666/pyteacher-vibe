"""
Application entry point for Language Learning App (PySide6)
"""
import sys
from PySide6.QtWidgets import QApplication
from pyteacher.ui.main_window import MainWindow

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
