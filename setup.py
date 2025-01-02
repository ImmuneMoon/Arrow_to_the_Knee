import os
import shutil
import zipfile
import subprocess
import urllib.request
import tarfile
import tkinter as tk
from tkinter import messagebox, filedialog

def download_file(url, dest):
    print(f"Downloading {url} to {dest}...")
    try:
        urllib.request.urlretrieve(url, dest)
        return True
    except Exception as e:
        print(f"Download failed: {e}")
        return False

def extract_zip_file(zip_path, extract_to):
    print(f"Extracting {zip_path}...")
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(extract_to)

def manual_install_prompt(message):
    print(message)
    while True:
        user_input = input("Press 'C' to continue after manual installation: ").strip().lower()
        if user_input == 'c':
            break

def install_skse(skyrim_path):
    skse_url = "http://skse.silverlock.org/download/skse64_2_00_19.7z"  # Update this URL to the latest version
    skse_zip_path = "skse.7z"
    skse_extract_path = "skse"

    # Attempt to download SKSE
    if not download_file(skse_url, skse_zip_path):
        manual_install_prompt("Please manually download SKSE from http://skse.silverlock.org and place the .7z file in the current directory.")

    # Extract SKSE
    extract_zip_file(skse_zip_path, skse_extract_path)

    # Copy SKSE files to Skyrim directory
    skse_files = ['skse64_loader.exe', 'skse64_steam_loader.dll', 'skse64_2_00_19.dll']
    for file in skse_files:
        shutil.copy2(os.path.join(skse_extract_path, file), skyrim_path)

def install_lua():
    lua_url = "https://www.lua.org/ftp/lua-5.4.3.tar.gz"
    lua_tar_path = "lua.tar.gz"
    lua_extract_path = "lua"

    # Attempt to download Lua
    if not download_file(lua_url, lua_tar_path):
        manual_install_prompt("Please manually download Lua from https://www.lua.org and place the .tar.gz file in the current directory.")

    # Extract Lua
    with tarfile.open(lua_tar_path, "r:gz") as tar:
        tar.extractall(path=lua_extract_path)

    # Build and install Lua (requires make and gcc)
    os.chdir(os.path.join(lua_extract_path, "lua-5.4.3"))
    subprocess.run(["make", "windows"])
    subprocess.run(["make", "install"])

def copy_files(src, dest):
    if not os.path.exists(dest):
        os.makedirs(dest)
    for item in os.listdir(src):
        s = os.path.join(src, item)
        d = os.path.join(dest, item)
        if os.path.isdir(s):
            shutil.copytree(s, d, False, None)
        else:
            shutil.copy2(s, d)

def extract_zip(src, dest):
    with zipfile.ZipFile(src, 'r') as zip_ref:
        zip_ref.extractall(dest)

def update_scripts(install_dir):
    # Check if update is needed
    update_needed = messagebox.askyesno("Update Scripts", "Do you want to update the scripts?")
    if update_needed:
        # Define source and destination directories for Skyrim
        source_scripts_skyrim = os.path.join("scripts", "skyrim_LE")
        destination_scripts_skyrim = os.path.join(install_dir, "Skyrim", "Scripts")
        
        source_zip_skyrim = os.path.join("Data", "Scripts", "Source.zip")
        destination_source_skyrim = os.path.join(install_dir, "Skyrim", "Scripts", "Source")
        
        # Copy compiled scripts to Skyrim's directory
        copy_files(source_scripts_skyrim, destination_scripts_skyrim)

        # Extract source zip to Skyrim's directory
        extract_zip(source_zip_skyrim, destination_source_skyrim)
        
        messagebox.showinfo("Update Scripts", "Skyrim scripts updated successfully!")
    else:
        messagebox.showinfo("Update Scripts", "Skipping script update.")

def run_skyrim_launcher(skyrim_path):
    skse_loader_path = os.path.join(skyrim_path, "skse_loader.exe")
    skyrim_launcher_path = os.path.join(skyrim_path, "SkyrimLauncher.exe")

    if os.path.exists(skse_loader_path):
        print("Launching Skyrim with SKSE...")
        subprocess.run([skse_loader_path])
    else:
        print("SKSE not found. Launching Skyrim normally...")
        subprocess.run([skyrim_launcher_path])

def main():

    def select_skyrim_dir():
        path = filedialog.askdirectory(initialdir="/", title="Select Skyrim Install Directory")
        skyrim_dir_entry.delete(0, tk.END)
        skyrim_dir_entry.insert(0, path)

    def select_elden_ring_dir():
        path = filedialog.askdirectory(initialdir="/", title="Select Elden Ring Install Directory")
        elden_ring_dir_entry.delete(0, tk.END)
        elden_ring_dir_entry.insert(0, path)

    def install():
        install_dir_skyrim = skyrim_dir_entry.get()
        install_dir_elden_ring = elden_ring_dir_entry.get()

        if not install_dir_skyrim or not install_dir_elden_ring:
            messagebox.showerror("Error", "Please select both install directories.")
            return

        # Install SKSE
        install_skse(install_dir_skyrim)

        # Install Lua
        install_lua()

        # Define source and destination directories for Skyrim
        source_esp = os.path.join("Data", "EldenRingArrowInTheKnee.esp")
        destination_esp = os.path.join(install_dir_skyrim, "EldenRingArrowInTheKnee.esp")
        
        source_config = os.path.join("Data", "config.txt")
        destination_config = os.path.join(install_dir_skyrim, "config.txt")
        
        source_music = os.path.join("audio")
        destination_music = os.path.join(install_dir_skyrim, "Music", "YourMod")

        # Copy ESP file to Skyrim's directory
        shutil.copy2(source_esp, destination_esp)
        
        # Copy config file to Skyrim's directory
        shutil.copy2(source_config, destination_config)
        
        # Copy music files to Skyrim's Music directory
        copy_files(source_music, destination_music)
        
        # Define source and destination directories for Elden Ring
        source_scripts_elden_ring = os.path.join("scripts", "elden_ring")
        destination_scripts_elden_ring = os.path.join(install_dir_elden_ring, "mods", "YourMod")

        # Copy Lua scripts to Elden Ring's mod directory
        copy_files(source_scripts_elden_ring, destination_scripts_elden_ring)

        # Update scripts if needed
        update_scripts(install_dir_skyrim)

        # Run Skyrim Launcher
        run_skyrim_launcher(install_dir_skyrim)
        
        messagebox.showinfo("Installation", "Setup completed successfully!")

    # GUI setup
    root = tk.Tk()
    root.title("Elden Ring x Skyrim Crossover Mod Installer")

    tk.Label(root, text="Skyrim Install Directory:").grid(row=0, column=0, padx=10, pady=10)
    skyrim_dir_entry = tk.Entry(root, width=50)
    skyrim_dir_entry.grid(row=0, column=1, padx=10, pady=10)
    tk.Button(root, text="Browse", command=select_skyrim_dir).grid(row=0, column=2, padx=10, pady=10)

    tk.Label(root, text="Elden Ring Install Directory:").grid(row=1, column=0, padx=10, pady=10)
    elden_ring_dir_entry = tk.Entry(root, width=50)
    elden_ring_dir_entry.grid(row=1, column=1, padx=10, pady=10)
    tk.Button(root, text="Browse", command=select_elden_ring_dir).grid(row=1, column=2, padx=10, pady=10)

    tk.Button(root, text="Install", command=install).grid(row=2, column=0, columnspan=3, pady=20)

    root.mainloop()

if __name__ == "__main__":
    main()
