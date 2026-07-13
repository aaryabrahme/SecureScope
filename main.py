from scanner.scanner import FileScanner
from scanner.readers import read_file


def main():

    scanner = FileScanner("sample_data")

    files = scanner.discover_files()

    for file in files:

        print(f"\nReading: {file.name}")

        text = read_file(file)

        print(text)


if __name__ == "__main__":
    main()