"""
UI Style constants for the language learning application
Modern dark theme that ensures consistent appearance regardless of OS theme
"""

# Color Palette for Dark Mode
COLORS = {
    'background_primary': '#1e1e1e',    # Main window background
    'background_secondary': '#2d2d2d',  # Secondary backgrounds
    'background_input': '#3d3d3d',      # Input fields background
    'text_primary': '#ffffff',          # Primary text color
    'text_secondary': '#b0b0b0',        # Secondary text color
    'text_muted': '#808080',            # Muted/disabled text
    'accent_primary': '#007acc',        # Primary accent color
    'accent_success': '#4caf50',        # Success/correct feedback
    'accent_error': '#f44336',          # Error/incorrect feedback
    'border_default': '#555555',        # Default border color
    'border_focus': '#007acc',          # Focused element border
    'hover_overlay': '#404040',         # Hover state overlay
}

# Application-wide dark theme stylesheet
APPLICATION_STYLE = f"""
QMainWindow, QWidget {{
    background-color: {COLORS['background_primary']};
    color: {COLORS['text_primary']};
    font-family: 'Segoe UI', system-ui, sans-serif;
    font-size: 12px;
}}

QLabel {{
    color: {COLORS['text_primary']};
    background: transparent;
}}

QPushButton {{
    background-color: {COLORS['background_secondary']};
    color: {COLORS['text_primary']};
    border: 1px solid {COLORS['border_default']};
    padding: 8px 16px;
    border-radius: 4px;
    font-weight: 500;
    min-height: 24px;
}}

QPushButton:hover {{
    background-color: {COLORS['hover_overlay']};
    border-color: {COLORS['border_focus']};
}}

QPushButton:pressed {{
    background-color: {COLORS['accent_primary']};
}}

QPushButton:disabled {{
    background-color: {COLORS['background_input']};
    color: {COLORS['text_muted']};
    border-color: {COLORS['text_muted']};
}}

QLineEdit {{
    background-color: {COLORS['background_input']};
    color: {COLORS['text_primary']};
    border: 1px solid {COLORS['border_default']};
    padding: 8px;
    border-radius: 4px;
    font-size: 12px;
}}

QLineEdit:focus {{
    border-color: {COLORS['border_focus']};
    outline: none;
}}

QLineEdit:read-only {{
    background-color: {COLORS['background_secondary']};
    color: {COLORS['text_secondary']};
}}

QDialog {{
    background-color: {COLORS['background_primary']};
    color: {COLORS['text_primary']};
}}

QMessageBox {{
    background-color: {COLORS['background_primary']};
    color: {COLORS['text_primary']};
}}

QFileDialog {{
    background-color: {COLORS['background_primary']};
    color: {COLORS['text_primary']};
}}

QProgressBar {{
    background-color: {COLORS['background_secondary']};
    border: 1px solid {COLORS['border_default']};
    border-radius: 4px;
    text-align: center;
}}

QProgressBar::chunk {{
    background-color: {COLORS['accent_primary']};
    border-radius: 3px;
}}
"""

# Text input styles
TEXTBOX_STYLE = f"""
QLineEdit {{
    background-color: {COLORS['background_input']};
    color: {COLORS['text_primary']};
    padding: 8px;
    font-size: 12px;
    border: 1px solid {COLORS['border_default']};
    border-radius: 4px;
}}
QLineEdit:focus {{
    border-color: {COLORS['border_focus']};
}}
"""

# Feedback styles for correct/incorrect answers
CORRECT_FEEDBACK_STYLE = f"""
QLineEdit {{
    background-color: #1b5e20;
    color: {COLORS['text_primary']};
    border: 2px solid {COLORS['accent_success']};
    padding: 8px;
    font-size: 12px;
    border-radius: 4px;
}}
"""

INCORRECT_FEEDBACK_STYLE = f"""
QLineEdit {{
    background-color: #b71c1c;
    color: {COLORS['text_primary']};
    border: 2px solid {COLORS['accent_error']};
    padding: 8px;
    font-size: 12px;
    border-radius: 4px;
}}
"""

# Label styles
BOLD_LABEL_STYLE = f"font-weight: bold; color: {COLORS['text_primary']};"
FEEDBACK_LABEL_STYLE = f"color: {COLORS['accent_error']}; font-weight: bold; margin: 5px;"
INSTRUCTION_LABEL_STYLE = f"color: {COLORS['text_muted']}; font-style: italic;"
MODE_LABEL_STYLE = f"font-weight: bold; font-size: 14px; color: {COLORS['text_primary']};"
FILE_LABEL_STYLE = f"color: {COLORS['text_secondary']};"
TITLE_LABEL_STYLE = f"font-size: 18px; font-weight: bold; color: {COLORS['text_primary']}; margin: 10px;"

# Button styles
BUTTON_STYLE = f"""
QPushButton {{
    background-color: {COLORS['background_secondary']};
    color: {COLORS['text_primary']};
    border: 1px solid {COLORS['border_default']};
    padding: 12px 20px;
    border-radius: 4px;
    font-weight: 500;
    min-height: 30px;
    font-size: 12px;
}}
QPushButton:hover {{
    background-color: {COLORS['hover_overlay']};
    border-color: {COLORS['border_focus']};
}}
QPushButton:pressed {{
    background-color: {COLORS['accent_primary']};
}}
"""

MAIN_BUTTON_STYLE = f"""
QPushButton {{
    background-color: {COLORS['accent_primary']};
    color: {COLORS['text_primary']};
    border: none;
    padding: 15px 25px;
    border-radius: 6px;
    font-weight: 600;
    font-size: 14px;
    min-height: 40px;
}}
QPushButton:hover {{
    background-color: #0086d1;
}}
QPushButton:pressed {{
    background-color: #005a8b;
}}
"""

# Statistics display styles
STATS_LABEL_STYLE = f"""
QLabel {{
    color: {COLORS['text_primary']};
    font-weight: bold;
    background-color: {COLORS['background_secondary']};
    padding: 6px 12px;
    border-radius: 4px;
    border: 1px solid {COLORS['border_default']};
    margin: 2px;
}}
"""

# Window styles
WINDOW_STYLE = f"""
QMainWindow {{
    background-color: {COLORS['background_primary']};
    color: {COLORS['text_primary']};
}}
QWidget {{
    background-color: {COLORS['background_primary']};
    color: {COLORS['text_primary']};
}}
"""

# Results window specific styles
RESULTS_TITLE_STYLE = f"font-size: 20px; font-weight: bold; color: {COLORS['text_primary']}; margin: 15px 0px;"
RESULTS_STATS_STYLE = f"font-size: 14px; color: {COLORS['text_primary']}; margin: 8px 0px;"
RESULTS_ACCURACY_STYLE = f"font-size: 16px; font-weight: bold; color: {COLORS['accent_success']}; margin: 10px 0px;"
