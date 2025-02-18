from UI import Line, Point, Window


class Cell:
    def __init__(self, x1, x2, y1, y2, window: Window = None):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2
        self._win: Window = window
        self.visited = False

    def draw(self):
        if not self._win:
            return
        x1, x2, y1, y2 = self._x1, self._x2, self._y1, self._y2
        left_line = Line(Point(x1, y1), Point(x1, y2))
        self._win.draw_line(left_line, "black" if self.has_left_wall else "white")
        right_line = Line(Point(x2, y1), Point(x2, y2))
        self._win.draw_line(right_line, "black" if self.has_right_wall else "white")
        bot_line = Line(Point(x1, y2), Point(x2, y2))
        self._win.draw_line(bot_line, "black" if self.has_bottom_wall else "white")
        top_line = Line(Point(x1, y1), Point(x2, y1))
        self._win.draw_line(top_line, "black" if self.has_top_wall else "white")

    def draw_move(self, to_cell, undo=False):
        x1 = (self._x1 + self._x2) // 2
        y1 = (self._y1 + self._y2) // 2
        x2 = (to_cell._x1 + to_cell._x2) // 2
        y2 = (to_cell._y1 + to_cell._y2) // 2
        line = Line(Point(x1, y1), Point(x2, y2))
        if not self._win:
            return
        self._win.draw_line(line, "red" if undo else "gray")
