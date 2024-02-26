import requests
import os
from urllib.request import urlretrieve

netherSX2repo='https://api.github.com/repos/Trixarian/NetherSX2-patch/releases'
aetherSX2dl='https://www.aethersx2.com/archive/android/alpha/15210-v1.5-4248.apk'

# Get the latest patch from github
response = requests.get(netherSX2repo)
netherSX2patch=response.json()[0]["assets"][3]["browser_download_url"]

# Create apks folder if it doesn't exist
if not os.path.exists("apks"):
    os.mkdir("apks")

# Download the patch file for somereason this doesn't work with requests
urlretrieve(netherSX2patch, "apks/nethersx2.xdelta")

# Download AetherSX2
target = requests.get(aetherSX2dl) # making requests to server
with open("apks/15210-v1.5-4248.apk", "wb") as f: # opening a file handler to create new file 
    f.write(target.content) # writing content to file

# Patch with bundled xdelta3 binary
os.system("./xdelta3 -d -f -s apks/15210-v1.5-4248.apk apks/nethersx2.xdelta apks/nethersx2.apk")