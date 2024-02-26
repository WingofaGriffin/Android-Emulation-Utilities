import requests
import os
from urllib.request import urlretrieve

netherSX2repo='https://api.github.com/repos/Trixarian/NetherSX2-patch/releases'
aetherSX2dl='https://www.aethersx2.com/archive/android/alpha/15210-v1.5-4248.apk'

response = requests.get(netherSX2repo)
netherSX2patch=response.json()[0]["assets"][3]["browser_download_url"]

if not os.path.exists("apks"):
    os.mkdir("apks")

urlretrieve(netherSX2patch, "apks/nethersx2.xdelta")

target = requests.get(aetherSX2dl) # making requests to server
with open("apks/15210-v1.5-4248.apk", "wb") as f: # opening a file handler to create new file 
    f.write(target.content) # writing content to file

os.system("./xdelta3 -d -f -s apks/15210-v1.5-4248.apk apks/nethersx2.xdelta apks/nethersx2.apk")