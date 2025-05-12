import os
import time
import urllib.request
import webbrowser
import sys
import platform
import shutil

# Terminal colors
RED = "\033[91m"
CYAN = "\033[96m"
YELLOW = "\033[93m"
RESET = "\033[0m"

def spooky_print(msg, delay=0.04, color=RED):
    for char in msg:
        print(f"{color}{char}{RESET}", end='', flush=True)
        time.sleep(delay)
    print()

def fake_encrypt_files():
    for i in range(1, 11):
        spooky_print(f"[{i}/10] Encrypting file: C:/system/core/boot_{i}.dll", delay=0.01, color=CYAN)
        time.sleep(0.1)

def countdown(seconds):
    for i in range(seconds, 0, -1):
        spooky_print(f"{i}...", delay=0.4, color=YELLOW)
        time.sleep(0.5)

def skull_art():
    return r"""
       ______
    .-'      '-.
   /            \
  |              |
  |,  .-.  .-.  ,|
  | )(_o/  \o_)( |
  |/     /\     \|
  (_     ^^     _)
   \__|IIIIII|__/
    | \IIIIII/ |
    \          /
     `--------`
"""

def fake_crash_screen():
    cols = shutil.get_terminal_size().columns
    os_name = platform.system()

    # Clear screen
    os.system('cls' if os_name == 'Windows' else 'clear')

    # Blue screen text
    blue_bg = "\033[44m"
    white_fg = "\033[97m"
    reset = "\033[0m"

    lines = [
        "",
        "  A problem has been detected and your system has been shut down to prevent damage.",
        "  The problem seems to be caused by the following file: virus.scary.exe",
        "",
        "  PAGE_FAULT_IN_NONPAGED_AREA",
        "",
        "  If this is the first time you've seen this stop error screen,",
        "  restart your computer. If this screen appears again, follow",
        "  these steps:",
        "",
        "  Check to make sure any new hardware or software is properly installed.",
        "  If this is a new installation, ask your hardware or software manufacturer",
        "  for any updates you might need.",
        "",
        "  If problems continue, disable or remove any newly installed hardware",
        "  or software. Disable BIOS memory options such as caching or shadowing.",
        "  If you need to use Safe Mode to remove or disable components,",
        "  restart your computer, press F8 to select Advanced Startup Options,",
        "  and then select Safe Mode.",
        "",
        f"  Technical information:",
        "",
        "  *** STOP: 0x00000050 (0xDEADBEEF, 0x00000000, 0xBADF00D, 0x00000000)",
        "",
        "  Collecting data for crash dump ...",
        "  Initializing disk for crash dump ...",
        "  Beginning dump of physical memory.",
        "  Dumping physical memory to disk: 100",
        "",
        "  Physical memory dump complete.",
        "  Contact your system administrator or technical support group.",
        "",
    ]

    print(blue_bg + white_fg)
    for line in lines:
        print(line.center(cols))
    print(reset)

# Begin prank
spooky_print("You regret this... hacking into your system...")
time.sleep(1)
spooky_print("Installing virus.scary.exe...")
time.sleep(1.2)
spooky_print("Connecting to C2 server at 13.37.66.6... Success.")
time.sleep(1)
spooky_print("Downloading payload...")

# Download the scary video
video_url = "https://cdn.discordapp.com/attachments/1212496951103324220/1371164541236416614/202505111923.mp4?ex=682223fd&is=6820d27d&hm=7161de71945918344db3cc7a932ab620667fea7587c9222ab01f0ea270b94a5c&"
video_name = "virus.scary.mp4"

try:
    headers = {'User-Agent': 'Mozilla/5.0'}
    req = urllib.request.Request(video_url, headers=headers)
    with urllib.request.urlopen(req) as response, open(video_name, 'wb') as out_file:
        out_file.write(response.read())
    spooky_print("Payload acquired.")
except Exception as e:
    spooky_print(f"Error downloading payload: {e}", color=YELLOW)
    sys.exit(1)

time.sleep(1)
spooky_print("Executing virus.scary.exe...")
time.sleep(1)

# Fake file encryption
fake_encrypt_files()

# Scary skull
print(RED + skull_art() + RESET)
spooky_print("CRITICAL ERROR: kernel32.dll not found", color=RED)
time.sleep(1)
spooky_print("Attempting recovery... FAILED.", color=YELLOW)
time.sleep(1)

spooky_print("System will reboot in:", color=RED)
countdown(5)

# Terminal beep (optional)
print('\a')

# FAKE CRASH SCREEN
fake_crash_screen()

# Pause before playing video
time.sleep(5)

# Open video
webbrowser.open(video_name)
