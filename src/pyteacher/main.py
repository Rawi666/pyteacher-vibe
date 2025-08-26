"""
Application entry point for Language Learning App (PySide6)
"""
import sys
from PySide6.QtWidgets import QApplication
from PySide6.QtGui import QPalette, QColor
from PySide6.QtCore import Qt
from pyteacher.ui.main_window import MainWindow
from pyteacher.ui.styles import APPLICATION_STYLE, COLORS
from pyteacher.utils.window_manager import window_manager

def setup_dark_theme(app: QApplication):
    """
    Set up application-wide dark theme that overrides OS settings
    """
    # Set application style sheet
    app.setStyleSheet(APPLICATION_STYLE)

    # Create and apply dark palette
    dark_palette = QPalette()

    # Window colors
    dark_palette.setColor(QPalette.ColorRole.Window, QColor(COLORS['background_primary']))
    dark_palette.setColor(QPalette.ColorRole.WindowText, QColor(COLORS['text_primary']))

    # Base colors for input fields
    dark_palette.setColor(QPalette.ColorRole.Base, QColor(COLORS['background_input']))
    dark_palette.setColor(QPalette.ColorRole.AlternateBase, QColor(COLORS['background_secondary']))

    # Text colors
    dark_palette.setColor(QPalette.ColorRole.Text, QColor(COLORS['text_primary']))
    dark_palette.setColor(QPalette.ColorRole.BrightText, QColor(COLORS['text_primary']))

    # Button colors
    dark_palette.setColor(QPalette.ColorRole.Button, QColor(COLORS['background_secondary']))
    dark_palette.setColor(QPalette.ColorRole.ButtonText, QColor(COLORS['text_primary']))

    # Highlight colors
    dark_palette.setColor(QPalette.ColorRole.Highlight, QColor(COLORS['accent_primary']))
    dark_palette.setColor(QPalette.ColorRole.HighlightedText, QColor(COLORS['text_primary']))

    # Disabled colors
    dark_palette.setColor(QPalette.ColorGroup.Disabled, QPalette.ColorRole.WindowText, QColor(COLORS['text_muted']))
    dark_palette.setColor(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Text, QColor(COLORS['text_muted']))
    dark_palette.setColor(QPalette.ColorGroup.Disabled, QPalette.ColorRole.ButtonText, QColor(COLORS['text_muted']))

    app.setPalette(dark_palette)

def main():
    app = QApplication(sys.argv)

    # Force dark theme regardless of OS settings
    setup_dark_theme(app)

    window = MainWindow()
    window_manager.set_main_window(window)
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
