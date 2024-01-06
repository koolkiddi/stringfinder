# DB String Checker

## Description
DB String Checker is a Python script designed for fast and efficient searching of specific strings within a set of databases, regardless of file extensions. This script is particularly useful for those handling large amounts of data and needing a quick, reliable method to locate specific information within these files.

## Features
- Searches for strings across multiple database files.
- Supports various file types with extension-independent searching.
- Option to perform case-sensitive searches.
- Displays results in the console with highlighted search terms.
- Saves results to a text file for later reference.

## How It Works
The script recursively traverses the specified directory, searching for the requested terms in each file. Results are displayed in real-time in the console with highlighted matching strings and are also saved to a text file.

## Prerequisites
- Python 3.x
- Python Modules: `os`, `re`, `colorama`, `multiprocessing`

## Installation
1. Ensure Python 3.x is installed on your system.
2. Clone the repository or download the script `db_string_checker.py`.
3. Install necessary dependencies by running `pip install colorama`.

## Configuration
To use the script, you need to set the paths to your database folder and the folder where you want to save the results. Modify the `search_path` and `save_path` variables in the script:

```python
# Configuration des chemins
search_path = "path/to/your/database"
save_path = "path/to/output/folder"
```

## Usage
Run the script in your terminal or command prompt:

```bash
Copy code
python db_string_checker.py
```

Follow the on-screen instructions to enter search terms and other options.
