"""
Application entry point for Language Learning App (PySide6)
"""
import sys
from PySide6.QtWidgets import QApplication
from pyteacher.ui.main_window import MainWindow
from pyteacher.utils.window_manager import window_manager

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window_manager.set_main_window(window)
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
