# This code is the initialization script for CLI TikTok. It performs the following tasks:

#     Clears the console screen
#     Welcomes the user and waits for the user to press the "ENTER" key to proceed.
#     Tests for required dependencies and installs them if missing.
#     Determines the operating system and Python version.
#     Checks for available updates to the software.
#     If an internet connection is not available, it informs the user and exits the program.

# The code also uses the log function to log important events during the execution of the script.

import os
import platform
import sys
import requests

from log import logtofile as log


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def init():
    clear_screen()
    print("Welcome to CLI TikTok, an open-source TikTok archiver and viewer!")
    input("Press ENTER to proceed")

    log("Started dependency test")
    required_libraries = ["atoma", "requests", "yt_dlp", "distro"]
    missing_libraries = [library for library in required_libraries if not _library_exists(library)]
    if missing_libraries:
        log("Dependency test failed - Missing libraries: " + ", ".join(missing_libraries))
        clear_screen()
        input("The program detected dependencies are not installed.\nPress ENTER to install the necessary libraries.\n(You will need to open the program again afterwards)")
        log("User accepted automatic installation, running it.\n")
        os.system("pip install -r requirements.txt --user")
        clear_screen()
        return -1
    else:
        log("Dependency test successful.\n")

    log("Started operating system and python detection")
    log("Operating System: " + _get_os_info())
    log("Python " + _get_python_version())
    log("Operating System and Python detection finished\n")

    log("Started update / networking test")
    try:
        import ast
        data = requests.get("https://raw.githubusercontent.com/nanometer5088/CLI-TikTok/main/src/constants.py")
        userversion = _read_user_version()
        data = str(ast.literal_eval(data.text.split("APP = ")[1])["version"])
        if userversion < data:
            log(f"New version detected! User version is {userversion}, but {data} was found on Github.")
            clear_screen()
            input("\tThere's a new version available!\n\tUpdates bring performance and feature improvements!\n\tDownload the new version here:\n\thttps://github.com/nanometer5088/CLI-TikTok/archive/refs/heads/main.zip\n\n\tPress ENTER to proceed")
            clear_screen()
        else:
            log("The user has internet access and the software is up-to-date.\n")
            clear_screen()

    except requests.exceptions.ConnectionError:
        clear_screen()
        log("A connection error was detected when trying to connect to https://raw.githubusercontent.com/ to check for updates.")
        print("CLI-TikTok detected your device isn't connected to the internet.")
        print("This software requires a reliable and uncensored internet connection to properly work.")
        print("Please try again with an internet connection.")
        log("The software exited, and the user was notified of the connection problem.")
        sys.exit()


def _library_exists(library):
    try:
        __import__(library)
        return True
    except ImportError:
        return False


def _get_os_info():
    system = platform.system()
    if system == "Windows":
        return f"Windows {platform.win32_ver()[0]}"
    elif system == "Darwin":
        return f"Mac OS {platform.mac_ver()}"
    elif system == "Linux":
        import distro
        return f"{distro.name()} {distro.version()} - {os.uname().release}"
    else:
        return f"{system} - {platform.machine()}"


def _get_python_version():
    return f"{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro} - {sys.version_info.releaselevel}"


def _read_user_version():
    from src.constants import APP
    return str(APP["version"])