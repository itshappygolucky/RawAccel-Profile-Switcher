import pystray
import pywintypes
import win32api
import win32con
import subprocess
import os
from PIL import Image
from pystray import MenuItem as item

## Project based off: https://www.youtube.com/watch?v=Vrg4RhjxztE
## How the executes work https://stackoverflow.com/questions/1811691/running-an-outside-program-executable-in-python

def on_set_curveA():
    subprocess.call(Curve1, shell=True)  

def on_set_curveB():
    subprocess.call(Curve2, shell=True)  

def on_set_curveC():
    subprocess.call(Curve3, shell=True) 

def on_set_curveD():
    subprocess.call(Curve4, shell=True) 

def on_quit():
    icon.visible = False
    icon.stop()

## Stores Files into List / Array ot whatever https://pynative.com/python-list-files-in-a-directory/

# folder path
dir_path = r'C:\\RawAccel\\profiles\\'

# list to store files
res = []

for path in os.listdir(dir_path):
    # check if current path is a file
    if os.path.isfile(os.path.join(dir_path, path)):
        res.append(path)
print(res)

## Takes the filetype off the end, and makes a new list https://stackoverflow.com/questions/27750611/how-can-i-strip-the-file-extension-from-a-list-full-of-filenames
lst = [os.path.splitext(x)[0] for x in res]
print(lst)

numOfProfiles = len(res)
print(numOfProfiles)

if __name__ == "__main__":
    image = Image.open("icon.png")

    if numOfProfiles == 4:
        ## making the profile locations
        profile1 = '"C:\\RawAccel\\profiles\\' + res[0] + '"'
        profile2 = '"C:\\RawAccel\\profiles\\' + res[1] + '"'
        profile3 = '"C:\\RawAccel\\profiles\\' + res[2] + '"'
        profile4 = '"C:\\RawAccel\\profiles\\' + res[3] + '"'

        ## this is what goes into the target box
        Curve1 = 'C:\RawAccel\writer.exe ' + profile1
        Curve2 = 'C:\RawAccel\writer.exe ' + profile2
        Curve3 = 'C:\RawAccel\writer.exe ' + profile3
        Curve4 = 'C:\RawAccel\writer.exe ' + profile4

        menu = (
            item(lst[0], lambda: on_set_curveA()), 
            item(lst[1], lambda: on_set_curveB()),
            item(lst[2], lambda: on_set_curveC()),
            item(lst[3], lambda: on_set_curveD()),
            item('Quit', on_quit)
            )   

    if numOfProfiles == 3:
        profile1 = '"C:\\RawAccel\\profiles\\' + res[0] + '"'
        profile2 = '"C:\\RawAccel\\profiles\\' + res[1] + '"'
        profile3 = '"C:\\RawAccel\\profiles\\' + res[2] + '"'

        Curve1 = 'C:\RawAccel\writer.exe ' + profile1
        Curve2 = 'C:\RawAccel\writer.exe ' + profile2
        Curve3 = 'C:\RawAccel\writer.exe ' + profile3
        menu = (
            item(lst[0], lambda: on_set_curveA()), 
            item(lst[1], lambda: on_set_curveB()),
            item(lst[2], lambda: on_set_curveC()),
            item('Quit', on_quit)
        )

    if numOfProfiles == 2:
        profile1 = '"C:\\RawAccel\\profiles\\' + res[0] + '"'
        profile2 = '"C:\\RawAccel\\profiles\\' + res[1] + '"'

        Curve1 = 'C:\RawAccel\writer.exe ' + profile1
        Curve2 = 'C:\RawAccel\writer.exe ' + profile2
        menu = (
            item(lst[0], lambda: on_set_curveA()), 
            item(lst[1], lambda: on_set_curveB()),
            item('Quit', on_quit)
        )
        
    if numOfProfiles == 1:
        profile1 = '"C:\\RawAccel\\profiles\\' + res[0] + '"'

        Curve1 = 'C:\RawAccel\writer.exe ' + profile1
        menu = (
            item(lst[0], lambda: on_set_curveA()), 
            item('Quit', on_quit)
        )

    icon = pystray.Icon("RA Switcher", image, "RA Switcher", menu)
    icon.run()