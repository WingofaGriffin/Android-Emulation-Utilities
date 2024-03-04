import requests
import os
import helperfunctions
import tempdir

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
    try:
        os.system("./xdelta3 -d -f -s apks/aethersx2.apk apks/nethersx2.xdelta apks/nethersx2.apk")
        # Cleanup files
        os.remove(os.path.join(tempfile.gettempdir(), "AndroidEmulationUtilities", "apks", "nethersx2.xdelta"))
        os.remove("apks/aethersx2.apk")
    except Exception as ex:
        template = "An exception of type {0} occurred. Arguments:\n{1!r}"
        message = template.format(type(ex).__name__, ex.args)
        print(message)
        print("xdelta patch failed. Report a bug in GitHub with the log.")
