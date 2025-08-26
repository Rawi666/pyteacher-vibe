"""
Tests for dark theme implementation
"""
import pytest
from PySide6.QtWidgets import QApplication
from PySide6.QtGui import QPalette
from pyteacher.ui.styles import COLORS, APPLICATION_STYLE
from pyteacher.main import setup_dark_theme
from pyteacher.ui.main_window import MainWindow
from pyteacher.ui.drill_window import DrillWindow
from pyteacher.ui.test_window import TestWindow
from pyteacher.ui.results_window import ResultsWindow


class TestDarkTheme:
    def test_color_constants_defined(self):
        """Test that all required color constants are defined"""
        required_colors = [
            'background_primary',
            'background_secondary',
            'background_input',
            'text_primary',
            'text_secondary',
            'text_muted',
            'accent_primary',
            'accent_success',
            'accent_error',
            'border_default',
            'border_focus',
            'hover_overlay'
        ]

        for color in required_colors:
            assert color in COLORS
            assert COLORS[color].startswith('#')
            assert len(COLORS[color]) == 7  # #RRGGBB format

    def test_application_style_defined(self):
        """Test that application style sheet is defined"""
        assert APPLICATION_STYLE is not None
        assert len(APPLICATION_STYLE) > 0
        assert 'QMainWindow' in APPLICATION_STYLE
        assert 'QPushButton' in APPLICATION_STYLE
        assert 'QLineEdit' in APPLICATION_STYLE

    def test_setup_dark_theme_function(self, qtbot):
        """Test that dark theme setup function works"""
        app = QApplication.instance()
        if app is None:
            app = QApplication([])

        # Ensure we have a QApplication instance
        assert isinstance(app, QApplication)

        setup_dark_theme(app)

        # Check that palette has been set
        palette = app.palette()
        assert palette is not None

        # Check that style sheet has been set
        style_sheet = app.styleSheet()
        assert style_sheet is not None
        assert len(style_sheet) > 0

    def test_main_window_dark_theme(self, qtbot):
        """Test that main window applies dark theme"""
        window = MainWindow()
        qtbot.addWidget(window)

        # Check that window has style sheet applied
        style_sheet = window.styleSheet()
        assert style_sheet is not None
        assert len(style_sheet) > 0

    def test_drill_window_dark_theme(self, qtbot):
        """Test that drill window applies dark theme"""
        window = DrillWindow()
        qtbot.addWidget(window)

        # Check that window has style sheet applied
        style_sheet = window.styleSheet()
        assert style_sheet is not None
        assert len(style_sheet) > 0

    def test_test_window_dark_theme(self, qtbot):
        """Test that test window applies dark theme"""
        window = TestWindow()
        qtbot.addWidget(window)

        # Check that window has style sheet applied
        style_sheet = window.styleSheet()
        assert style_sheet is not None
        assert len(style_sheet) > 0

    def test_results_window_dark_theme(self, qtbot):
        """Test that results window applies dark theme"""
        window = ResultsWindow()
        qtbot.addWidget(window)

        # Check that window has style sheet applied
        style_sheet = window.styleSheet()
        assert style_sheet is not None
        assert len(style_sheet) > 0

    def test_dark_colors_are_dark(self):
        """Test that the primary colors are actually dark"""
        # Convert hex to RGB and check brightness
        def hex_to_brightness(hex_color):
            hex_color = hex_color.lstrip('#')
            rgb = tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))
            # Calculate brightness (0-255, lower is darker)
            return (rgb[0] * 299 + rgb[1] * 587 + rgb[2] * 114) / 1000

        # Primary background should be dark (low brightness)
        bg_brightness = hex_to_brightness(COLORS['background_primary'])
        assert bg_brightness < 128  # Less than middle gray

        # Secondary background should be slightly lighter but still dark
        bg2_brightness = hex_to_brightness(COLORS['background_secondary'])
        assert bg2_brightness < 128
        assert bg2_brightness > bg_brightness  # But lighter than primary

    def test_text_colors_are_light(self):
        """Test that text colors provide good contrast on dark background"""
        def hex_to_brightness(hex_color):
            hex_color = hex_color.lstrip('#')
            rgb = tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))
            return (rgb[0] * 299 + rgb[1] * 587 + rgb[2] * 114) / 1000

        # Primary text should be light (high brightness)
        text_brightness = hex_to_brightness(COLORS['text_primary'])
        assert text_brightness > 200  # Should be quite light

        # Secondary text should be lighter than muted text
        text2_brightness = hex_to_brightness(COLORS['text_secondary'])
        muted_brightness = hex_to_brightness(COLORS['text_muted'])
        assert text2_brightness > muted_brightness
