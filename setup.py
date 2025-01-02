import os
import shutil
import platform
import zipfile
import subprocess
import urllib.request
import tarfile

def download_file(url, dest):
    print(f"Downloading {url} to {dest}...")
    urllib.request.urlretrieve(url, dest)

def extract_zip_file(zip_path, extract_to):
    print(f"Extracting {zip_path}...")
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(extract_to)

def install_skse(skyrim_path):
    skse_url = "http://skse.silverlock.org/download/skse_1_07_03.7z"
    skse_zip_path = "skse.7z"
    skse_extract_path = "skse"

    # Download SKSE
    download_file(skse_url, skse_zip_path)
    
    # Extract SKSE
    extract_zip_file(skse_zip_path, skse_extract_path)

    # Copy SKSE files to Skyrim directory
    skse_files = ['skse_loader.exe', 'skse_steam_loader.dll', 'skse_1_9_32.dll']
    for file in skse_files:
        shutil.copy2(os.path.join(skse_extract_path, file), skyrim_path)

def install_lua():
    lua_url = "https://www.lua.org/ftp/lua-5.4.3.tar.gz"
    lua_tar_path = "lua.tar.gz"
    lua_extract_path = "lua"

    # Download Lua
    download_file(lua_url, lua_tar_path)

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
    update_needed = input("Do you want to update the scripts? (y/n): ").lower()
    if update_needed == 'y':
        # Define source and destination directories for Skyrim
        source_scripts_skyrim = os.path.join("scripts", "skyrim_LE")
        destination_scripts_skyrim = os.path.join(install_dir, "Skyrim", "Scripts")
        
        source_zip_skyrim = os.path.join("Data", "Scripts", "Source.zip")
        destination_source_skyrim = os.path.join(install_dir, "Skyrim", "Scripts", "Source")
        
        # Copy compiled scripts to Skyrim's directory
        copy_files(source_scripts_skyrim, destination_scripts_skyrim)

        # Extract source zip to Skyrim's directory
        extract_zip(source_zip_skyrim, destination_source_skyrim)
        
        print("Skyrim scripts updated successfully!")
    else:
        print("Skipping script update.")

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
    # Prompt user for Skyrim install directory
    install_dir_skyrim = input("Please enter your Skyrim install directory (default: C:\\Program Files (x86)\\Steam\\steamapps\\common\\Skyrim): ")
    if not install_dir_skyrim:
        install_dir_skyrim = "C:\\Program Files (x86)\\Steam\\steamapps\\common\\Skyrim"
    
    # Prompt user for Elden Ring install directory
    install_dir_elden_ring = input("Please enter your Elden Ring install directory (default: C:\\Program Files (x86)\\Steam\\steamapps\\common\\Elden Ring): ")
    if not install_dir_elden_ring:
        install_dir_elden_ring = "C:\\Program Files (x86)\\Steam\\steamapps\\common\\Elden Ring"

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
    
    print("Setup completed successfully!")

if __name__ == "__main__":
    main()
