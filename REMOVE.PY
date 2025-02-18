import os
import tkinter as tk
from tkinter import messagebox

def remove_files_from_user_folders(destination_folder):
    """
    Removes all files from each user folder in the destination folder.
    
    Parameters:
        destination_folder (str): Path to the folder containing the user folders.
    """
    # Get the list of user folders in the destination folder
    user_folders = [f for f in os.listdir(destination_folder) if os.path.isdir(os.path.join(destination_folder, f))]
    
    # If no user folders are found
    if not user_folders:
        messagebox.showwarning("No Folders", "No user folders found in the destination folder.")
        return
    
    # Iterate over each user folder and remove files inside
    for user_folder in user_folders:
        user_folder_path = os.path.join(destination_folder, user_folder)
        
        # List all files inside the user folder
        for file_name in os.listdir(user_folder_path):
            file_path = os.path.join(user_folder_path, file_name)
            
            if os.path.isfile(file_path):  # Make sure it's a file, not a directory
                try:
                    os.remove(file_path)  # Remove the file
                    print(f"Removed file '{file_name}' from user folder '{user_folder}'.")
                except Exception as e:
                    print(f"Failed to remove file '{file_name}' from user folder '{user_folder}': {e}")
            else:
                print(f"Skipping '{file_name}' as it is not a file.")
    
    messagebox.showinfo("Completed", "File removal completed from all user folders.")

# GUI for the script
def on_remove_files():
    destination_directory = folder_path_entry.get().strip()
    if not destination_directory:
        messagebox.showwarning("Input Error", "Please provide the destination folder path.")
        return
    
    # Call the function to remove files from user folders
    remove_files_from_user_folders(destination_directory)

# Create the main window
window = tk.Tk()
window.title("Remove Files from User Folders")

# Create and place widgets for the GUI
tk.Label(window, text="Destination Folder:").grid(row=0, column=0, padx=10, pady=10)
folder_path_entry = tk.Entry(window, width=50)
folder_path_entry.grid(row=0, column=1, padx=10, pady=10)

# Button to remove files
remove_button = tk.Button(window, text="Remove Files", command=on_remove_files, width=20)
remove_button.grid(row=1, column=0, columnspan=2, pady=20)

# Start the Tkinter event loop
window.mainloop()
