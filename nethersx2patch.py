import requests
import os
import helperfunctions
import sys

netherSX2repo='https://api.github.com/repos/Trixarian/NetherSX2-patch/releases'
aetherSX2dl='https://github.com/Trixarian/NetherSX2-patch/releases/download/0.0/15210-v1.5-4248.apk'

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
    if sys.platform == "linux" or sys.platform == "darwin":
        # Ensure xdelta is executable
        os.system("chmod +x ./Utilities/xdelta3")
        patchcmd="./Utilities/xdelta3 -d -f -s apks/aethersx2.apk apks/nethersx2.xdelta apks/nethersx2.apk"
    elif system.platform == "win32":
        # To be tested on pc...
        patchcmd="Utilities\\xdelta.exe -d -f -s apks\\aethersx2.apk apks\\nethersx2.xdelta apks\\nethersx2.apk"
    try:
        os.system(patchcmd)
        # Cleanup files
        # os.remove(os.path.join(tempfile.gettempdir(), "AndroidEmulationUtilities", "apks", "nethersx2.xdelta"))
        os.remove(os.path.join("apks", "nethersx2.xdelta"))
        os.remove(os.path.join("apks", "aethersx2.apk"))
    except Exception as ex:
        template = "An exception of type {0} occurred. Arguments:\n{1!r}"
        message = template.format(type(ex).__name__, ex.args)
        print(message)
        print("xdelta patch failed. Report a bug in GitHub with the log.")