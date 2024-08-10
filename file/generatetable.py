import os

def generatetables(n):
    """
    This function generates a multiplication table of size n x n
    """
    table = ""

    for i in range(1, 11):
        table += f"{n} x {i} = {n * i}\n"

    # Correct the file path format
    file_path = os.path.join(r"C:\Users\rg975\OneDrive\Desktop\python programming\file\tables", f"table of {n}.txt")
    with open(file_path, "w") as f:
        f.write(table)

# Ensure the directory exists
os.makedirs(r"C:\Users\rg975\OneDrive\Desktop\python programming\file\tables", exist_ok=True)

for i in range(2, 21):
    generatetables(i)
