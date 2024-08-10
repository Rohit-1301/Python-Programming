import os

file_path = r"C:\Users\rg975\OneDrive\Desktop\python programming\file\this.txt"
st = "Hello everyone I am learning python programming language"

if os.path.exists(file_path):
    try:
        with open(file_path, 'w') as f:
            f.write(st)
        print(f"Successfully wrote: {st}")
    except IOError as e:
        print(f"An error occurred while writing to the file: {e}")
else:
    print(f"The file {file_path} does not exist.")

