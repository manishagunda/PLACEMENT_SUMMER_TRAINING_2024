def find_area(i, j, n, a):
    # If out of bounds or the cell is not land, return 0
    if i < 0 or i >= n or j < 0 or j >= n or a[i][j] != 1:
        return 0
    
    # Mark the cell as visited
    a[i][j] = '0'
    
    # Initialize area
    area = 1
    
    # Recursively find area of the island
    area += find_area(i-1, j, n, a)  # Up
    area += find_area(i+1, j, n, a)  # Down
    area += find_area(i, j-1, n, a)  # Left
    area += find_area(i, j+1, n, a)  # Right
    
    return area

def count_islands_and_max_area(a):
    n = len(a)
    num_islands = 0
    max_area = 0
    
    for i in range(n):
        for j in range(n):
            if a[i][j] == 1:
                num_islands += 1
                current_area = find_area(i, j, n, a)
                max_area = max(max_area, current_area)
    
    return num_islands, max_area

# Input grid
a = [
    [0, 1, 0, 0, 1],
    [1, 0, 0, 1, 1],
    [0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0],
    [1, 0, 0, 0, 1]
]

# Count the number of islands and find the maximum area
num_islands, max_area = count_islands_and_max_area(a)
print(f"Number of islands: {num_islands}")
print(f"Maximum area of an island: {max_area}")
