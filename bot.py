import datetime
import os
import traceback
from winsound import Beep

import pyautogui

from resources.utils import (ensure_output_dir, exit_notepad, fetch_posts,
                             launch_notepad, launch_run, save_post, write_post,
                             ensure_logs_dir)

# Configure PyAutoGUI
pyautogui.PAUSE = 0.5
pyautogui.FAILSAFE = True # This allows fail-safe exit, moving the mouse to the top left corner of the screen will exit the program.


def main(output_dir):
    
    # Step 1: Fetch posts
    posts = fetch_posts()
    print(f"Found {len(posts)} posts")
    
    # Step 2: Launch Notepad then Write and save posts
    for post in posts:
        launch_run()
        launch_notepad()
        write_post(post)
        save_post(post, output_dir)
        exit_notepad()
        

if __name__ == '__main__':
    try:
        ensure_logs_dir()
        output_dir = ensure_output_dir()
        Beep(500, 500)
        main(output_dir)
    except Exception as e:
        Beep(2000, 500)
        log_path = os.path.join(os.path.dirname(__file__), "resources", "logs", f"{datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}_crash_log.txt")
        error_message = f"\n❌ An error occurred: {e}\n"
        print(error_message)

        # Write the traceback to the log file
        with open(log_path, "w") as f:
            f.write("\n--- Traceback ---\n")
            f.write(traceback.format_exc())  # This captures the full traceback as a string
            f.write(error_message)
            
        print(f"\n📄 Crash log saved to: {log_path}\n")
    finally:
        Beep(500, 500)
        input("🔚 Press Enter to exit...")