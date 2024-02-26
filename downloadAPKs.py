import requests
import os
import helperfunctions

githubAPKs = {
    "obtanium": "https://api.github.com/repos/ImranR98/Obtainium/releases",
    "citra": "https://api.github.com/repos/citra-emu/citra-nightly/releases",
    "yuzu": "https://api.github.com/repos/yuzu-emu/yuzu-android/releases",
    "vita3k": "https://api.github.com/repos/Vita3K/Vita3K-Android/releases",
}

otherAPKs = {
    "retroarch": "https://buildbot.libretro.com/nightly/android/RetroArch.apk",
}

gplayAPKs = {
    "daijisho": "com.magneticchen.daijishou",
    "dolphin": "org.dolphinemu.dolphinemu",
    "duckstation": "com.github.stenzek.duckstation",
    "melonds": "me.magnum.melonds",
    "PPSSPP": "org.ppsspp.ppsspp",
}

def downloadAPKs():
    for e in githubAPKs:
        latestRelease=helperfunctions.getLatestGithubURL(githubAPKs[e])
        helperfunctions.downloadAPK(latestRelease["browser_download_url"], f"{e}.apk")
        
    for e in otherAPKs:
        helperfunctions.downloadAPK(otherAPKs[e], f"{e}.apk")