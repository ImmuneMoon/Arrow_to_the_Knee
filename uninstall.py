import os
import tkinter as tk
from tkinter import messagebox

def remove_file(path):
    if os.path.exists(path):
        os.remove(path)

def main():
    skyrim_dir = "C:\\Program Files (x86)\\Steam\\steamapps\\common\\Skyrim"
    elden_ring_dir = "C:\\Program Files (x86)\\Steam\\steamapps\\common\\ELDEN RING"

    def uninstall():
        confirm = messagebox.askyesno("Uninstall", "Do you want to uninstall the mod and remove the files?")
        if confirm:
            # Define paths to the files to be removed
            mod_file_elden_ring = os.path.join(elden_ring_dir, "mods", "arrow to the knee 1.0")
            esp_file_skyrim = os.path.join(skyrim_dir, "Data", "EldenRingArrowInTheKnee.esp")

            # Remove files
            remove_file(mod_file_elden_ring)
            remove_file(esp_file_skyrim)

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
