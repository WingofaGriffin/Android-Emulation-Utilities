import requests
import os
import helperfunctions
import adbutils

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
    "PPSSPP": "org.ppsspp.ppsspp",
    "Snes9x EX+": "com.explusalpha.Snes9xPlus",
    "Yaba Sanshiro": "org.devmiyax.yabasanshioro2",
    "M64Plus FZ": "org.mupen64plusae.v3.fzurita",
    "Redream": "io.recompiled.redream",

}

def downloadAPKs():
    for e in githubAPKs:
        latestRelease=helperfunctions.getLatestGithubURL(githubAPKs[e])
        helperfunctions.downloadAPK(latestRelease["browser_download_url"], f"{e}.apk")
        
    for e in otherAPKs:
        helperfunctions.downloadAPK(otherAPKs[e], f"{e}.apk")

def installPlayStore(device):
    for app in gplayAPKs:
        helperfunctions.openPlayStoreApp(gplayAPKs[app], device)