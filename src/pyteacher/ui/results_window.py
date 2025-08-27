"""
ResultsWindow for session summary
"""
from PySide6.QtWidgets import QDialog, QVBoxLayout, QLabel, QPushButton, QProgressBar, QHBoxLayout
from PySide6.QtCore import Qt
from pyteacher.utils.window_manager import window_manager
from .styles import (WINDOW_STYLE, RESULTS_TITLE_STYLE, RESULTS_STATS_STYLE,
                     RESULTS_ACCURACY_STYLE, BUTTON_STYLE, COLORS)


class ResultsWindow(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Session Results")
        self.setGeometry(200, 200, 450, 300)
        self.setModal(True)
        self.setStyleSheet(WINDOW_STYLE)
        self._init_ui()

    def set_results(self, stats: dict):
        """Set the results to display"""
        total = stats.get('total', 0)
        correct = stats.get('learned', 0)

        self.total_label.setText(f"Total Questions: {total}")
        self.correct_label.setText(f"Correct Answers: {correct}")

        accuracy = stats.get('accuracy', '0%')
        if isinstance(accuracy, str) and accuracy.endswith('%'):
            accuracy_value = float(accuracy.rstrip('%'))
        else:
            accuracy_value = float(accuracy) if accuracy else 0
            accuracy = f"{accuracy_value:.1f}%"

        self.accuracy_label.setText(f"Accuracy: {accuracy}")
        self.progress_bar.setValue(int(accuracy_value))

        # Add motivational message
        if accuracy_value >= 90:
            message = "🎉 Excellent work! Outstanding performance!"
        elif accuracy_value >= 75:
            message = "👍 Great job! Keep up the good work!"
        elif accuracy_value >= 60:
            message = "👌 Good effort! Practice makes perfect!"
        else:
            message = "💪 Keep practicing! You'll improve with time!"

        self.motivation_label.setText(message)
        self.motivation_label.setStyleSheet(f"color: {COLORS['accent_primary']}; font-weight: bold; margin: 10px;")

    def _init_ui(self):
        """Initialize the UI components"""
        layout = QVBoxLayout()

        # Title
        title_label = QLabel("Session Statistics")
        title_label.setStyleSheet(RESULTS_TITLE_STYLE)
        title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Statistics
        self.total_label = QLabel("Total Questions: 0")
        self.total_label.setStyleSheet(RESULTS_STATS_STYLE)

        self.correct_label = QLabel("Correct Answers: 0")
        self.correct_label.setStyleSheet(RESULTS_STATS_STYLE)

        self.accuracy_label = QLabel("Accuracy: 0%")
        self.accuracy_label.setStyleSheet(RESULTS_ACCURACY_STYLE)

        # Progress bar
        self.progress_bar = QProgressBar()
        self.progress_bar.setRange(0, 100)
        self.progress_bar.setValue(0)
        self.progress_bar.setStyleSheet(f"""
            QProgressBar {{
                background-color: {COLORS['background_secondary']};
                border: 1px solid {COLORS['border_default']};
                border-radius: 4px;
                text-align: center;
                height: 25px;
                margin: 5px;
                color: {COLORS['text_primary']};
            }}
            QProgressBar::chunk {{
                background-color: {COLORS['accent_success']};
                border-radius: 3px;
            }}
        """)

        # Motivational message
        self.motivation_label = QLabel("")
        self.motivation_label.setStyleSheet(f"color: {COLORS['accent_primary']}; font-weight: bold; margin: 10px;")
        self.motivation_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.motivation_label.setWordWrap(True)

        # Buttons
        button_layout = QHBoxLayout()

        close_btn = QPushButton("Close")
        close_btn.setStyleSheet(BUTTON_STYLE)
        close_btn.setDefault(True)

        button_layout.addWidget(close_btn)

        # Add all widgets to main layout
        layout.addWidget(title_label)
        layout.addSpacing(10)
        layout.addWidget(self.total_label)
        layout.addWidget(self.correct_label)
        layout.addWidget(self.accuracy_label)
        layout.addWidget(self.progress_bar)
        layout.addWidget(self.motivation_label)
        layout.addStretch()
        layout.addLayout(button_layout)

        self.setLayout(layout)

        # Connect button events
        def close_all():
            """Close both results window and parent drill/test window, return to main menu"""
            self.accept()  # Close results window
            # Use window manager to properly close all windows and return to main menu
            window_manager.close_all_except_main()

        close_btn.clicked.connect(close_all)
