import os
import adbutils

import nethersx2patch
import downloadAPKs
import helperfunctions

# Ensure adb is installed
try:
    os.system("adb version")
except:
    print("adb not installed. Please install it before running this program: https://developer.android.com/tools/releases/platform-tools#downloads")
    exit()

# Initialize adb
adb = adbutils.AdbClient(host="127.0.0.1", port=5037)
for info in adb.list():
    print(info.serial, info.state)

# You do not need to offer serial if only one device connected
# RuntimeError will be raised if multi device connected
d = adb.device()

if not os.path.exists("apks"):
    os.mkdir("apks")

# Check if APKs have already been downloaded
if os.listdir('apks'):
    redownload = input("APKs folder is not empty, would you like to redownload? y/n\n")
    if redownload != "n":
        # Download APKs
        try:
            downloadAPKs.downloadAPKs()
            nethersx2patch.patchNether()
        except:
            print("APK downloads failed. Check your internet connection and try again.")
            quit()
        else:
            print("APKs downloaded locally.")

# Install apks
for apk in os.listdir("apks"):
    if apk.endswith(".apk"):
        d.install(f"apks/{apk}")

downloadAPKs.installPlayStore(d)

# Copy the folder structure over (for some reason the python package doesn't work)
os.system("adb push Emulation /storage/emulated/0")

# Copy obtainium json to downloads to be uploaded
d.sync.push("obtainium-emus.json", "/storage/emulated/0/Downloads/obtainium-emus.json")