import helperfunctions
import nethersx2patch

githubAPKs = {
    "obtanium": "ImranR98/Obtainium",
    "citra": "PabloMK7/citra",
    "vita3k": "Vita3K/Vita3K-Android",
    "melonds": "rafaelvcaetano/melonDS-android",
    "flycast": "flyinghead/flycast",
    "skyemu": "skylersaleh/SkyEmu",
    "sudachi": "sudachi-emu/sudachi",
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
    except Exception as ex:
        template = "An exception of type {0} occurred. Arguments:\n{1!r}"
        message = template.format(type(ex).__name__, ex.args)
        print(message)
        print("APK downloads failed. Check your internet connection and try again.")
        quit()
    else:
        print("APKs downloaded locally.")