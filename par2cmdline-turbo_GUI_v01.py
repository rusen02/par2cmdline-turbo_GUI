import tkinter as tk
from tkinter import filedialog, messagebox
import subprocess
import os

class Par2GUI:
    def __init__(self, root):
        self.root = root
        self.root.title("PAR2 GUI")

        self.file_list = []

        # Radio buttons for selecting operation
        self.operation_var = tk.StringVar()
        self.operation_var.set("c")  # Default to Create
        self.create_radio = tk.Radiobutton(root, text="Create", variable=self.operation_var, value="c")
        self.create_radio.pack(anchor=tk.W)
        self.verify_radio = tk.Radiobutton(root, text="Verify", variable=self.operation_var, value="v")
        self.verify_radio.pack(anchor=tk.W)
        self.repair_radio = tk.Radiobutton(root, text="Repair", variable=self.operation_var, value="r")
        self.repair_radio.pack(anchor=tk.W)

        # Create file listbox
        self.file_listbox = tk.Listbox(root, selectmode=tk.MULTIPLE, width=50)
        self.file_listbox.pack(pady=10)

        # Buttons
        self.add_button = tk.Button(root, text="Add Files", command=self.add_files)
        self.add_button.pack(pady=5)

        self.run_button = tk.Button(root, text="Run par2", command=self.run_par2)
        self.run_button.pack(pady=5)

    def add_files(self):
        files = filedialog.askopenfilenames(title="Select files", filetypes=[("All Files", "*.*")])
        for file in files:
            self.file_listbox.insert(tk.END, file)
            self.file_list.append(file)

    def run_par2(self):
        if not self.file_list:
            messagebox.showerror("Error", "No files selected.")
            return

        # Get directory of the script
        script_dir = os.path.dirname(os.path.realpath(__file__))
        par2_path = os.path.join(script_dir, "par2.exe")

        # Construct par2 command
        command = [par2_path, self.operation_var.get()]

        # Add options here if needed

        # Add PAR2 file and files to command
        par2_file = "recovery.par2"
        command.append(par2_file)
        command.extend(self.file_list)

        # Run par2
        try:
            subprocess.run(command, check=True)
            messagebox.showinfo("Success", "Operation completed successfully.")
        except subprocess.CalledProcessError as e:
            messagebox.showerror("Error", f"Operation failed: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = Par2GUI(root)
    root.mainloop()
