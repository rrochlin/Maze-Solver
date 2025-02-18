import random
import time

from cell import Cell
from UI import Window


class Maze:
    def __init__(
        self,
        x1,
        y1,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        win: Window = None,
        seed=None,
    ):
        if seed:
            random.seed(seed)
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        self._create_cells()
        self._break_walls_r(0, 0)
        self._break_entrance_and_exit()
        self._reset_cells_visited()

    def _create_cells(self):
        self._cells = [
            [
                Cell(x, x + self.cell_size_x, y, y + self.cell_size_y, self.win)
                for y in range(
                    self.y1,
                    self.y1 + int(self.num_rows * self.cell_size_y),
                    int(self.cell_size_y),
                )
            ]
            for x in range(
                self.x1,
                self.x1 + int(self.num_cols * self.cell_size_x),
                int(self.cell_size_x),
            )
        ]
        self._draw_cell()

    def _draw_cell(self):
        for row in self._cells:
            for cell in row:
                if cell._win:
                    cell.draw()
        self._animate()

    def _animate(self):
        if self.win:
            self.win.redraw()
        time.sleep(0.03)

    def _break_entrance_and_exit(self):
        entrance: Cell = self._cells[0][0]
        exit: Cell = self._cells[-1][-1]
        entrance.has_top_wall = False
        entrance.draw()
        exit.has_bottom_wall = False
        exit.draw()
        self._animate()

    def _break_walls_r(self, i, j):
        self._cells[i][j].visited = True
        while True:
            temp = []
            if i > 0 and not self._cells[i - 1][j].visited:
                temp.append((-1, 0))
            if j > 0 and not self._cells[i][j - 1].visited:
                temp.append((0, -1))
            if i < len(self._cells) - 1 and not self._cells[i + 1][j].visited:
                temp.append((1, 0))
            if j < len(self._cells[0]) - 1 and not self._cells[i][j + 1].visited:
                temp.append((0, 1))
            if not temp:
                self._cells[i][j].draw()
                self._animate()
                return
            next_dir = random.choice(temp)
            next_cell: Cell = self._cells[i + next_dir[0]][j + next_dir[1]]
            current_cell: Cell = self._cells[i][j]

            if next_dir[0] == 1:
                current_cell.has_right_wall = False
                next_cell.has_left_wall = False
            elif next_dir[0] == -1:
                next_cell.has_right_wall = False
                current_cell.has_left_wall = False
            elif next_dir[1] == 1:
                current_cell.has_bottom_wall = False
                next_cell.has_top_wall = False
            else:
                current_cell.has_top_wall = False
                next_cell.has_top_wall = False

            self._animate()
            self._break_walls_r(i + next_dir[0], j + next_dir[1])

    def _reset_cells_visited(self):
        for row in self._cells:
            for cell in row:
                cell.visited = False

    def solve(self):
        return self._solve_r(0, 0)

    def _solve_r(self, i, j):
        self._animate()
        cell = self._cells[i][j]
        cell.visited = True
        if i == len(self._cells) - 1 and j == len(self._cells[0]) - 1:
            return True
        directions = [(1, 0), (-1, 0), (0, -1), (0, 1)]
        for d in directions:
            if (
                i + d[0] == len(self._cells)
                or i + d[0] < 0
                or j + d[1] == len(self._cells[0])
                or j + d[1] < 0
            ):
                continue
            if self._cells[i + d[0]][j + d[1]].visited:
                continue
            if (
                (d[0] == 1 and cell.has_right_wall)
                or (d[0] == -1 and cell.has_left_wall)
                or (d[1] == 1 and cell.has_bottom_wall)
                or (d[1] == -1 and cell.has_top_wall)
            ):
                continue
            next_cell = self._cells[i + d[0]][j + d[1]]
            cell.draw_move(next_cell)
            if self._solve_r(i + d[0], j + d[1]):
                return True
            cell.draw_move(next_cell, True)
        return False
