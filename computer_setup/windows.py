# a full install of my windows system (mostly made for fun)
# Proceed with caution, may do some damage to your computer

import requests
import subprocess
import os
import sys

STEAM_URL = 'https://steamcdn-a.akamaihd.net/client/installer/SteamSetup.exe'
STEAM_PATH = 'SteamSetup.exe'

FIREFOX_URL = 'https://www.mozilla.org/en-US/firefox/download/thanks/'
FIREFOX_PATH = 'Firefox Installer.exe'

VSCODE_URL = ''
VSCODE_PATH = ''

DISCORD_URL = ''
DISCORD_PATH = ''

PRISM_LAUNCHER_URL = ''
PRISM_LAUNCHER_PATH = ''

SCOOP_URL = ''
SCOOP_PATH = ''

#used to download programs
def download_program(url, save_path):
    response = requests.get(url, stream=True)
    if response.status_code == 200:
        with open(save_path, 'wb') as file:
            for chunk in response.iter_content(chunk_size=8192):
                file.write(chunk)
        print(f"Saved as: {save_path}")
    else:
        print(f"Failed to download: {response.status_code}")

def powershell_script(script_path):
    try:
        subprocess.run(["powershell", "-ExecutionPolicy", "ByPass", "-File", script_path], check=True)
    except subprocess.CalledProcessError as e:
        print(f"failed")

#add a download meter for the looks
if __name__ == '__main__':
    print("Downlaoding Steam")
    download_program(STEAM_URL, STEAM_PATH)

    print("Downloading Firefox")



    print("Downloading Scoop")
    if download_program(SCOOP_URL, SCOOP_PATH):
        powershell_script(SCOOP_PATH)



    os.remove(STEAM_PATH, FIREFOX_PATH, VSCODE_PATH, DISCORD_PATH, PRISM_LAUNCHER_PATH, SCOOP_PATH)
