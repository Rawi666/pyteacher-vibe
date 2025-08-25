"""
DrillWindow for Strict Dictionary Drill mode
"""
from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QHBoxLayout
from PySide6.QtCore import Qt

class DrillWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Strict Dictionary Drill")
        self.setGeometry(150, 150, 500, 300)
        self.controller = None
        self.questions = []
        self.file_name = None
        self._init_ui()

    def _init_ui(self):
        from pyteacher.utils.data_loader import DataLoader
        from pyteacher.controllers.drill_controller import DrillController
        from pyteacher.utils.file_manager import FileManager

        layout = QVBoxLayout()
        self.mode_label = QLabel("Mode: LEARN")
        self.file_label = QLabel("File: <not loaded>")
        stats_layout = QHBoxLayout()
        self.total_label = QLabel("Total: 0")
        self.learned_label = QLabel("Learned: 0")
        self.left_label = QLabel("Left: 0")
        stats_layout.addWidget(self.total_label)
        stats_layout.addWidget(self.learned_label)
        stats_layout.addWidget(self.left_label)
        instruction_label = QLabel("Press ESC to exit")
        question_label = QLabel("Question:")
        self.question_edit = QLineEdit()
        self.question_edit.setReadOnly(True)
        answer_label = QLabel("Answer:")
        self.answer_edit = QLineEdit()
        load_btn = QPushButton("Load Questions File")
        layout.addWidget(self.mode_label)
        layout.addWidget(self.file_label)
        layout.addLayout(stats_layout)
        layout.addWidget(instruction_label)
        layout.addWidget(load_btn)
        layout.addWidget(question_label)
        layout.addWidget(self.question_edit)
        layout.addWidget(answer_label)
        layout.addWidget(self.answer_edit)
        self.setLayout(layout)

        def load_file():
            file_path = FileManager.select_json_file(self)
            if not FileManager.validate_file(file_path):
                FileManager.show_error(self, "Invalid file selected.")
                return
            try:
                data = DataLoader.load_json_file(file_path)
                if not DataLoader.validate_json_structure([q.__dict__ for q in data]):
                    FileManager.show_error(self, "File format invalid.")
                    return
                self.questions = data
                self.file_name = file_path.split("/")[-1]
                self.file_label.setText(f"File: {self.file_name}")
                self.controller = DrillController(self.questions)
                self.controller.start_drill()
                self.update_ui()
            except Exception as e:
                FileManager.show_error(self, f"Error loading file: {e}")

        def submit_answer():
            if not self.controller or self.controller.current_idx is None:
                return
            user_input = self.answer_edit.text()
            correct = self.controller.check_answer(user_input)
            self.update_ui()
            if correct:
                self.answer_edit.setStyleSheet("background-color: lightgreen;")
            else:
                self.answer_edit.setStyleSheet("background-color: pink;")
            self.answer_edit.clear()
            self.controller.next_question()
            self.update_ui()
            # Show results if session is complete
            stats = self.controller.update_statistics()
            if stats['left'] == 0:
                from pyteacher.ui.results_window import ResultsWindow
                from pyteacher.utils.statistics import StatisticsCalculator
                results = ResultsWindow()
                perf = StatisticsCalculator.generate_performance_report(stats)
                results.set_results({**stats, 'accuracy': perf['accuracy']})
                results.exec()

        load_btn.clicked.connect(load_file)
        self.answer_edit.returnPressed.connect(submit_answer)

    def update_ui(self):
        if self.controller and self.controller.current_idx is not None:
            stats = self.controller.update_statistics()
            self.total_label.setText(f"Total: {stats['total']}")
            self.learned_label.setText(f"Learned: {stats['learned']}")
            self.left_label.setText(f"Left: {stats['left']}")
            q = self.controller.session.questions[self.controller.current_idx]
            self.question_edit.setText(q.question)
            self.answer_edit.setFocus()
        else:
            self.question_edit.setText("")
