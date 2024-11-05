import time
import os
import subprocess
import getpass  # To get the current username
import sys

# ANSI escape code for dark green text
DARK_GREEN = '\033[32m'
RESET = '\033[0m'

# List of developer usernames
developer_usernames = ["roger", "s10095479", "georg"]  # Add more usernames as needed

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_with_delay(text, delay=0.2):
    """Print text with a delay between lines unless space is pressed to skip"""
    for line in text.splitlines():
        print(DARK_GREEN + line + RESET)
        if not wait_for_spacebar():
            time.sleep(delay)

def wait_for_spacebar():
    """Detect if the spacebar is pressed (non-blocking)"""
    if sys.platform == "win32":
        import msvcrt
        if msvcrt.kbhit() and msvcrt.getch() == b' ':
            return True
    else:
        import tty
        import termios
        # Non-blocking read on Unix-like systems (Linux/macOS)
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(fd)
            if sys.stdin.read(1) == ' ':
                return True
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return False

# Clear the screen first
clear_screen()

# ASCII Art for "3 stars and a swirl"
title_screen = """
 /$$    /$$$$$$$$ /$$   /$$                                          
| $$   |__  $$__/| $$  | $$                                          
| $$      | $$   | $$  | $$  /$$$$$$   /$$$$$$$                      
| $$      | $$   | $$$$$$$$ /$$__  $$ /$$_____/                      
| $$      | $$   | $$__  $$| $$  \ $$|  $$$$$$                       
| $$      | $$   | $$  | $$| $$  | $$ \____  $$                      
| $$$$$$$$| $$   | $$  | $$|  $$$$$$/ /$$$$$$$/                     
|________/|__/   |__/  |__/ \______/ |_______/                          
                                                                     
 /$$$$$$$$                                /$$                     /$$
|__  $$__/                               |__/                    | $$
   | $$  /$$$$$$   /$$$$$$  /$$$$$$/$$$$  /$$ /$$$$$$$   /$$$$$$ | $$
   | $$ /$$__  $$ /$$__  $$| $$_  $$_  $$| $$| $$__  $$ |____  $$| $$
   | $$| $$$$$$$$| $$  \__/| $$ \ $$ \ $$| $$| $$  \ $$  /$$$$$$$| $$
   | $$| $$_____/| $$      | $$ | $$ | $$| $$| $$  | $$ /$$__  $$| $$
   | $$|  $$$$$$$| $$      | $$ | $$ | $$| $$| $$  | $$|  $$$$$$$| $$
   |__/ \_______/|__/      |__/ |__/ |__/|__/|__/  |__/ \_______/|__/
                                                                     
"""

footer = """
     Loading... please wait
"""

# Display the ASCII title slowly
print_with_delay(title_screen, 0.5)
print_with_delay(footer, 0.3)

# Display menu options with delay
print(DARK_GREEN + "\n\nOptions:\n" + RESET)
time.sleep(0.5)
print(DARK_GREEN + "1. Run a Python Script" + RESET)
time.sleep(0.5)
print(DARK_GREEN + "2. Run Game Menu" + RESET)
time.sleep(0.5)
print(DARK_GREEN + "3. Watch a Movie?" + RESET)
time.sleep(0.5)
print(DARK_GREEN + "4. Exit\n" + RESET)

# Prompt the user to enter "Dev" to unlock Developer mode
dev_mode_enabled = False
user_input = input(DARK_GREEN + "Enter your choice (1, 2, 3, or 4): " + RESET)

# Check if user enters "Dev" to unlock Developer mode
if user_input.lower() == "dev":
    dev_mode_enabled = True
    print(DARK_GREEN + "Developer Mode Enabled!" + RESET)
    print(DARK_GREEN + "5. Developer Mode\n" + RESET)
    # Re-prompt the user for choice with Developer mode enabled
    user_input = input(DARK_GREEN + "Enter your choice (1-5): " + RESET)

# Run the selected option
if user_input == '1':
    script_name = input(DARK_GREEN + "Enter the Python script name to run (e.g., script.py): " + RESET)
    try:
        subprocess.run(["powershell", "-NoExit", "python", script_name], check=True)
    except Exception as e:
        print(DARK_GREEN + f"Error running the script: {e}" + RESET)

elif user_input == '2':
    try:
        subprocess.run(["powershell", "-NoExit", "python", "game_menu.py"], check=True)
    except Exception as e:
        print(DARK_GREEN + f"Error running the game menu: {e}" + RESET)

elif user_input == '3':
    try:
        subprocess.run(["powershell", "-NoExit", "ssh -o StrictHostKeyChecking=no watch.ascii.theater"], shell=True)
    except Exception as e:
        print(DARK_GREEN + f"Error connecting to ASCII theater: {e}" + RESET)

elif user_input == '4':
    print(DARK_GREEN + "Goodbye! Exiting in 10 seconds..." + RESET)
    time.sleep(10)
    os.system('exit')  # Close the terminal

elif dev_mode_enabled and user_input == '5':
    # Check if the current user is in the list of developers
    current_user = getpass.getuser()
    if current_user in developer_usernames:
        print(DARK_GREEN + "Developer mode activated. Access granted." + RESET)
        
        # Run the developer Python script directly
        subprocess.run(["python", "LTHosDev.py"], shell=True)  # Make sure the script path is correct
    else:
        print(DARK_GREEN + "ERR - User is not developer." + RESET)

else:
    print(DARK_GREEN + "Invalid choice. Exiting..." + RESET)
    os.system('exit')  # Close the terminal
