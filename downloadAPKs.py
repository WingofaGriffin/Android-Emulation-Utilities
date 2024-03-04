import requests
import os
import helperfunctions
import adbutils
import nethersx2patch

githubAPKs = {
    "obtanium": "ImranR98/Obtainium",
    "citra": "citra-emu/citra-nightly",
    "yuzu": "yuzu-emu/yuzu-android",
    "vita3k": "Vita3K/Vita3K-Android",
    "melonds": "rafaelvcaetano/melonDS-android",
    "flycast": "flyinghead/flycast",
    "skyemu": "skylersaleh/SkyEmu",
}

otherAPKs = {
    "retroarch": "https://buildbot.libretro.com/nightly/android/RetroArch.apk",
}

gplayAPKs = {
    "daijisho": "com.magneticchen.daijishou",
    "dolphin": "org.dolphinemu.dolphinemu",
    "duckstation": "com.github.stenzek.duckstation",
    "ppsspp": "org.ppsspp.ppsspp",
    "snes9xex": "com.explusalpha.Snes9xPlus",
    "yabasanshiro": "org.devmiyax.yabasanshioro2",
    "m64plusfz": "org.mupen64plusae.v3.fzurita",
    "redream": "io.recompiled.redream",
    "scummvm": "org.scummvm.scummvm",
}

def downloadAPKs():
    # Install Retroarch First
    for e in otherAPKs:
        print("Installing Retroarch...")
        helperfunctions.downloadAPK(otherAPKs[e], f"{e}.apk")

    for e in githubAPKs:
        print(f"Would you like to install {e}? y/n (default yes)")
        install = input()
        if install != "n":
            latestRelease=helperfunctions.getLatestGithubURL(githubAPKs[e])
            helperfunctions.downloadAPK(latestRelease["browser_download_url"], f"{e}.apk")

def installPlayStore(device):
    for app in gplayAPKs:
        helperfunctions.openPlayStoreApp(gplayAPKs[app], device)

def downloadScript():
    try:
        downloadAPKs()
        nethersx2patch.patchNether()
    except:
        print("APK downloads failed. Check your internet connection and try again.")
        quit()
    else:
        print("APKs downloaded locally.")