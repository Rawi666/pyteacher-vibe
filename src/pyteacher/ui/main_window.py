"""
MainWindow for Language Learning App (PySide6)
"""
from PySide6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QLabel, QPushButton
from PySide6.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Language Learning App")
        self.setGeometry(100, 100, 400, 300)
        self.drill_window = None
        self.test_window = None
        self._init_ui()

    def _init_ui(self):
        from pyteacher.ui.drill_window import DrillWindow
        from pyteacher.ui.test_window import TestWindow
        central_widget = QWidget()
        layout = QVBoxLayout()
        title_label = QLabel("Language Learning App")
        title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(title_label)
        drill_btn = QPushButton("Strict Dictionary Drill")
        test_btn = QPushButton("Strict Dictionary Test")
        layout.addWidget(drill_btn)
        layout.addWidget(test_btn)
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        # Navigation logic
        def open_drill():
            self.drill_window = DrillWindow()
            self.drill_window.show()

        def open_test():
            self.test_window = TestWindow()
            self.test_window.show()

        drill_btn.clicked.connect(open_drill)
        test_btn.clicked.connect(open_test)
