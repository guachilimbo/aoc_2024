def parse_input(file_dir):
    xword = []
    with open(file_dir, "r") as f:
        for line in f:
            xword.append([c for c in line.strip()])
    return xword


def traverse_grid(grid):
    def _is_valid(row, col, direction):
        dr, dc = direction
        xmas = "XMAS"
        for i in range(len(xmas)):
            nr = row + dr * i
            nc = col + dc * i
            if not (0 <= nr < nrows and 0 <= nc < ncols) or grid[nr][nc] != xmas[i]:
                return False
        return True
    
    nrows = len(grid)
    ncols = len(grid[0])
    _moves = [(0, 1), (0, -1), (1, 0), (-1, 0), (-1, -1), (-1, 1), (1, 1), (1, -1)]
    count = 0
    for r in range(nrows):
        for c in range(ncols):
            for direction in _moves:
                if _is_valid(r, c, direction):
                    count += 1
    return count

def find_mas(grid):
    def is_xmas(row, col):
        tl = (row - 1, col - 1)
        tr = (row - 1, col + 1)
        bl = (row + 1, col - 1)
        br = (row + 1, col + 1)
        for r, c in [tl, tr, bl, br]:
            if not (0 <= r < nrows and 0 <= c < ncols):
                return False
        if not (grid[tl[0]][tl[1]] == "M" and grid[br[0]][br[1]] == "S" or grid[tl[0]][tl[1]] == "S" and grid[br[0]][br[1]] == "M"):
            return False
        if not (grid[tr[0]][tr[1]] == "M" and grid[bl[0]][bl[1]] == "S" or grid[tr[0]][tr[1]] == "S" and grid[bl[0]][bl[1]] == "M"):
            return False
        return True
    nrows = len(grid)
    ncols = len(grid[0])
    count = 0   
    for r in range(nrows):
        for c in range(ncols):
            if grid[r][c] == "A":
                if is_xmas(r,c):
                    count += 1
    return count


if __name__ == "__main__":
    grid = parse_input(r".\day4_input.txt")
    print(traverse_grid(grid))
    assert find_mas(grid=parse_input(r".\day4_test.txt")) == 9
    print(find_mas(grid))