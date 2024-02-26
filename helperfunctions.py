import requests
import shutil
import os
from tqdm.auto import tqdm

# Helper function to get latest APK from Github
def getLatestGithubURL(url):
    response = requests.get(url)
    for i in response.json()[0]["assets"]:
        if i["name"].endswith(".apk"):
            return i

def downloadAPK(url, name):
    # make an HTTP request within a context manager
    print(f"Downloading {name}...")
    with requests.get(url, stream=True) as r:
        # check header to get content length, in bytes
        total_length = int(r.headers.get("Content-Length"))
        # implement progress bar via tqdm
        with tqdm.wrapattr(r.raw, "read", total=total_length, desc="")as raw:
            # save the output to a file
            with open(f"apks/{name}", 'wb')as output:
                shutil.copyfileobj(raw, output)

def openPlayStoreApp(id, device):
    shellcmd=f"am start -a adroid.intent.action.VIEW -d 'market://details?id={id}' -p com.android.vending;"
    device.shell(shellcmd)
