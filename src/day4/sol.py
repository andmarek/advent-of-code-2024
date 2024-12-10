XMAS = "xmas"
SAMX = XMAS[::-1]


def search_horizontal(lines) -> int:
    count = 0
    for line in lines:
        for i in range(len(line) - len(XMAS) + 1):
            window = line[i : i + len(XMAS)]
            if window == XMAS or window == SAMX:
                count += 1
    return count


def search_vertical(lines) -> int:
    cols = []
    for c in range(len(lines[0])):
        col = ""
        for r in range(len(lines)):
            col += lines[r][c]
        cols.append(col)
    return search_horizontal(cols)


def search_diagonal_right(lines) -> int:
    rows, cols = len(lines), len(lines[0])
    count = 0
    for c in range(cols):
        diag = ""
        r, col = 0, c
        while r < rows and col < cols:
            diag += lines[r][col]
            r += 1
            col += 1
        count += search_horizontal([diag])

    for r in range(1, rows):
        diag = ""
        row, c = r, 0
        while row < rows and c < cols:
            diag += lines[row][c]
            row += 1
            c += 1
        count += search_horizontal([diag])
    return count


def search_diagonal_left(lines) -> int:
    rows, cols = len(lines), len(lines[0])
    count = 0
    for c in range(cols):
        diag = ""
        r, col = 0, c
        while r < rows and col >= 0:
            diag += lines[r][col]
            r += 1
            col -= 1
        count += search_horizontal([diag])

    for r in range(1, rows):
        diag = ""
        row, c = r, cols - 1
        while row < rows and c >= 0:
            diag += lines[row][c]
            row += 1
            c -= 1
        count += search_horizontal([diag])
    return count


def part1():
    with open("input.txt", "r") as f:
        d = f.read()
    puzzle_input = d.lower().splitlines()

    count = (
        search_horizontal(puzzle_input)
        + search_vertical(puzzle_input)
        + search_diagonal_right(puzzle_input)
        + search_diagonal_left(puzzle_input)
    )
    return count


def get_x_mas_count(grid):
    rows = len(grid)
    cols = len(grid[0])
    count = 0
    for row in range(1, rows-1):
        for col in range(1, cols-1):
            if grid[row][col] != 'a':
                continue

            tl = grid[row-1][col-1]
            tr = grid[row-1][col+1]
            bl = grid[row+1][col-1]
            br = grid[row+1][col+1]

            left_diagonal = "".join([tl, grid[row][col], br])
            right_diagonal = "".join([tr, grid[row][col], bl])

            if left_diagonal in ["mas", "sam"] and right_diagonal in ["mas", "sam"]:
                count += 1
    return count


def part2():
    with open("input.txt", "r") as f:
        d = f.read()

    puzzle_input = d.lower().splitlines()

    return get_x_mas_count(puzzle_input)


def main():
    print("Part 1: ", part1())
    print("Part 2: ", part2())


main()
