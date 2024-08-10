def rat(array_2d, rows, cols, srow, scol):
    # Check for invalid starting point
    if srow >= rows or scol >= cols or srow < 0 or scol < 0:
        return 0
    # Check if the current position is out of bounds or already visited
    elif srow < 0 or scol < 0:
        return 0
    # Check if the end is reached
    elif srow == rows - 1 and scol == cols - 1:
        return 1
    # Check if the cell is blocked (True)
    elif array_2d[srow][scol] == True:
        return 0
    
    # Mark the cell as visited
    array_2d[srow][scol] = True
    
    # Recursively explore all possible directions
    ways = (rat(array_2d, rows, cols, srow + 1, scol) +
            rat(array_2d, rows, cols, srow, scol + 1) +
            rat(array_2d, rows, cols, srow - 1, scol) +
            rat(array_2d, rows, cols, srow, scol - 1))
    
    # Unmark the cell (backtrack)
    array_2d[srow][scol] = False
    
    return ways

# Step 1: Get the dimensions of the array from the user
rows = int(input("Enter the number of rows: "))
cols = int(input("Enter the number of columns: "))

# Step 2: Initialize a 2D array with False values
array_2d = [[False for _ in range(cols)] for _ in range(rows)]
print("the total no of paths is",rat(array_2d,rows,cols,0,0));

# Print the 2D array

