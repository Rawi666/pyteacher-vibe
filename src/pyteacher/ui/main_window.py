"""
MainWindow for Language Learning App (PySide6)
"""
from PySide6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QLabel, QPushButton
from PySide6.QtCore import Qt
from pyteacher.utils.window_manager import window_manager
from .styles import WINDOW_STYLE, TITLE_LABEL_STYLE, MAIN_BUTTON_STYLE

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Language Learning App")
        self.setGeometry(100, 100, 400, 300)
        self.drill_window = None
        self.test_window = None
        self.setStyleSheet(WINDOW_STYLE)
        self._init_ui()

    def _init_ui(self):
        from pyteacher.ui.drill_window import DrillWindow
        from pyteacher.ui.test_window import TestWindow
        central_widget = QWidget()
        layout = QVBoxLayout()

        # Add some spacing at the top
        layout.addSpacing(30)

        title_label = QLabel("Language Learning App")
        title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title_label.setStyleSheet(TITLE_LABEL_STYLE)
        layout.addWidget(title_label)

        # Add spacing between title and buttons
        layout.addSpacing(30)

        drill_btn = QPushButton("Strict Dictionary Drill")
        drill_btn.setStyleSheet(MAIN_BUTTON_STYLE)
        test_btn = QPushButton("Strict Dictionary Test")
        test_btn.setStyleSheet(MAIN_BUTTON_STYLE)

        layout.addWidget(drill_btn)
        layout.addSpacing(10)
        layout.addWidget(test_btn)

        # Add stretch to center the content
        layout.addStretch()

        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        # Navigation logic
        def open_drill():
            if self.drill_window:
                self.drill_window.close()
            self.drill_window = DrillWindow()
            window_manager.register_window('drill', self.drill_window)
            self.drill_window.show()

        def open_test():
            if self.test_window:
                self.test_window.close()
            self.test_window = TestWindow()
            window_manager.register_window('test', self.test_window)
            self.test_window.show()

        drill_btn.clicked.connect(open_drill)
        test_btn.clicked.connect(open_test)
