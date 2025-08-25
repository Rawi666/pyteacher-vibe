"""
FileManager for file selection and validation
"""
from PySide6.QtWidgets import QFileDialog, QMessageBox, QWidget
import os

class FileManager:
    @staticmethod
    def select_json_file(parent: QWidget) -> str:
        file_path, _ = QFileDialog.getOpenFileName(parent, "Select JSON File", "", "JSON Files (*.json)")
        return file_path

    @staticmethod
    def validate_file(file_path: str) -> bool:
        if not file_path or not os.path.isfile(file_path):
            return False
        if not file_path.lower().endswith('.json'):
            return False
        return True

    @staticmethod
    def show_error(parent: QWidget, message: str):
        QMessageBox.critical(parent, "File Error", message)
