# RareFinder
![Screenshot 2024-04-01 200852](https://github.com/DARKSTONE-LABS/RareFinder/assets/141037846/d538ca0b-65e2-4dd7-8221-21fff994d64f)

RareFinder is a Python application with a graphical user interface (GUI) built using Tkinter. It allows users to download directories containing JSON files from a specified base URL and then search for specific keywords within those JSON files.

## Features

- **Step 1: Download Directories**: Users can specify the base URL, main folder name, download delay, and directory size to download directories containing JSON files.
- **Step 2: Search Keywords**: After downloading directories, users can search for specific keywords within the JSON files.
- **Select Directory**: Users can manually select a directory to search for keywords.
- **Console Output**: The application provides a console where users can see the progress of downloads and search results.

## Usage

1. **Step 1: Download Directories**
   - Enter the base URL where directories containing JSON files are located.
   - Specify the main folder name where downloaded directories will be saved.
   - Set the download delay in seconds (optional).
   - Enter the desired directory size.
   - Click on the "Step 1: Download Directories" button to start the download process.

2. **Step 2: Search Keywords**
   - Enter keywords separated by commas.
   - Click on the "Step 2: Search Keywords" button to start the search process.
   - The application will display the search results in the console.

3. **Select Directory**
   - Click on the "Select Directory" button to manually choose a directory to search for keywords.

## Requirements

- Python 3.x
- Tkinter (Python GUI library)
- Requests (HTTP library)
- JSON (JavaScript Object Notation) library

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/DARKSTONE-LABS/RareFinder.git
   ```
2. Install the required dependencies:
   ```
   pip install requests
   ```
3. Run the application:
   ```
   cd RareFinder
   python rarefind.py
   ```

## Contribution

Contributions are welcome! If you encounter any issues or have suggestions for improvement, please feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
