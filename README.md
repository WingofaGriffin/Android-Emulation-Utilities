# Android Emulation Utilities

A simple to use python script to install popular emulators on your Android device.

## Prerequisites

* [Python 3](https://www.python.org/downloads/)
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

## "Installation"

This is not an app that is designed to be installed on your device. Instead, I suggest downloading this project to a temporary location on your computer (such as the Downloads folder). You can either directly download this git directory, or grab the zip from the [releases folder](https://github.com/WingofaGriffin/Android-Emulation-Utilities/releases/latest).

## Usage

Install all python dependencies with pip, then run `main.py` in python. For most users, this will look like the following:

```sh
cd Android-Emulation-Utilities
pip install -r requirements.txt
python main.py
```
