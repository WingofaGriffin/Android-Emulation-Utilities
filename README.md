# Android Emulation Utilities

A simple to use python script to install popular emulators on your Android device.

## Prerequisites

* [adb](https://developer.android.com/tools/releases/platform-tools#downloads)
    * Confirm that you have this before installing.
* An Android device of decent recency
    * I am not sure exactly which version is required, as all apps have different requirements.

## Supported Operating Systems

* MacOS
* Linux
* Windows (Untested)

This will **NOT** run on Android devices directly. You must connect it to a PC first.

## Important Notes

This is designed to be as unopinionated of an installation script as possible. There are no assumptions to settings for optimizing performance for your device, nor controls for those of you installing this on a gaming handheld. I assume you will want to customize those controls to your own desire based on how diverse and different the options on the market are from one another. As such, this has not been tested on any specific devices unless otherwise noted.

USE AT YOUR OWN RISK! While this script is fully open source and is easily reviewable, there is always a risk of your device not behaving as expected, especially with the large number of Android devices that are all configured slightly differently. I cannot guarantee your specific device is compatible.

## "Installation" and Usage

This is not an app that is designed to be installed on your device. Instead, I suggest downloading this project to a temporary location on your computer (such as the Downloads folder). You can either directly download this git directory, or grab the zip from the [releases folder](https://github.com/WingofaGriffin/Android-Emulation-Utilities/releases/latest).

Ensure that **ONLY** the desired Android device is connected to your computer and no Android emulators are running to ensure the correct device is targeted.

Install all python dependencies with pip, then run `main.py` in python. For most users, this will look like the following:

In MacOS and Linux, open your terminal and run something along the lines of"

```sh
cd ~/Downloads
git clone "https://github.com/WingofaGriffin/Android-Emulation-Utilities.git"
cd Android-Emulation-Utilities
pip install -r requirements.txt
python main.py
```
On Windows, open Command Prompt and run something along the following:

```powershell
cd "$HOME\Downloads"
git clone "https://github.com/WingofaGriffin/Android-Emulation-Utilities.git"
cd "Android-Emulation-Utilities"
py -m pip install -r requirements.txt
py main.py
```

## TODO and Future Additions

- Add a GUI
- RetroAchievements baked in
- More config optimizations for emulators
    - Setting up Save and Bios folders
- Test on gaming handhelds
- Test on Windows
- Better streamlined setup

## Special Thanks

- DragoonDoirse and the EmuDeck team
- https://github.com/RJNY/Obtainium-Emulation-Pack