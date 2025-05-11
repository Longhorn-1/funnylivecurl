import os
import time
import urllib.request
import webbrowser

def spooky_print(msg, delay=0.05):
    for char in msg:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

spooky_print("You regret this... hacking into your system...")
time.sleep(1)
spooky_print("Installing virus.scary.exe...")
time.sleep(1.5)
spooky_print("Connecting to C2 server... Success.")
time.sleep(1)
spooky_print("Downloading payload...")

# Download the video
video_url = "https://cdn.discordapp.com/attachments/1212496951103324220/1371164541236416614/202505111923.mp4?ex=682223fd&is=6820d27d&hm=7161de71945918344db3cc7a932ab620667fea7587c9222ab01f0ea270b94a5c&"
video_name = "virus.scary.mp4"

try:
    urllib.request.urlretrieve(video_url, video_name)
    spooky_print("Payload ready.")
    time.sleep(1)
    spooky_print("Executing virus.scary.mp4...")
    webbrowser.open(video_name)
except Exception as e:
    spooky_print(f"Error downloading payload: {e}")
