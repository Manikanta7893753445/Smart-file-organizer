from file_utils import organize

if __name__ == "__main__":
    path = input("Enter folder path: ").strip()
    count = organize(path)
    print(f"Organized {count} files.")
