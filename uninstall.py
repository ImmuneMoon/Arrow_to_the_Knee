import os
import shutil
import tkinter as tk
from tkinter import messagebox
import winreg
import logging

# Configure logging
logging.basicConfig(filename='uninstaller_log.txt', level=logging.DEBUG, format='%(asctime)s - %(asctime)s - %(levelname)s - %(message)s')

def find_steam_library():
    try:
        key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\WOW6432Node\Valve\Steam")
        steam_path, _ = winreg.QueryValueEx(key, "InstallPath")
        winreg.CloseKey(key)
        
        libraries_path = os.path.join(steam_path, "steamapps", "libraryfolders.vdf")
        if os.path.exists(libraries_path):
            with open(libraries_path, 'r') as file:
                for line in file:
                    if "path" in line:
                        path = line.split('"')[3]
                        return os.path.join(path, "steamapps", "common")
        return os.path.join(steam_path, "steamapps", "common")
    except Exception as e:
        logging.error(f"Error finding Steam library: {e}")
        return None

def find_game_directory(game_name):
    steam_library_path = find_steam_library()
    if steam_library_path:
        game_path = os.path.join(steam_library_path, game_name)
        if os.path.exists(game_path):
            return game_path
    return None

def remove_path(path):
    if os.path.exists(path):
        if os.path.isfile(path) or os.path.islink(path):
            os.remove(path)
            logging.debug(f'Removed file: {path}')
        elif os.path.isdir(path):
            shutil.rmtree(path)
            logging.debug(f'Removed directory: {path}')
    else:
        logging.debug(f'File or directory not found: {path}')

def main():
    skyrim_dir = find_game_directory("Skyrim")
    elden_ring_mods_dir = os.path.join(find_game_directory("ELDEN RING"), "mods")

    def uninstall():
        confirm = messagebox.askyesno("Uninstall", "Do you want to uninstall the mod and remove the files?")
        if confirm:
            # Define paths to the files and directories to be removed
            mod_folder_elden_ring = os.path.join(elden_ring_mods_dir, "arrow to the knee 1.0")
            esp_file_skyrim = os.path.join(skyrim_dir, "Data", "EldenRingArrowInTheKnee.esp")
            config_file_skyrim = os.path.join(skyrim_dir, "Data", "config.txt")
            music_folder_skyrim = os.path.join(skyrim_dir, "Data", "Music", "arrow to the knee 1.0")

            # Remove files and directories
            remove_path(mod_folder_elden_ring)
            remove_path(esp_file_skyrim)
            remove_path(config_file_skyrim)
            remove_path(music_folder_skyrim)

            messagebox.showinfo("Uninstallation", "Uninstallation completed successfully!")
            root.destroy()  # Close the Tkinter window

    # GUI setup
    root = tk.Tk()
    root.title("Elden Ring x Skyrim Crossover Mod Uninstaller")

    tk.Label(root, text="Click 'Uninstall' to remove the mod files.").grid(row=0, column=0, padx=10, pady=10)
    tk.Button(root, text="Uninstall", command=uninstall).grid(row=1, column=0, padx=10, pady=10)

    root.mainloop()

if __name__ == "__main__":
    main()
