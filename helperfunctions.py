import requests
import shutil
from tqdm.auto import tqdm

# Helper function to get latest APK from Github
def getLatestGithubURL(repo):
    url=f"https://api.github.com/repos/{repo}/releases"
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
    print(f"Navigating Play Store to {id}. Please install manually and press enter to continue when done.")
    shellcmd=f"am start -a android.intent.action.VIEW -d 'market://details?id={id}'"
    device.shell(shellcmd)
    print("Press Enter to continue...")
    input()
