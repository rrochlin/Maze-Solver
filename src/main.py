from maze import Maze
from UI import Window


def main():
    """
    cells = [
        Cell(x, x + 50, y, y + 50, win)
        for x in range(0, 800, 50)
        for y in range(0, 800, 50)
    ]
    for cell in cells:
        cell.has_left_wall = randint(0, 3) == 0
        cell.has_right_wall = randint(0, 3) == 0
        cell.has_top_wall = randint(0, 3) == 0
        cell.has_bottom_wall = randint(0, 3) == 0
        cell.draw()
    """
    num_rows = 12
    num_cols = 16
    margin = 50
    screen_x = 800
    screen_y = 600
    cell_size_x = (screen_x - 2 * margin) // num_cols
    cell_size_y = (screen_y - 2 * margin) // num_rows
    win = Window(screen_x, screen_y)

    maze = Maze(margin, margin, num_rows, num_cols, cell_size_x, cell_size_y, win)
    maze.solve()
    win.wait_for_close()


if __name__ == "__main__":
    main()
