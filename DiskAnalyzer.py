import os
import argparse

def get_size(start_path='.'):
    """Calculate the size of a directory or file."""
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(start_path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            if not os.path.islink(fp):
                total_size += os.path.getsize(fp)
    return total_size

def analyze_disk_usage(path):
    """Analyze the disk usage of the given directory."""
    if not os.path.exists(path):
        raise FileNotFoundError(f"The path {path} does not exist.")

    usage_report = []
    if os.path.isdir(path):
        for entry in os.scandir(path):
            entry_path = os.path.join(path, entry.name)
            entry_size = get_size(entry_path)
            usage_report.append((entry.name, entry_size))
    else:
        entry_size = os.path.getsize(path)
        usage_report.append((os.path.basename(path), entry_size))

    return sorted(usage_report, key=lambda x: x[1], reverse=True)

def format_size(size_bytes):
    """Convert a size in bytes to a more readable format."""
    for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
        if size_bytes < 1024:
            return f"{size_bytes:.2f} {unit}"
        size_bytes /= 1024
    return f"{size_bytes:.2f} PB"

def print_report(report):
    """Print the disk usage report."""
    print("Disk Usage Report:")
    for name, size in report:
        print(f"{name}: {format_size(size)}")

def main():
    parser = argparse.ArgumentParser(description="Analyze disk usage and report on space consumption by different files and folders in Windows.")
    parser.add_argument("path", type=str, help="Path of the directory or file to analyze")
    args = parser.parse_args()

    try:
        report = analyze_disk_usage(args.path)
        print_report(report)
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()