import requests

# Helper function to get latest APK from Github
def getLatestGithubAPK(url) :
    response = requests.get(url)
    for i in response.json()[0]["assets"]:
        if i["name"].endswith(".apk"):
            return i["browser_download_url"]
