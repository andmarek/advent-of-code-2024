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


def get_x_mas_count(puzzle_input):
    """
    Look for the below:
    M.S
    .A.
    M.S

    or

    S.S
    .A.
    M.M

    or

    S.M
    .A.
    S.M
    """

    for i in range(len(puzzle_input)):
        for j in range(len(puzzle_input[0])):
            # right
            if puzzle_input[i][j] == "M":
                # check for diagonal MAS right
                pass

                # check for left if A below
            if puzzle_input[i][j] == "S":
                # check for diagonal SAM right
                pass

    return puzzle_input


def part2():
    with open("example.txt", "r") as f:
        d = f.read()

    puzzle_input = d.lower().splitlines()

    return get_x_mas_count(puzzle_input)


def main():
    print("Part 1: ", part1())
    print("Part 2: ", part2())


main()
