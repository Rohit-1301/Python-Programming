# Writing to a file
file_path = r"C:\Users\rg975\OneDrive\Desktop\python programming\file\example.txt"
with open("file_path", "w") as f:
    f.write("Hello, world!\n")
    f.writelines(["This is the first line.\n", "This is the second line.\n"])

# Reading the entire content of the file
with open(file_path, "r") as f:
    content = f.read()
    print("Reading the entire content:")
    print(content)


# Reading the file line by line
with open(file_path, "r") as f:
    print("Reading line by line:")
    for line in f:
        print(line, end='')

# Reading lines into a list
with open(file_path, "r") as f:
    lines = f.readlines()
    print("\nReading lines into a list:")
    print(lines)

# Appending to a file
with open(file_path, "a") as f:
    f.write("This is an appended line.\n")

# Reading the modified file content
with open(file_path, "r") as f:
    print("Reading the modified file content:")
    print(f.read())
