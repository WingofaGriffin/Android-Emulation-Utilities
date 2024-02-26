import requests
import os
from urllib.request import urlretrieve
import helperfunctions

netherSX2repo='https://api.github.com/repos/Trixarian/NetherSX2-patch/releases'
aetherSX2dl='https://www.aethersx2.com/archive/android/alpha/15210-v1.5-4248.apk'

def patchNether():
    # Get the latest patch from github
    response = requests.get(netherSX2repo)
    netherSX2patch=response.json()[0]["assets"][3]["browser_download_url"]

    # Create apks folder if it doesn't exist
    if not os.path.exists("apks"):
        os.mkdir("apks")

    # Download apk and patch
    helperfunctions.downloadAPK(netherSX2patch, "nethersx2.xdelta")
    helperfunctions.downloadAPK(aetherSX2dl, "aethersx2.apk")

    # Patch with bundled xdelta3 binary
    os.system("./xdelta3 -d -f -s apks/15210-v1.5-4248.apk apks/nethersx2.xdelta apks/nethersx2.apk")
    # Cleanup files
    os.remove("apks/nethersx2.xdelta")
    os.remove("apks/15210-v1.5-4248.apk")
    