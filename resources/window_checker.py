import time

import pygetwindow


def ensure_window(title_contains: str, timeout=3):
    """
    Ensure a window with part of the title is active.
    Raises an Exception if not found or not focused within timeout.
    """
    start = time.time()
    while time.time() - start < timeout:
        windows = pygetwindow.getWindowsWithTitle(title_contains)
        for win in windows:
            if win.isActive:
                return True
            else:
                win.activate()
                time.sleep(0.5)
                if win.isActive:
                    return True
        time.sleep(0.5)
    raise Exception(f"Expected window with title containing '{title_contains}' not found or not active.")

def requires_window(title_contains):
    """
    Decorator to ensure a window with part of the title is active.
    """
    def decorator(func):
        def wrapper(*args, **kwargs):
            ensure_window(title_contains)
            return func(*args, **kwargs)
        return wrapper
    return decorator

def get_active_window_title():
    return pygetwindow.getActiveWindowTitle()