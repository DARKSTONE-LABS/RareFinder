import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
import os
import time
import requests
import json

class RareFinderGUI:
    def __init__(self, master):
        self.master = master
        master.title("Rare Finder")

        # Create widgets
        self.base_url_label = ttk.Label(master, text="Base URL:")
        self.base_url_entry = ttk.Entry(master, width=50)
        self.base_url_entry.insert(0, "https://we-assets.pinit.io/J2Q2j6kpSg7tq8JzueCHNTQNcyNnQkvr85RhsFnYZWeG/f7ac2fd2-13c4-4ca1-85ee-962772caf73e")

        self.main_folder_label = ttk.Label(master, text="Main Folder Name:")
        self.main_folder_entry = ttk.Entry(master, width=50)
        self.main_folder_entry.insert(0, "OutPut Folder")

        self.delay_label = ttk.Label(master, text="Download Delay (seconds):")
        self.delay_entry = ttk.Entry(master, width=10)
        self.delay_entry.insert(0, "0.0001")

        self.directory_size_label = ttk.Label(master, text="Directory Size:")
        self.directory_size_entry = ttk.Entry(master, width=10)
        self.directory_size_entry.insert(0, "4444")

        self.keywords_label = ttk.Label(master, text="Keywords (comma-separated):")
        self.keywords_entry = ttk.Entry(master, width=50)

        self.start_button = ttk.Button(master, text="Step 1: Download Directories", command=self.step1_download)
        self.search_button = ttk.Button(master, text="Step 2: Search Keywords", command=self.step2_search)
        self.select_directory_button = ttk.Button(master, text="Select Directory", command=self.select_directory)

        self.console_label = ttk.Label(master, text="Console:")
        self.console_text = tk.Text(master, width=80, height=20)

        # Grid layout
        self.base_url_label.grid(row=0, column=0, sticky="w")
        self.base_url_entry.grid(row=0, column=1, columnspan=2, padx=10, pady=5, sticky="ew")
        self.main_folder_label.grid(row=1, column=0, sticky="w")
        self.main_folder_entry.grid(row=1, column=1, columnspan=2, padx=10, pady=5, sticky="ew")
        self.delay_label.grid(row=2, column=0, sticky="w")
        self.delay_entry.grid(row=2, column=1, columnspan=2, padx=10, pady=5, sticky="ew")
        self.directory_size_label.grid(row=3, column=0, sticky="w")
        self.directory_size_entry.grid(row=3, column=1, columnspan=2, padx=10, pady=5, sticky="ew")
        self.keywords_label.grid(row=4, column=0, sticky="w")
        self.keywords_entry.grid(row=4, column=1, columnspan=2, padx=10, pady=5, sticky="ew")
        self.start_button.grid(row=5, column=0, columnspan=3, pady=10)
        self.search_button.grid(row=6, column=0, columnspan=3, pady=10)
        self.select_directory_button.grid(row=7, column=0, columnspan=3, pady=10)
        self.console_label.grid(row=8, column=0, sticky="w")
        self.console_text.grid(row=9, column=0, columnspan=3, padx=10, pady=5, sticky="ew")

    def step1_download(self):
        self.base_url = self.base_url_entry.get()
        self.main_folder = self.main_folder_entry.get()
        self.delay = float(self.delay_entry.get())
        self.directory_size = int(self.directory_size_entry.get())

        directories = {'': self.directory_size}  # Specified directory size

        for directory, count in directories.items():
            folder = os.path.join(self.main_folder, directory)
            if not os.path.exists(folder):
                os.makedirs(folder)

            for i in range(0, count + 1):
                url = f'{self.base_url}{directory}/{i}.json'
                self.download_json(url)

                time.sleep(self.delay)

        messagebox.showinfo("Information", "Directory download process completed.")
        self.search_button.config(state=tk.NORMAL)

    def download_json(self, url):
        try:
            response = requests.get(url)
            if response.status_code == 200:
                file_path = os.path.join(self.main_folder, f"{url.split('/')[-1]}")
                with open(file_path, 'wb') as file:
                    file.write(response.content)
            else:
                self.log(f"Failed to download JSON from {url}. Status code: {response.status_code}")
        except Exception as e:
            self.log(f"Error downloading JSON from {url}: {e}")

    def step2_search(self):
        keywords = [keyword.strip().lower() for keyword in self.keywords_entry.get().split(',')]
        results = []

        directory = self.main_folder_entry.get()
        if directory and os.path.exists(directory):
            self.log(f"Searching directory: {directory}")
            for root, dirs, files in os.walk(directory):
                for file in files:
                    if file.endswith(".json"):
                        file_path = os.path.join(root, file)
                        self.log(f"Searching file: {file_path}")
                        with open(file_path, 'r') as f:
                            try:
                                json_data = json.load(f)
                            except json.JSONDecodeError:
                                self.log(f"Error decoding JSON from file: {file_path}")
                                continue

                            if self.search_keywords_in_json(json_data, keywords):
                                results.append(file_path)

            if results:
                self.log("Search completed. Files found:")
                for result in results:
                    self.log(result)
                messagebox.showinfo("Information", "Search completed. Check console log for results.")
            else:
                self.log("No results found for specified keywords.")
                messagebox.showinfo("Information", "No results found for specified keywords.")
        else:
            self.log("Invalid directory. Please select a valid directory.")
            messagebox.showinfo("Information", "Invalid directory. Please select a valid directory.")

    def search_keywords_in_json(self, json_data, keywords):
        if isinstance(json_data, dict):
            for key, value in json_data.items():
                if isinstance(value, (dict, list)):
                    if self.search_keywords_in_json(value, keywords):
                        return True
                elif isinstance(value, str) and any(keyword.lower() in value.lower() for keyword in keywords):
                    return True
        elif isinstance(json_data, list):
            for item in json_data:
                if isinstance(item, (dict, list)):
                    if self.search_keywords_in_json(item, keywords):
                        return True
                elif isinstance(item, str) and any(keyword.lower() in item.lower() for keyword in keywords):
                    return True
        elif isinstance(json_data, str) and any(keyword.lower() in json_data.lower() for keyword in keywords):
            return True
        
        return False

    def select_directory(self):
        directory = filedialog.askdirectory()
        if directory:
            self.main_folder_entry.delete(0, tk.END)
            self.main_folder_entry.insert(0, directory)

    def log(self, message):
        self.console_text.insert(tk.END, message + "\n")
        self.console_text.see(tk.END)

def main():
    root = tk.Tk()
    app = RareFinderGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
