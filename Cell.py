class Cell(object):
    def __init__(self, x, y, size):
        self._x = x
        self._y = y
        self._size = size
        self._live = False
        self._next = False

    def check_collision(self, x, y):
        return self.x < x < self.x + self._size and self.y < y < self.y + self._size

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, x):
        self._x = x

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, y):
        self._y = y

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, size):
        self._size = size

    @property
    def live(self):
        return self._live

    @live.setter
    def live(self, live):
        self._live = live

    @property
    def next(self):
        return self._next

    @next.setter
    def next(self, next_live):
        self._next = next_live
