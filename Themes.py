import os
import time
import random

# Directory where your wallpaper images are stored
wallpaper_dir = "/home/ghost/Pictures/Themes"

# List all image files in the wallpaper directory
wallpapers = [os.path.join(wallpaper_dir, f) for f in os.listdir(wallpaper_dir) if os.path.isfile(os.path.join(wallpaper_dir, f))]

# Function to change wallpaper
def change_wallpaper():
    wallpaper = random.choice(wallpapers)
    os.system(f"feh --bg-fill {wallpaper}")

# Time interval between wallpaper changes (in seconds)
change_interval = 60 #* 30  # Change wallpaper every 30 minutes

# Main loop
while True:
    change_wallpaper()
    time.sleep(change_interval)
