import os
import subprocess
from env_tester import load_env
from requirements_checker import install_missing_requirements
from telegram_bot import main




api_key, api_hash, bot_token, debug_mode = load_env()
#print(bot_token)

def clear_screen():
    subprocess.run(['clear' if os.name == 'posix' else 'cls'], shell=True)
input("Press Enter to clear the screen.")
clear_screen()

requirements_file = 'requirements.txt'
if os.path.exists(requirements_file):
    install_missing_requirements(requirements_file)
else:
    print("requirements.txt file not found.")
    exit()

if __name__ == "__main__":
    main()
