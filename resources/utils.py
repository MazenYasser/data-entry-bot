import os
from winsound import Beep

import pyautogui
import requests

from .constants import (CONFIRM_SAVE_AS_TITLE, KEY_INTERVAL, NEW_NOTEPAD_TITLE,
                        NOTEPAD_TITLE, POSTS_API_URL, RUN_TITLE, SAVE_AS_TITLE,
                        SAVE_DIR_NAME)
from .window_checker import (ensure_window, get_active_window_title,
                             requires_window)


# ---------------------
# Filesystem
# ---------------------
def ensure_output_dir():
    """
    Ensure the output directory exists. If not, create it.
    """
    path = os.path.join(os.path.expanduser("~"), "Desktop", SAVE_DIR_NAME)
    os.makedirs(path, exist_ok=True)
    return path

def ensure_logs_dir():
    """
    Ensure the output directory exists. If not, create it.
    """
    path = os.path.join(os.path.dirname(__file__), "logs")
    os.makedirs(path, exist_ok=True)
    return path

# ---------------------
# Data fetching from API
# ---------------------
def fetch_posts(page=1, per_page=10):
    try:
        response = requests.get(f"{POSTS_API_URL}?_page={page}&_per_page={per_page}")
        
        if response.status_code != 200:
            raise requests.exceptions.RequestException(f"Error fetching posts: {response.status_code}")
        
        posts = response.json()
        return posts
    except requests.exceptions.RequestException as e:
        raise requests.exceptions.RequestException(f"Error fetching posts: {e}")


# ---------------------
# App Automation
# ---------------------
def launch_run():
    pyautogui.hotkey("win", "r")

@requires_window(RUN_TITLE)
def launch_notepad():
    pyautogui.write("notepad", interval=0.1)
    pyautogui.press("enter")

@requires_window(NEW_NOTEPAD_TITLE)
def write_post(post):
    pyautogui.write(f"Title: {post['title']}\n\n", interval=KEY_INTERVAL)
    pyautogui.write(f"Body: {post['body']}\n\n", interval=KEY_INTERVAL)

    

@requires_window(NEW_NOTEPAD_TITLE)
def save_post(post, output_dir):
    pyautogui.hotkey("ctrl", "s")
    ensure_window(SAVE_AS_TITLE)
    pyautogui.write(f"{output_dir}\\post {post['id']}.txt", interval=KEY_INTERVAL)
    pyautogui.press("enter")
    current_window_title = get_active_window_title()
    
    # If the file name already exists, overwrite.
    if current_window_title == CONFIRM_SAVE_AS_TITLE:
        pyautogui.press("y")

@requires_window(NOTEPAD_TITLE)
def exit_notepad():
    pyautogui.hotkey("alt", "f4")
    Beep(500, 500)