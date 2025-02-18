from tkinter import Canvas, Tk


class Window:
    def __init__(self, width, height):
        self.root = Tk()
        self.title = self.root.title
        self.canvas = Canvas(self.root, bg="white", width=width, height=height)
        self.canvas.pack()
        self.is_window_running = False
        self.root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self.root.update_idletasks()
        self.root.update()

    def wait_for_close(self):
        self.is_window_running = True
        while self.is_window_running:
            self.redraw()

    def close(self):
        self.is_window_running = False

    def draw_line(self, line, fill):
        line.draw(self.canvas, fill, 2)


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Line:
    def __init__(self, p1: Point, p2: Point):
        self.p1 = p1
        self.p2 = p2

    def draw(self, canvas: Canvas, fill: str = "black", width: int = 2):
        canvas.create_line(
            self.p1.x, self.p1.y, self.p2.x, self.p2.y, fill=fill, width=width
        )
