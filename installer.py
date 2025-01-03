import os
import shutil
import sys
import tkinter as tk
from tkinter import messagebox, filedialog

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except AttributeError:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

def copy_files(src, dest):
    if not os.path.exists(dest):
        os.makedirs(dest)
    for item in os.listdir(src):
        s = os.path.join(src, item)
        d = os.path.join(dest, item)
        if os.path.isdir(s):
            shutil.copytree(s, d, dirs_exist_ok=True)
        else:
            shutil.copy2(s, d)

def main():
    def select_skyrim_dir():
        path = filedialog.askdirectory(initialdir="/", title="Select Skyrim Install Directory (e.g., C:\\Program Files (x86)\\Steam\\steamapps\\common\\Skyrim)")
        skyrim_dir_entry.delete(0, tk.END)
        skyrim_dir_entry.insert(0, path)

    def select_elden_ring_dir():
        path = filedialog.askdirectory(initialdir="/", title="Select Elden Ring Install Directory (e.g., C:\\Program Files (x86)\\Steam\\steamapps\\common\\ELDEN RING)")
        elden_ring_dir_entry.delete(0, tk.END)
        elden_ring_dir_entry.insert(0, path)

    def show_context_menu(event, entry):
        context_menu = tk.Menu(root, tearoff=0)
        context_menu.add_command(label="Copy", command=lambda: root.clipboard_append(entry.get()))
        context_menu.add_command(label="Paste", command=lambda: entry.insert(tk.END, root.clipboard_get()))
        context_menu.add_command(label="Clear", command=lambda: entry.delete(0, tk.END))
        context_menu.post(event.x_root, event.y_root)

    def install():
        install_dir_skyrim = skyrim_dir_entry.get()
        install_dir_elden_ring = elden_ring_dir_entry.get()

        if not install_dir_skyrim or not install_dir_elden_ring:
            messagebox.showerror("Error", "Please select both install directories.")
            return

        # Define source and destination directories for Skyrim
        source_esp = resource_path("Data/scripts/EldenRingArrowInTheKnee.esp")
        destination_esp = os.path.join(install_dir_skyrim, "Data", "EldenRingArrowInTheKnee.esp")
        
        source_config = resource_path("Data/scripts/config.txt")
        destination_config = os.path.join(install_dir_skyrim, "Data", "config.txt")
        
        source_music = resource_path("audio")
        destination_music = os.path.join(install_dir_skyrim, "Data", "Music", "arrow to the knee 1.0")

        # Check if the source files exist
        print(f"Checking existence of {source_esp}")
        if not os.path.exists(source_esp):
            messagebox.showerror("Error", f"File not found: {source_esp}")
            return
        print(f"Checking existence of {source_config}")
        if not os.path.exists(source_config):
            messagebox.showerror("Error", f"File not found: {source_config}")
            return
        print(f"Checking existence of {source_music}")
        if not os.path.exists(source_music):
            messagebox.showerror("Error", f"Directory not found: {source_music}")
            return

        # Copy ESP file to Skyrim's Data directory
        shutil.copy2(source_esp, destination_esp)
        
        # Copy config file to Skyrim's Data directory
        shutil.copy2(source_config, destination_config)
        
        # Copy music files to Skyrim's Data/Music directory
        copy_files(source_music, destination_music)
        
        # Define source and destination directories for Elden Ring

        # Arrow to the knee hit detection
        source_arrow_knee_detection_lua = resource_path("E:\\Files\\elden ring - arrow to the knee mod\\Arrow_to_the_Knee\\scripts\\elden_ring\\Arrow_knee_detection.lua")
        destination_arrow_knee_detection_lua = os.path.join(install_dir_elden_ring, "mods", "arrow to the knee 1.0", "Arrow_knee_detection.lua")
        
        source_arrow_knee_detection_luac = resource_path("E:\\Files\\elden ring - arrow to the knee mod\\Arrow_to_the_Knee\\scripts\\elden_ring\\Arrow_knee_detection.luac")
        destination_arrow_knee_detection_luac = os.path.join(install_dir_elden_ring, "mods", "arrow to the knee 1.0", "Arrow_knee_detection.luac")
        
        # Save_management 
        source_save_management_lua = resource_path("E:\\Files\\elden ring - arrow to the knee mod\\Arrow_to_the_Knee\\scripts\\elden_ring\\Save_management.lua")
        destination_save_management_lua = os.path.join(install_dir_elden_ring, "mods", "arrow to the knee 1.0", "Save_management.lua")
        
        source_save_management_luac = resource_path("E:\\Files\\elden ring - arrow to the knee mod\\Arrow_to_the_Knee\\scripts\\elden_ring\\Save_management.luac")
        destination_save_management_luac = os.path.join(install_dir_elden_ring, "mods", "arrow to the knee 1.0", "Save_management.luac")
        
        # Skyrim_transition
        source_skyrim_transition_lua = resource_path("E:\\Files\\elden ring - arrow to the knee mod\\Arrow_to_the_Knee\\scripts\\elden_ring\\Skyrim_transition.lua")
        destination_skyrim_transition_lua = os.path.join(install_dir_elden_ring, "mods", "arrow to the knee 1.0", "Skyrim_transition.lua")
        
        source_skyrim_transition_luac = resource_path("E:\\Files\\elden ring - arrow to the knee mod\\Arrow_to_the_Knee\\scripts\\elden_ring\\Skyrim_transition.luac")
        destination_skyrim_transition_luac = os.path.join(install_dir_elden_ring, "mods", "arrow to the knee 1.0", "Skyrim_transition.luac")

        # Check if the source Lua scripts and compiled Lua scripts exist
        print(f"Checking existence of {source_arrow_knee_detection_lua}")
        if not os.path.exists(source_arrow_knee_detection_lua):
            messagebox.showerror("Error", f"File not found: {source_arrow_knee_detection_lua}")
            return
        print(f"Checking existence of {source_arrow_knee_detection_luac}")
        if not os.path.exists(source_arrow_knee_detection_luac):
            messagebox.showerror("Error", f"File not found: {source_arrow_knee_detection_luac}")
            return
        print(f"Checking existence of {source_save_management_lua}")
        if not os.path.exists(source_save_management_lua):
            messagebox.showerror("Error", f"File not found: {source_save_management_lua}")
            return
        print(f"Checking existence of {source_save_management_luac}")
        if not os.path.exists(source_save_management_luac):
            messagebox.showerror("Error", f"File not found: {source_save_management_luac}")
            return
        print(f"Checking existence of {source_skyrim_transition_lua}")
        if not os.path.exists(source_skyrim_transition_lua):
            messagebox.showerror("Error", f"File not found: {source_skyrim_transition_lua}")
            return
        print(f"Checking existence of {source_skyrim_transition_luac}")
        if not os.path.exists(source_skyrim_transition_luac):
            messagebox.showerror("Error", f"File not found: {source_skyrim_transition_luac}")
            return

        # Ensure destination directories exist
        os.makedirs(os.path.dirname(destination_arrow_knee_detection_lua), exist_ok=True)
        os.makedirs(os.path.dirname(destination_arrow_knee_detection_luac), exist_ok=True)
        os.makedirs(os.path.dirname(destination_save_management_lua), exist_ok=True)
        os.makedirs(os.path.dirname(destination_save_management_luac), exist_ok=True)
        os.makedirs(os.path.dirname(destination_skyrim_transition_lua), exist_ok=True)
        os.makedirs(os.path.dirname(destination_skyrim_transition_luac), exist_ok=True)

        # Copy Lua scripts to Elden Ring's mod directory
        shutil.copy2(source_arrow_knee_detection_lua, destination_arrow_knee_detection_lua)
        shutil.copy2(source_arrow_knee_detection_luac, destination_arrow_knee_detection_luac)
        shutil.copy2(source_save_management_lua, destination_save_management_lua)
        shutil.copy2(source_save_management_luac, destination_save_management_luac)
        shutil.copy2(source_skyrim_transition_lua, destination_skyrim_transition_lua)
        shutil.copy2(source_skyrim_transition_luac, destination_skyrim_transition_luac)

        messagebox.showinfo("Installation", "Setup completed successfully!")
        root.destroy()  # Close the Tkinter window

    # GUI setup
    root = tk.Tk()
    root.title("Elden Ring x Skyrim Crossover Mod Installer")

    # Requirement message
    requirement_message = (
        "This mod requires both Skyrim Legendary Edition (LE) and Elden Ring installed to work properly.\n\n"
        "Common install locations:\n"
        "Skyrim LE: C:\\Program Files (x86)\\Steam\\steamapps\\common\\Skyrim\n"
        "Elden Ring: C:\\Program Files (x86)\\Steam\\steamapps\\common\\ELDEN RING"
    )
    tk.Label(root, text=requirement_message, wraplength=500, justify="left").grid(row=0, column=0, columnspan=3, padx=10, pady=10)

    tk.Label(root, text="Skyrim Install Directory:").grid(row=1, column=0, padx=10, pady=10)
    skyrim_dir_entry = tk.Entry(root, width=50)
    skyrim_dir_entry.grid(row=1, column=1, padx=10, pady=10)
    tk.Button(root, text="Browse", command=select_skyrim_dir).grid(row=1, column=2, padx=10, pady=10)
    skyrim_dir_entry.bind("<Button-3>", lambda event: show_context_menu(event, skyrim_dir_entry))

    tk.Label(root, text="Elden Ring Install Directory:").grid(row=2, column=0, padx=10, pady=10)
    elden_ring_dir_entry = tk.Entry(root, width=50)
    elden_ring_dir_entry.grid(row=2, column=1, padx=10, pady=10)
    tk.Button(root, text="Browse", command=select_elden_ring_dir).grid(row=2, column=2, padx=10, pady=10)
    elden_ring_dir_entry.bind("<Button-3>", lambda event: show_context_menu(event, elden_ring_dir_entry))

    tk.Button(root, text="Install", command=install).grid(row=3, column=0, columnspan=3, pady=20)

    root.mainloop()

if __name__ == "__main__":
    main()
