# Keylogger Script

## Overview
This repository contains a basic keylogger script written in Python. The script captures keystrokes, saves them locally in a log file, and optionally emails the log file. It is designed for **educational purposes only** to demonstrate how keylogging works and should not be used for malicious activities.

## Features
- Captures and logs all keystrokes.
- Saves keystrokes in a `keylogger.txt` file.
- Sends the contents of the log file to a specified email address.
- Simple and lightweight implementation.

## Prerequisites
- Python 3.6 or later.
- Required Python libraries:
  - `pynput`
  - `smtplib` (built-in)
  - `ssl` (built-in)

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/Mecktro/Keylogger.git
   cd Keylogger
   ```

2. Install the required library:
   ```bash
   pip install pynput
   ```

3. Configure the script:
   - Open `keylogger.py`.
   - Replace placeholders (`sender_email`, `receiver_email`, `password`) with your email credentials.

## Usage
1. Run the script:
   ```bash
   python keylogger.py
   ```

2. Press the `Esc` key to stop the keylogger.

## Security Disclaimer
This script is intended solely for **educational purposes**. Using it to monitor or log keystrokes without permission is **illegal and unethical**. Always ensure you have explicit consent before deploying this tool.

## Repository Structure
```
Keylogger/
|├── keylogger.py        # Main script
|├── keylogger.txt       # Log file (generated after running the script)
|└── README.md           # Documentation
```

## License
This project is licensed under the MIT License. See the LICENSE file for more details.

## Contributing
Contributions are welcome! Feel free to submit issues or pull requests to improve functionality or add features.

---

**Author**: Mecktro

