import os
import subprocess
import time
import requests
from pyfiglet import Figlet

# Define the function to display text with live typing effect
def live_typing_effect(text, delay=0.05):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

# Define the figlet text and color
figlet_text = Figlet(font='slant')
figlet_output = figlet_text.renderText('Watsapp Bot')

# Show figlet text with live typing effect
live_typing_effect(figlet_output)

# Wait for a moment before showing the next message
time.sleep(1)

# Show additional text with live typing effect
live_typing_effect("This Tool is created by Alone Stand Larka.")

# Create the Bot folder in Downloads
bot_folder_path = os.path.expanduser('~/storage/downloads/Bot')
os.makedirs(bot_folder_path, exist_ok=True)

# Download the file
url = 'https://www.mediafire.com/file/1netptfufzi6w61/techgodv7.zip/file'
zip_file_path = os.path.join(bot_folder_path, 'techgodv7.zip')

response = requests.get(url)
with open(zip_file_path, 'wb') as file:
    file.write(response.content)

# Function to run commands in Termux
def run_command(command):
    subprocess.run(command, shell=True, check=True)

# Commands to be run after downloading the file
commands = [
    'apt update',
    'apt upgrade',
    'pkg install git -y',
    'pkg install python -y',
    'clear',
    'pkg install python3 -y',
    'pkg install node -y',
    'termux-setup-storage',
    f'cd {bot_folder_path}',
    'pkg install zip -y',
    'pkg install unzip -y',
    'unzip techgodv7.zip',
    'cd techgodv7',
    'ls',
    'cd techgodv7',
    'yarn install',
    'npm start'
]

# Run each command
for cmd in commands:
    run_command(cmd)

print("Setup completed successfully.")
