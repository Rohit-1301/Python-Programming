import os

file_path = r"C:\Users\rg975\OneDrive\Desktop\python programming\file\this.txt"

if os.path.exists(file_path):
    try:
        with open(file_path, 'r') as f:
            content = f.read()
            print(content)
    except IOError as e:
        print(f"An error occurred while reading the file: {e}")
else:
    print(f"The file {file_path} does not exist.")

