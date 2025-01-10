

def make_grid(rows:int, cols:int)->list[list]: 
    grid = []
    for x in range(rows): 
        row = []
        for y in range(cols):
            row.append("*")
        grid.append(row)
    return grid 

assert make_grid(2,2) == [['*', '*'], ['*', '*']]

# there's also an analytic solution to this, almost certainly 
# but I'm on the computer, so computational here we go 
# okay no this is brute force and taking too long 
# def count_paths_to_bottom_right(grid: list[list], row: int = 0, col: int = 0) -> int:
#     rows, cols = len(grid), len(grid[0])
    
#     if row == rows - 1 and col == cols - 1:
#         return 1
    
#     if row >= rows or col >= cols:
#         return 0
    
#     down_paths = count_paths_to_bottom_right(grid, row + 1, col)
#     right_paths = count_paths_to_bottom_right(grid, row, col + 1)
    
#     return down_paths + right_paths

def count_paths_to_bottom_right_memo(grid: list[list], row: int = 0, col: int = 0, memo: dict = {}) -> int:
    rows, cols = len(grid), len(grid[0])
    
    if (row, col) in memo:
        return memo[(row, col)]
    
    if row == rows - 1 and col == cols - 1:
        return 1
    
    if row >= rows or col >= cols:
        return 0
    
    down_paths = count_paths_to_bottom_right_memo(grid, row + 1, col, memo)
    right_paths = count_paths_to_bottom_right_memo(grid, row, col + 1, memo)
    
    memo[(row, col)] = down_paths + right_paths
    
    return memo[(row, col)]


print(count_paths_to_bottom_right_memo(make_grid(21,21)))