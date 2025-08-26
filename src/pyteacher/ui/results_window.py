"""
ResultsWindow for session summary
"""
from PySide6.QtWidgets import QDialog, QVBoxLayout, QLabel, QPushButton, QProgressBar
from PySide6.QtCore import Qt

class ResultsWindow(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Session Results")
        self.setGeometry(200, 200, 400, 250)
        self._init_ui()

    def set_results(self, stats: dict):
        self.total_label.setText(f"Total Questions: {stats.get('total', 0)}")
        self.correct_label.setText(f"Correct Answers: {stats.get('learned', 0)}")
        accuracy = stats.get('accuracy', '0%')
        self.accuracy_label.setText(f"Accuracy: {accuracy}")
        self.progress_bar.setValue(int(float(accuracy.strip('%'))))

    def _init_ui(self):
        layout = QVBoxLayout()
        self.stats_label = QLabel("Session Statistics:")
        self.total_label = QLabel("Total Questions: 0")
        self.correct_label = QLabel("Correct Answers: 0")
        self.accuracy_label = QLabel("Accuracy: 0%")
        self.progress_bar = QProgressBar()
        self.progress_bar.setValue(0)
        close_btn = QPushButton("Close")
        new_session_btn = QPushButton("New Session")
        layout.addWidget(self.stats_label)
        layout.addWidget(self.total_label)
        layout.addWidget(self.correct_label)
        layout.addWidget(self.accuracy_label)
        layout.addWidget(self.progress_bar)
        layout.addWidget(close_btn)
        layout.addWidget(new_session_btn)
        self.setLayout(layout)

        def close_all():
            # Close both the results window and the parent drill/test window
            if self.parent() is not None:
                self.parent().close()
            self.close()
        close_btn.clicked.connect(close_all)
