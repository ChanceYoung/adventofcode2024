from adventofcode2024.utils.filereader import format_input

"""
Help the little elf with her word search

find all instances of XMAS
directions allowed:
horiziontal
vertical
diagonal
overlapping
backwards

"""

def puzzle1(data):
    twodimarray = []
    for row in data:
        twodimarray.append(list(row))
    return count_xmas(twodimarray)

def count_xmas(grid):
    directions = [
        (0, 1), (0, -1), (1, 0), (-1, 0),
        (1, 1), (-1, -1), (1, -1), (-1, 1)
    ]
    word = "XMAS"
    word_length = len(word)
    rows, cols = len(grid), len(grid[0])
    count = 0

    def is_within_bounds(x, y):
        return 0 <= x < rows and 0 <= y < cols

    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == word[0]:  # Check only if first letter matches
                for dx, dy in directions:
                    found = True
                    for i in range(word_length):
                        nx, ny = row + i * dx, col + i * dy
                        if not is_within_bounds(nx, ny) or grid[nx][ny] != word[i]:
                            found = False
                            break
                    if found:
                        count += 1

    return count

def puzzle2(data):
    twodimarray = []
    for row in data:
        twodimarray.append(list(row))
    return count_mas_in_x(twodimarray)

def count_mas_in_x(grid):
    rows, cols = len(grid), len(grid[0])
    count = 0

    def is_within_bounds(x, y):
        """Check if coordinates are within grid bounds."""
        return 0 <= x < rows and 0 <= y < cols

    def matches_mas_or_sam(cells):
        """Check if the given cells match 'MAS' or 'SAM'."""
        return cells == ['M', 'A', 'S'] or cells == ['S', 'A', 'M']

    for r in range(rows):
        for c in range(cols):
            # Check if the current cell is a valid center for an "X"
            if (is_within_bounds(r - 1, c - 1) and is_within_bounds(r + 1, c + 1) and
                is_within_bounds(r - 1, c + 1) and is_within_bounds(r + 1, c - 1) and
                grid[r][c] == 'A' and
                matches_mas_or_sam([grid[r - 1][c - 1], grid[r][c], grid[r + 1][c + 1]]) and
                matches_mas_or_sam([grid[r - 1][c + 1], grid[r][c], grid[r + 1][c - 1]])):
                count += 1

    return count




data = format_input('../day4/input.txt',None,True)
pz1_results = puzzle1(data)
print(pz1_results)
pz2_results = puzzle2(data)
print(pz2_results)