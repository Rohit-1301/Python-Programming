def multiply(array_2d, barray_2d, rows, cols, rowsb, colsb):
    # Step 1: Check for the validity of the input
    if cols != rowsb:
        print("Invalid input")
        return

    # Initialize the result array with zeros
    result = [[0 for _ in range(colsb)] for _ in range(rows)]

    # Perform matrix multiplication
    for i in range(rows):
        for j in range(colsb):
            for k in range(cols):  # or range(rowsb) since cols == rowsb
                result[i][j] += array_2d[i][k] * barray_2d[k][j]

    # Print the result array
    for row in result:
        print(" ".join(map(str, row)))


# Step 1: Initialize an empty 2D array
array_2d = []

# Step 2: Get the dimensions of the array from the user
rows = int(input("Enter the number of rows: "))
cols = int(input("Enter the number of columns: "))

# Step 3: Use nested loops to fill the 2D array with user input
for i in range(rows):
    row = []  # Create an empty row
    for j in range(cols):
        value = int(input(f"Enter value for element [{i}][{j}]: "))
        row.append(value)
    array_2d.append(row)

# Print the 2D array
for row in array_2d:
    print(row)


barray_2d = []

# Step 2: Get the dimensions of the array from the user
rowsb = int(input("Enter the number of rows: "))
colsb = int(input("Enter the number of columns: "))

# Step 3: Use nested loops to fill the 2D array with user input
for i in range(rowsb):
    row = []  # Create an empty row
    for j in range(colsb):
        value = int(input(f"Enter value for element [{i}][{j}]: "))
        row.append(value)
    barray_2d.append(row)

# Print the 2D array
for row in barray_2d:
    print(row)

print("The multiplication of the two matrices is: ")
multiply(array_2d,barray_2d,rows,cols,rowsb,colsb)
