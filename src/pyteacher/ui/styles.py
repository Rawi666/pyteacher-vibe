"""
UI Style constants for the language learning application
"""

# Text input styles
TEXTBOX_STYLE = "QLineEdit { background-color: #2b2b2b; color: #ffffff; padding: 8px; font-size: 12px; border: 1px solid #555; }"

# Feedback styles for correct/incorrect answers
CORRECT_FEEDBACK_STYLE = """
QLineEdit {
    background-color: #1b5e20;
    color: #ffffff;
    border: 2px solid #4caf50;
    padding: 8px;
    font-size: 12px;
}
"""

INCORRECT_FEEDBACK_STYLE = """
QLineEdit {
    background-color: #b71c1c;
    color: #ffffff;
    border: 2px solid #f44336;
    padding: 8px;
    font-size: 12px;
}
"""

# Label styles
BOLD_LABEL_STYLE = "font-weight: bold;"
FEEDBACK_LABEL_STYLE = "color: #d32f2f; font-weight: bold; margin: 5px;"
INSTRUCTION_LABEL_STYLE = "color: #888; font-style: italic;"
MODE_LABEL_STYLE = "font-weight: bold; font-size: 14px;"
FILE_LABEL_STYLE = "color: #666;"

# Button styles
BUTTON_STYLE = "QPushButton { padding: 8px; }"
