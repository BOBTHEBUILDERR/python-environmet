import os
import subprocess

def install_missing_requirements(requirements_file):
    with open(requirements_file) as file:
        requirements = file.read().splitlines()
    missing_requirements = [r for r in requirements if not package_installed(r)]
    if missing_requirements:
        subprocess.run(['pip', 'install', *missing_requirements], check=True)
        print("Missing requirements installed.")
    else:
        print("All requirements are satisfied.")

def package_installed(package_name):
    try:
        subprocess.run(['pip', 'show', package_name], stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
        return True
    except subprocess.CalledProcessError:
        return False

if __name__ == '__main__':
    requirements_file = 'requirements.txt'
    if os.path.exists(requirements_file):
        install_missing_requirements(requirements_file)
    else:
        print("requirements.txt file not found.")
