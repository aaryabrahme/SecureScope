from scanner.scanner import FileScanner


def main():

    scanner = FileScanner("sample_data")

    files = scanner.discover_files()

    print("\nScanning completed.\n")

    for file in files:
        print(f"✓ {file}")

    print(f"\nTotal files found: {len(files)}")


if __name__ == "__main__":
    main()