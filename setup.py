import os
import shutil
import tkinter as tk
from tkinter import messagebox, filedialog

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

def main():
    base_path = os.path.dirname(os.path.abspath(__file__))

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
        source_esp = os.path.join(base_path, "Data", "scripts", "EldenRingArrowInTheKnee.esp")
        destination_esp = os.path.join(install_dir_skyrim, "Data", "EldenRingArrowInTheKnee.esp")
        
        source_config = os.path.join(base_path, "Data", "scripts", "config.txt")
        destination_config = os.path.join(install_dir_skyrim, "Data", "config.txt")
        
        source_music = os.path.join(base_path, "audio")
        destination_music = os.path.join(install_dir_skyrim, "Data", "Music", "arrow to the knee 1.0")

        # Debug information
        print(f"source_esp: {source_esp}")
        print(f"destination_esp: {destination_esp}")
        print(f"source_config: {source_config}")
        print(f"destination_config: {destination_config}")
        print(f"source_music: {source_music}")

        # Check if the source files exist
        if not os.path.exists(source_esp):
            messagebox.showerror("Error", f"File not found: {source_esp}")
            return
        if not os.path.exists(source_config):
            messagebox.showerror("Error", f"File not found: {source_config}")
            return
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
        source_scripts_elden_ring = os.path.join(base_path, "Data", "scripts")
        # MOD NAME FOR ELDEN RING MOD FOLDER, NEEDS UPDATING w/ NEW VER: VER1.0 released 01-02-2025
        destination_scripts_elden_ring = os.path.join(install_dir_elden_ring, "mods", "arrow to the knee 1.0")

        # Debug information
        print(f"source_scripts_elden_ring: {source_scripts_elden_ring}")
        print(f"destination_scripts_elden_ring: {destination_scripts_elden_ring}")

        # Check if the source Lua scripts exist
        if not os.path.exists(source_scripts_elden_ring):
            messagebox.showerror("Error", f"Directory not found: {source_scripts_elden_ring}")
            return

        # Copy Lua scripts to Elden Ring's mod directory
        copy_files(source_scripts_elden_ring, destination_scripts_elden_ring)

        messagebox.showinfo("Installation", "Setup completed successfully!")

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
