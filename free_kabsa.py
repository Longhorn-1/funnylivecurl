import os
import time
import urllib.request
import webbrowser

def spooky_print(msg, delay=0.04):
    for char in msg:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def fake_encrypt_files():
    for i in range(10):
        spooky_print(f"[{i+1}/10] Encrypting file: system32/boot_{i}...", delay=0.01)
        time.sleep(0.1)

spooky_print("You regret this... hacking into your system...")
time.sleep(1)
spooky_print("Installing virus.scary.exe...")
time.sleep(1)
spooky_print("Connecting to C2 server... Success.")
time.sleep(1)
spooky_print("Downloading payload...")

video_url = "https://cdn.discordapp.com/attachments/1212496951103324220/1371164541236416614/202505111923.mp4?ex=682223fd&is=6820d27d&hm=7161de71945918344db3cc7a932ab620667fea7587c9222ab01f0ea270b94a5c&"
video_name = "virus.scary.mp4"

try:
    # Set a browser-like User-Agent to bypass Discord's block
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
    req = urllib.request.Request(video_url, headers=headers)
    with urllib.request.urlopen(req) as response, open(video_name, 'wb') as out_file:
        out_file.write(response.read())
    spooky_print("Payload ready.")
except Exception as e:
    spooky_print(f"Error downloading payload: {e}")
    exit(1)

time.sleep(1)
spooky_print("Executing virus.scary.mp4...")
fake_encrypt_files()

spooky_print("Launching payload...")
time.sleep(2)
webbrowser.open(video_name)
