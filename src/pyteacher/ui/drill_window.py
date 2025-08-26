"""
DrillWindow for Strict Dictionary Drill mode
"""
from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QHBoxLayout, QMessageBox
from PySide6.QtCore import Qt, QTimer
from PySide6.QtGui import QKeyEvent
from pyteacher.utils.window_manager import window_manager
import os


class DrillWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Strict Dictionary Drill")
        self.setGeometry(150, 150, 500, 400)
        self.controller = None
        self.questions = []
        self.file_name = None
        self.feedback_timer = QTimer()
        self.feedback_timer.timeout.connect(self._clear_feedback)
        self.feedback_timer.setSingleShot(True)
        self._init_ui()

    def _init_ui(self):
        from pyteacher.utils.data_loader import DataLoader
        from pyteacher.controllers.drill_controller import DrillController
        from pyteacher.utils.file_manager import FileManager

        layout = QVBoxLayout()

        # Mode and file info
        self.mode_label = QLabel("Mode: LEARN")
        self.mode_label.setStyleSheet("font-weight: bold; font-size: 14px;")
        self.file_label = QLabel("File: <not loaded>")
        self.file_label.setStyleSheet("color: #666;")

        # Statistics
        stats_layout = QHBoxLayout()
        self.total_label = QLabel("Total: 0")
        self.learned_label = QLabel("Learned: 0")
        self.left_label = QLabel("Left: 0")
        stats_layout.addWidget(self.total_label)
        stats_layout.addWidget(self.learned_label)
        stats_layout.addWidget(self.left_label)

        # Instructions
        instruction_label = QLabel("Press ESC to exit")
        instruction_label.setStyleSheet("color: #888; font-style: italic;")

        # Load button
        load_btn = QPushButton("Load Questions File")
        load_btn.setStyleSheet("QPushButton { padding: 8px; }")

        # Question and answer interface
        question_label = QLabel("Question:")
        question_label.setStyleSheet("font-weight: bold;")
        self.question_edit = QLineEdit()
        self.question_edit.setReadOnly(True)
        self.question_edit.setStyleSheet("QLineEdit { background-color: #f5f5f5; padding: 8px; font-size: 12px; }")

        answer_label = QLabel("Answer:")
        answer_label.setStyleSheet("font-weight: bold;")
        self.answer_edit = QLineEdit()
        self.answer_edit.setStyleSheet("QLineEdit { padding: 8px; font-size: 12px; }")

        # Feedback label for showing correct answer
        self.feedback_label = QLabel("")
        self.feedback_label.setStyleSheet("color: #d32f2f; font-weight: bold; margin: 5px;")
        self.feedback_label.hide()

        # Layout assembly
        layout.addWidget(self.mode_label)
        layout.addWidget(self.file_label)
        layout.addLayout(stats_layout)
        layout.addWidget(instruction_label)
        layout.addWidget(load_btn)
        layout.addSpacing(10)
        layout.addWidget(question_label)
        layout.addWidget(self.question_edit)
        layout.addWidget(answer_label)
        layout.addWidget(self.answer_edit)
        layout.addWidget(self.feedback_label)
        layout.addStretch()

        self.setLayout(layout)

        # Connect events
        def load_file():
            file_path = FileManager.select_json_file(self)
            if not FileManager.validate_file(file_path):
                if file_path:  # Only show error if user actually selected a file
                    FileManager.show_error(self, "Invalid file selected.")
                return
            try:
                data = DataLoader.load_json_file(file_path)
                self.questions = data
                self.file_name = FileManager.get_file_name(file_path)
                self.file_label.setText(f"File: {self.file_name}")
                self.controller = DrillController(self.questions)
                self.controller.start_drill()
                self._update_ui()
                load_btn.hide()  # Hide load button after successful load
                self.answer_edit.setFocus()
            except ValueError as e:
                FileManager.show_error(self, str(e))
            except Exception as e:
                FileManager.show_error(self, f"Unexpected error loading file: {e}")

        def submit_answer():
            if not self.controller or self.controller.current_idx is None:
                return

            user_input = self.answer_edit.text()
            if not user_input.strip():
                return

            correct = self.controller.check_answer(user_input)
            self._show_feedback(correct)

            # Move to next question after brief delay
            QTimer.singleShot(200, self._proceed_to_next)

        load_btn.clicked.connect(load_file)
        self.answer_edit.returnPressed.connect(submit_answer)

    def _show_feedback(self, correct: bool):
        """Show visual feedback for answer"""
        if correct:
            self.answer_edit.setStyleSheet("""
                QLineEdit {
                    background-color: #c8e6c9;
                    border: 2px solid #4caf50;
                    padding: 8px;
                    font-size: 12px;
                }
            """)
            self.feedback_label.hide()
        else:
            self.answer_edit.setStyleSheet("""
                QLineEdit {
                    background-color: #ffcdd2;
                    border: 2px solid #f44336;
                    padding: 8px;
                    font-size: 12px;
                }
            """)
            # Show correct answer
            if self.controller:
                correct_answer = self.controller.get_current_correct_answer()
                self.feedback_label.setText(f"Correct answer: {correct_answer}")
                self.feedback_label.show()

        # Start timer to clear feedback
        self.feedback_timer.start(2500)  # 2.5 seconds

    def _clear_feedback(self):
        """Clear visual feedback"""
        self.answer_edit.setStyleSheet("QLineEdit { padding: 8px; font-size: 12px; }")
        self.feedback_label.hide()

    def _proceed_to_next(self):
        """Move to next question"""
        if not self.controller:
            return

        self.controller.next_question()
        self.answer_edit.clear()
        self._update_ui()

        # Check if session is complete
        stats = self.controller.update_statistics()
        if stats['left'] == 0:
            self._show_results(stats)
        else:
            # Ensure focus is on answer input
            self.answer_edit.setFocus()

    def _update_ui(self):
        """Update UI elements with current state"""
        if self.controller and self.controller.current_idx is not None:
            stats = self.controller.update_statistics()
            self.total_label.setText(f"Total: {stats['total']}")
            self.learned_label.setText(f"Learned: {stats['learned']}")
            self.left_label.setText(f"Left: {stats['left']}")

            question = self.controller.session.questions[self.controller.current_idx]
            self.question_edit.setText(question.question)
            self.answer_edit.setFocus()
        else:
            self.question_edit.setText("")

    def _show_results(self, stats):
        """Show results window when drill is complete"""
        from pyteacher.ui.results_window import ResultsWindow
        from pyteacher.utils.statistics import StatisticsCalculator

        results = ResultsWindow(self)
        perf = StatisticsCalculator.generate_performance_report(stats)
        results.set_results({**stats, 'accuracy': perf['accuracy']})
        results.exec()

    def keyPressEvent(self, event: QKeyEvent):
        """Handle key press events"""
        if event.key() == Qt.Key.Key_Escape:
            self._return_to_main_menu()
        else:
            super().keyPressEvent(event)

    def _return_to_main_menu(self):
        """Return to main menu and cleanup"""
        # Stop any running timers
        if self.feedback_timer.isActive():
            self.feedback_timer.stop()

        # Close this window and return to main menu
        self.close()
        window_manager.close_window('drill')
        window_manager.show_main_window()

    def closeEvent(self, event):
        """Handle window close event"""
        if self.feedback_timer.isActive():
            self.feedback_timer.stop()
        super().closeEvent(event)
