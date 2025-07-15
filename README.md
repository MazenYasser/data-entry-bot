# 📝 TJM Auto Data Entry Bot

A Python automation script that fetches blog posts from the [JSONPlaceholder API](https://jsonplaceholder.typicode.com/guide/) and types them into Notepad, then saves each post as a `.txt` file on the user's Desktop under a folder named `tjm-project`.

Built as a take-home challenge using **PyAutoGUI**, **BotCity**, and supporting libraries like `pygetwindow` for window state validation.

Bootstrapped with **BotCity** cookiecutter template v2.

---

## ✅ Features

- Launches **Notepad** using `win + R`
- Fetches the first 10 blog posts from JSONPlaceholder API
- For each post:
  - Opens Notepad
  - Writes the post title and body in a blog format
  - Saves the file as `post <id>.txt` in `Desktop/tjm-project/`
  - Handles file overwrite confirmation if the file exists
  - Closes Notepad

---

## 💡 Technical Design

- **pyautogui** handles all keyboard automation
- **pygetwindow** is used to check for and activate the correct application window before continuing
- **Custom decorator** `@requires_window("title")` ensures the target window is in focus before executing any critical action
- **BotCity structure**: project uses BotCity cookiecutter template structure and is compatible with **BotCity Studio + Runner**

---

## 📁 Main Project Structure

├── bot.py                     # Main entry point
├── resources/
│   ├── utils.py               # All automation logic
│   ├── window_checker.py      # Window focus checking utilities
│   ├── constants.py           # Configurable values (e.g., output dir, key intervals)
│   ├── logs/                  # Automatically created if a crash occurs
├── README.md                  # You’re reading this!
├── requirements.txt           # Project dependencies
├── textBot.botproj            # BotCity project file

---

## 🧪 Error Handling

- **API Errors**: The app checks HTTP status and handles failed requests gracefully
- **Window Validation**: Each automation step checks that the correct window is in focus (e.g., `"Untitled - Notepad"`, `"Save As"`, etc.)
- **Missing UI Elements**: If a window fails to open within a timeout (default 3s), the script throws an explicit exception
- **Crash Logging**: Any uncaught exception is logged in full detail to `error.log` for inspection

---

## 🧱 Technical Constraints & Decisions

- Used **pyautogui** exclusively for automation as required, even though BotCity offers convenient wrappers
- Introduced a **clean architecture** using decorators (`@requires_window`) to enforce window focus logic
- Used `Beep()` sounds to indicate:
  - ✅ Successful run start
  - 📝 Successful file save
  - ❌ Error occurrence
  - 🧼 End of script (finally block)

---

## 🖥️ Requirements

- Windows OS
- Python 3.12+
- Python packages:
  - `pyautogui`
  - `requests`
  - `pygetwindow`
  - `botcity-core`
  - `botcity-maestro-sdk`

Install dependencies with:

```bash
pip install -r requirements.txt