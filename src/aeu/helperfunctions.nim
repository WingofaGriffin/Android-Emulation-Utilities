import std/[httpclient, json, strformat, strutils]
# import suru

proc getLatestGithubURL*(repo: string): string =
    var 
        url = &"https://api.github.com/repos/{repo}/releases"
        client = newHttpClient()
        content = client.getContent(url).parseJson
        options = content[0]["assets"]
    for i in options:
        if i["name"].getStr().endswith(".apk") == true:
            client.close()
            return i["browser_download_url"].getStr()

proc downloadAPK*(url: string, name: string): bool =
    echo &"Downloading {name}..."

proc openPLayStore*(id: string, device): bool =
    echo &"Navigating Play Store to {id}. Please install manually and press enter to continue when done."
    let shellcmd = &"am start -a android.intent.action.VIEW -d 'market://details?id={id}'"