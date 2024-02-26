import os
import adbutils

import nethersx2patch
import downloadAPKs
import helperfunctions

# Initialize adb
adb = adbutils.AdbClient(host="127.0.0.1", port=5037)
for info in adb.list():
    print(info.serial, info.state)

# You do not need to offer serial if only one device connected
# RuntimeError will be raised if multi device connected
d = adb.device()

if not os.path.exists("apks"):
    os.mkdir("apks")

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

installPlayStore(d)

# Copy the folder structure over
d.sync.push("Emulation", "/storage/sdcard0/")