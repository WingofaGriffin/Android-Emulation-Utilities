import helperfunctions
import nethersx2patch

githubAPKs = {
    "obtanium (REQUIRED)": "ImranR98/Obtainium",
    "citra (3DS)": "PabloMK7/citra",
    "vita3k (Vita)": "Vita3K/Vita3K-Android",
    "melonds (NDS)": "rafaelvcaetano/melonDS-android",
    "flycast (Dreamcast)": "flyinghead/flycast",
    "skyemu (GB/GBC/GBA)": "skylersaleh/SkyEmu",
    "sudachi (Switch)": "sudachi-emu/sudachi",
}

otherAPKs = {
    "retroarch": "https://buildbot.libretro.com/nightly/android/RetroArch.apk",
}

gplayAPKs = {
    "daijisho (RECOMMENDED Frontend)": "com.magneticchen.daijishou",
    "dolphin (Gamecube and Wii)": "org.dolphinemu.dolphinemu",
    "duckstation (PS1)": "com.github.stenzek.duckstation",
    "ppsspp (PSP)": "org.ppsspp.ppsspp",
    "snes9xex (SNES)": "com.explusalpha.Snes9xPlus",
    "yabasanshiro (Saturn)": "org.devmiyax.yabasanshioro2",
    "m64plusfz (N64)": "org.mupen64plusae.v3.fzurita",
    "redream (Dreamcast)": "io.recompiled.redream",
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
        print(f"Would you like to install NetherSX2 (PS2)? y/n (default yes)")
        install = input()
        if install != "n":
            nethersx2patch.patchNether()
    except Exception as ex:
        template = "An exception of type {0} occurred. Arguments:\n{1!r}"
        message = template.format(type(ex).__name__, ex.args)
        print(message)
        print("APK downloads failed. Check your internet connection and try again.")
        quit()
    else:
        print("APKs downloaded locally.")