def parse_input(input_file):
    grid = []
    start_pos = (None, None)
    with open(input_file, 'r') as f:
        for r, line in enumerate(f):
            row = []
            for c, item in enumerate(line.strip()):
                if item == "^":
                    start_pos = (r, c)
                row.append(item)
            grid.append(row)
    return grid, start_pos

def get_distinct_pos(input_file):
    grid, start_pos = parse_input(input_file)
    NROWS, NCOLS = len(grid), len(grid[0])
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    idx = 0
    visited = set()
    r, c = start_pos
    while 0 <= r < NROWS and 0<= c < NCOLS:
        if grid[r][c] == "#":
            # return to previous slot
            r -= directions[idx][0]
            c -= directions[idx][1]
            idx = (idx + 1) % 4
        else:
            visited.add((r, c))
            r += directions[idx][0]
            c += directions[idx][1]
    return len(visited)

if __name__ == "__main__":
    print(get_distinct_pos('./day6_test.txt'))
