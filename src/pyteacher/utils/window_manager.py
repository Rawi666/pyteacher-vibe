"""
WindowManager for handling window lifecycle and navigation
"""
from typing import Optional, Dict, Any
from PySide6.QtWidgets import QWidget


class WindowManager:
    """Manages window lifecycle and navigation throughout the application"""

    def __init__(self):
        self._main_window: Optional[QWidget] = None
        self._active_windows: Dict[str, QWidget] = {}

    def set_main_window(self, window: QWidget):
        """Set the main application window"""
        self._main_window = window
        self._active_windows['main'] = window

    def show_main_window(self):
        """Show the main window and hide others"""
        if self._main_window:
            self._main_window.show()
            self._main_window.raise_()
            self._main_window.activateWindow()

    def register_window(self, name: str, window: QWidget):
        """Register a window for management"""
        self._active_windows[name] = window

    def show_window(self, name: str, hide_others: bool = False):
        """Show a specific window"""
        if name in self._active_windows:
            window = self._active_windows[name]
            window.show()
            window.raise_()
            window.activateWindow()

            if hide_others:
                for window_name, win in self._active_windows.items():
                    if window_name != name and win.isVisible():
                        win.hide()

    def close_window(self, name: str):
        """Close and cleanup a specific window"""
        if name in self._active_windows:
            window = self._active_windows[name]
            window.close()
            if name != 'main':  # Don't remove main window
                del self._active_windows[name]

    def close_all_except_main(self):
        """Close all windows except main and show main"""
        windows_to_close = []
        for name, window in self._active_windows.items():
            if name != 'main':
                window.close()
                windows_to_close.append(name)

        for name in windows_to_close:
            del self._active_windows[name]

        self.show_main_window()

    def cleanup(self):
        """Cleanup all windows"""
        for window in self._active_windows.values():
            window.close()
        self._active_windows.clear()


# Global window manager instance
window_manager = WindowManager()
