"""
FileManager for file selection and validation
"""
from PySide6.QtWidgets import QFileDialog, QMessageBox, QWidget
import os


class FileManager:
    @staticmethod
    def select_json_file(parent: QWidget) -> str:
        """Show file dialog to select JSON file"""
        file_path, _ = QFileDialog.getOpenFileName(
            parent,
            "Select JSON Question File",
            "",
            "JSON Files (*.json);;All Files (*)"
        )
        return file_path

    @staticmethod
    def validate_file(file_path: str) -> bool:
        """Validate that the selected file is valid"""
        if not file_path:
            return False

        if not os.path.exists(file_path):
            return False

        if not os.path.isfile(file_path):
            return False

        if not file_path.lower().endswith('.json'):
            return False

        # Check file size (limit to 10MB for safety)
        try:
            file_size = os.path.getsize(file_path)
            if file_size > 10 * 1024 * 1024:  # 10MB
                return False
        except OSError:
            return False

        return True

    @staticmethod
    def show_error(parent: QWidget, message: str, title: str = "File Error"):
        """Show error dialog with recovery suggestions"""
        # Add helpful suggestions based on error type
        detailed_message = message

        if "not found" in message.lower():
            detailed_message += "\n\nSuggestions:\n• Check if the file path is correct\n• Ensure the file hasn't been moved or deleted"
        elif "json" in message.lower() and "format" in message.lower():
            detailed_message += "\n\nSuggestions:\n• Check if the file is valid JSON\n• Try opening the file in a text editor to verify format\n• Ensure the file contains a list of question-answer pairs"
        elif "encoding" in message.lower():
            detailed_message += "\n\nSuggestions:\n• Save the file with UTF-8 encoding\n• Try opening the file in a text editor and re-saving with UTF-8"
        elif "empty" in message.lower():
            detailed_message += "\n\nSuggestions:\n• Add some question-answer pairs to the file\n• Check the sample-input.json file for format reference"

        msg_box = QMessageBox(parent)
        msg_box.setIcon(QMessageBox.Icon.Critical)
        msg_box.setWindowTitle(title)
        msg_box.setText(message)
        msg_box.setDetailedText(detailed_message)
        msg_box.exec()

    @staticmethod
    def show_info(parent: QWidget, message: str, title: str = "Information"):
        """Show information dialog"""
        QMessageBox.information(parent, title, message)

    @staticmethod
    def get_file_name(file_path: str) -> str:
        """Get just the filename from a full path"""
        if not file_path:
            return ""
        return os.path.basename(file_path)
