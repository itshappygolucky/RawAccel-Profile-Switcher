import pystray
import subprocess
import os
from PIL import Image
from pystray import MenuItem as item
from functools import partial

def on_set_curve(profile, *args, **kwargs):
    """Generalized function to run writer.exe with a given profile"""
    profile_path = f"C:\\RawAccel\\profiles\\{profile}.json"
    subprocess.call(["C:\\RawAccel\\writer.exe", profile_path])
    print(f"profile: {profile} profile paths: {profile_path}")

def on_quit(icon, item):
    """Quit function to stop the icon"""
    icon.visible = False
    icon.stop()

# Folder path where profiles are stored
dir_path = r'C:\\RawAccel\\profiles\\'

# List to store the profile names (without extensions)
res = [file for file in os.listdir(dir_path) if os.path.isfile(os.path.join(dir_path, file))]
lst = [os.path.splitext(file)[0] for file in res]  # Stripping file extensions

num_of_profiles = len(res)
print(f"Found {num_of_profiles} profiles: {lst}")

if __name__ == "__main__":
    # Load the icon image
    image = Image.open("icon.png")

    # Create the menu items dynamically based on the number of profiles
    menu_items = [item(profile, partial(on_set_curve, profile)) for profile in lst]

    # Add the 'Quit' item to the menu
    menu_items.append(item('Quit', on_quit))

    # Create the tray icon with the dynamically generated menu
    menu = tuple(menu_items)
    icon = pystray.Icon("RA Switcher", image, "RA Switcher", menu)
    
    # Run the icon (blocking call)
    icon.run()
