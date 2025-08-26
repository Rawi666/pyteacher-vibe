"""
Unit tests for WindowManager
"""
import pytest
from PySide6.QtWidgets import QWidget, QApplication
from pyteacher.utils.window_manager import WindowManager
import sys


class TestWindowManager:

    @pytest.fixture(autouse=True)
    def setup_app(self):
        """Setup QApplication for GUI tests"""
        if not QApplication.instance():
            self.app = QApplication(sys.argv)
        else:
            self.app = QApplication.instance()
        yield
        # Cleanup is handled by the app instance

    def test_window_manager_creation(self):
        """Test window manager creation"""
        wm = WindowManager()
        assert wm._main_window is None
        assert len(wm._active_windows) == 0

    def test_set_main_window(self):
        """Test setting main window"""
        wm = WindowManager()
        main_widget = QWidget()
        wm.set_main_window(main_widget)
        assert wm._main_window == main_widget
        assert 'main' in wm._active_windows

    def test_register_window(self):
        """Test registering windows"""
        wm = WindowManager()
        test_widget = QWidget()
        wm.register_window('test', test_widget)
        assert 'test' in wm._active_windows
        assert wm._active_windows['test'] == test_widget

    def test_close_window(self):
        """Test closing specific window"""
        wm = WindowManager()
        test_widget = QWidget()
        wm.register_window('test', test_widget)

        assert 'test' in wm._active_windows
        wm.close_window('test')
        assert 'test' not in wm._active_windows

    def test_close_all_except_main(self):
        """Test closing all windows except main"""
        wm = WindowManager()
        main_widget = QWidget()
        test_widget1 = QWidget()
        test_widget2 = QWidget()

        wm.set_main_window(main_widget)
        wm.register_window('test1', test_widget1)
        wm.register_window('test2', test_widget2)

        assert len(wm._active_windows) == 3
        wm.close_all_except_main()
        assert len(wm._active_windows) == 1
        assert 'main' in wm._active_windows

    def test_cleanup(self):
        """Test cleanup functionality"""
        wm = WindowManager()
        main_widget = QWidget()
        test_widget = QWidget()

        wm.set_main_window(main_widget)
        wm.register_window('test', test_widget)

        assert len(wm._active_windows) == 2
        wm.cleanup()
        assert len(wm._active_windows) == 0
