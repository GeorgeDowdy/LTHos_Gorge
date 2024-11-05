import time
import os
import subprocess
import getpass  # To get the current username
import random  # For random password selection

# ANSI escape code for dark green text
DARK_GREEN = '\033[32m'
RESET = '\033[0m'

# Developer usernames list with common typo variations
developer_usernames = {"roger", "s10095479", "goerg"}
username_variations = {"georg": "goerg"}  # Variations for common typos

# Hardcoded list of passwords
passwords = [
    "1215", "2342", "1232", "0329"
]

# Customizable override key
override_key = "OVERIDE_#ROGER"  # Change this to your desired override key
override_key2 = "OVERIDE_#DOWDY"

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_with_delay(text, delay=0.2):
    for line in text.splitlines():
        print(DARK_GREEN + line + RESET)
        time.sleep(delay)

def select_random_password():
    # Return a random password from the list
    return random.choice(passwords)

def verify_password(selected_password):
    # Prompt the user for the password
    entered_password = input(DARK_GREEN + "Enter Developer Password (or type override key): " + RESET)
    return entered_password == selected_password or entered_password == override_key or override_key2

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
                                                                     
                                                                     
                                                                     
 /$$$$$$$                                                            
| $$__  $$                                                           
| $$  \ $$  /$$$$$$  /$$    /$$                                     
| $$  | $$ /$$__  $$|  $$  /$$/                                     
| $$  | $$| $$$$$$$$ \  $$/$$/                                      
| $$  | $$| $$_____/  \  $$$/                                       
| $$$$$$$/|  $$$$$$$   \  $/                                        
|_______/  \_______/    \_/                                         
                                                                     
                                                                     
                                                                     
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
     Welcome back, developer!
"""

# Display the ASCII title slowly
print_with_delay(title_screen, 0.5)
print_with_delay(footer, 0.3)

# Get the current username
current_user = getpass.getuser()

# Correct the username if it’s a known variation
current_user = username_variations.get(current_user, current_user)

# Check if current user is in the list of developers
if current_user in developer_usernames:
    # Select a random password from the list
    selected_password = select_random_password()
    print(DARK_GREEN + f"Developer access granted! (Random password selected: {selected_password})" + RESET)
    
    if verify_password(selected_password):
        print(DARK_GREEN + "Access confirmed!" + RESET)
    else:
        print(DARK_GREEN + "ERR - Incorrect password." + RESET)
        time.sleep(3)
        exit()
else:
    print(DARK_GREEN + "ERR - User is not developer." + RESET)
    time.sleep(3)
    exit()

# Developer terminal main menu options
print_with_delay("\n\nOptions:\n")
print(DARK_GREEN + "1. Customize with dev control here!" + RESET)
print(DARK_GREEN + "2. Exit\n" + RESET)

user_input = input(DARK_GREEN + "Enter your choice (1 or 2): " + RESET)

if user_input == '1':
    print(DARK_GREEN + "Customizing with developer controls... (Placeholder for your custom functionality)" + RESET)
    # Place any customization code here

elif user_input == '2':
    print(DARK_GREEN + "See you soon!" + RESET)
    time.sleep(10)
    os.system('exit')

else:
    print(DARK_GREEN + "Invalid choice. Exiting..." + RESET)
    os.system('exit')
