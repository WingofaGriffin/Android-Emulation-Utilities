import os
import adbutils
import sys
import downloadAPKs

class Logger(object):
    def __init__(self, filename="Default.log"):
        self.terminal = sys.stdout
        self.log = open(filename, "a")

    def write(self, message):
        # if message and not message.isspace():
        self.terminal.write(f"{message}")
        self.log.write(f"{message}")
    
    def flush(self): pass

sys.stdout = Logger("emudroid-installer.log")

# Check for updates
versionNumber=0.1
currentVersion=versionNumber #TO BE ADDED
if versionNumber != currentVersion:
    print("There is a newer version of Android Emulation Utilities available.")
    print("Please navigate to https://github.com/WingofaGriffin/Android-Emulation-Utilities/releases/latest")
    continue = input("Continue anyway? y/n (default: y)")
    if continue == "n":
        quit()

print("Welcome to Android Emulation Utilities! Please wait for further instructions.")

# Ensure adb is installed
try:
    os.system("adb version")
except Exception as ex:
    template = "An exception of type {0} occurred. Arguments:\n{1!r}"
    message = template.format(type(ex).__name__, ex.args)
    print(message)
    print("adb is likely not installed. Please install it before running this program: https://developer.android.com/tools/releases/platform-tools#downloads")
    exit()

# Initialize adb
adb = adbutils.AdbClient(host="127.0.0.1", port=5037)
for info in adb.list():
    print(info.serial, info.state)

# You do not need to offer serial if only one device connected
# RuntimeError will be raised if multi device connected
try:
    d = adb.device()
except Exception as ex:
    template = "An exception of type {0} occurred. Arguments:\n{1!r}"
    message = template.format(type(ex).__name__, ex.args)
    print(message)
    print("Android device likely not found. Please ensure your Android device is connected to this system and is properly in debug mode: https://developer.android.com/tools/adb#Enabling")
    exit()

if not os.path.exists("apks"):
    os.mkdir("apks")

# Check if APKs have already been downloaded
if os.listdir('apks'):
    redownload = input("APKs folder is not empty, would you like to redownload? (NOTE: Every APK in this folder will be installed) y/n (default: y)\n")
    if redownload != "n":
        downloadAPKs.downloadScript()
else:
    downloadAPKs.downloadScript()

# Install apks
for apk in os.listdir("apks"):
    if apk.endswith(".apk"):
        d.install(f"apks/{apk}")

downloadAPKs.installPlayStore(d)

# Copy the folder structure over (for some reason the python package doesn't work)
os.system("adb push Emulation /storage/emulated/0")

# Copy obtainium json to downloads to be uploaded
print("Opening browser to Obtainium config downloader. Please add the Obtainium configs for the desired applications.")
shellcmd="am start -a android.intent.action.VIEW -d https://wingofagriffin.github.io/Android-Emulation-Utilities/obtainium.html"
d.shell(shellcmd)
print("Press Enter to continue...")
input()
