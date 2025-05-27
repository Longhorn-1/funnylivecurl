import os
import time
import urllib.request
import webbrowser
import sys
import platform
import shutil

# Check if ANSI colors should be used
def detect_color_support():
    if os.name != "nt":
        return True  # Unix terminals usually support ANSI
    if "WT_SESSION" in os.environ or "TERM" in os.environ:
        return True  # Windows Terminal or ANSI-aware
    return False  # Classic CMD — no color

USE_COLOR = detect_color_support()

# Define ANSI colors
RED = "\033[91m" if USE_COLOR else ""
CYAN = "\033[96m" if USE_COLOR else ""
YELLOW = "\033[93m" if USE_COLOR else ""
WHITE = "\033[97m" if USE_COLOR else ""
BLUE_BG = "\033[44m" if USE_COLOR else ""
RESET = "\033[0m" if USE_COLOR else ""

def spooky_print(msg, delay=0.04, color=RED):
    for char in msg:
        print(f"{color}{char}{RESET}", end='', flush=True)
        time.sleep(delay)
    print()

def fake_encrypt_files():
    for i in range(1, 11):
        spooky_print(f"[{i}/10] Encrypting file: /system/core/boot_{i}.dll", delay=0.01, color=CYAN)
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
    cols = shutil.get_terminal_size((80, 20)).columns
    os_name = platform.system()

    os.system('cls' if os_name == 'Windows' else 'clear')

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

    print(BLUE_BG + WHITE)
    for line in lines:
        print(line.center(cols))
    print(RESET)

# Begin the horror
spooky_print("You regret this... hacking into your system...")
time.sleep(1)
spooky_print("Installing virus.scary.exe...")
time.sleep(1.2)
spooky_print("Connecting to C2 server at 13.37.66.6... Success.")
time.sleep(1)
spooky_print("Downloading payload...")

video_url = "https://cdn.discordapp.com/attachments/1212745950443872257/1376978987489820772/virus.scary.mp4?ex=68374b1d&is=6835f99d&hm=80f740c027bafbc85e4217f991b85add405ad557a693f24baff4d9f77aedd264&"
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

# Fake stuff
fake_encrypt_files()
print(RED + skull_art() + RESET)
spooky_print("CRITICAL ERROR: kernel32.dll not found", color=RED)
time.sleep(1)
spooky_print("Attempting recovery... FAILED.", color=YELLOW)
time.sleep(1)
spooky_print("System will reboot in:", color=RED)
countdown(5)

# Terminal beep
print('\a')

# Final horror: Fake BSOD
fake_crash_screen()
time.sleep(5)

# Play scary video
webbrowser.open(video_name)
