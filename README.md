# DiskAnalyzer

DiskAnalyzer is a Python program that analyzes disk usage and reports on space consumption by different files and folders in Windows.

## Features

- Recursively calculates the size of directories and files.
- Provides a sorted report of files and directories by size.
- Displays sizes in a human-readable format (B, KB, MB, GB, TB, PB).

## Requirements

- Python 3.6 or higher

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/DiskAnalyzer.git
   ```
2. Navigate to the directory:
   ```bash
   cd DiskAnalyzer
   ```

## Usage

Run the script using the command line by specifying the path of the directory or file you want to analyze:

```bash
python DiskAnalyzer.py <path>
```

Replace `<path>` with the path to the directory or file you want to analyze.

Example:

```bash
python DiskAnalyzer.py C:\Users\YourName\Documents
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please submit a pull request or open an issue to discuss improvements or new features.