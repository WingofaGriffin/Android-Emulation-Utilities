from adb_shell.adb_device import AdbDeviceTcp, AdbDeviceUsb
from adb_shell.auth.sign_pythonrsa import PythonRSASigner
import os

# Load the public and private keys
try:
    # for *nix devices
    adbkey = f'{os.getenv('HOME')}/.android/adbkey'
    with open(adbkey) as f:
        priv = f.read()
    with open(adbkey + '.pub') as f:
        pub = f.read()
    signer = PythonRSASigner(pub, priv)
except:
    print("adbkeys not found. Have you connected an Android device to this computer?")
    quit()

# Connect via USB (package must be installed via `pip install adb-shell[usb])`
print("Attempting to connect to Android device over USB...")
try:
    device = AdbDeviceUsb()
    device.connect(rsa_keys=[signer], auth_timeout_s=0.1):
except:
    print("Device connection over USB failed. Ensure access has been granted on your device.")
    quit()
else:
    print("Device connected successfully!")


