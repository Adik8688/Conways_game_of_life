import pygame
from Cell import Cell

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
CELL_SIZE = 10
WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 700


class Game:
    def __init__(self):
        self.window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

        self.cells = []
        for x in range(0, WINDOW_HEIGHT, CELL_SIZE):
            self.cells.append([Cell(y, x, CELL_SIZE) for y in range(0, WINDOW_WIDTH, CELL_SIZE)])

    def initialize_game(self, delay, mode):
        run = True
        while run:
            if self.isQuit():
                run = False
            if pygame.mouse.get_pressed()[0] or pygame.mouse.get_pressed()[2]:
                for row in self.cells:
                    for cell in row:
                        if cell.check_collision(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]):
                            cell.live = True if pygame.mouse.get_pressed()[0] else False

            if pygame.key.get_pressed()[pygame.K_SPACE]:
                run = False
            self.draw(mode)
            self.update(delay)

    def run_game(self, delay):
        run = True
        while run:
            if self.isQuit():
                run = False
            self.count_neighbours()
            self.survived()
            self.draw()
            self.update(delay)

    @staticmethod
    def isQuit():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True

    def draw(self, mode=0):
        self.window.fill(BLACK)

        for row in self.cells:
            for cell in row:
                color = WHITE if cell.live else BLACK
                pygame.draw.rect(self.window, color, (cell.x, cell.y, cell.size, cell.size))

        if mode == 1:
            self.draw_lines(self.window)

    @staticmethod
    def update(delay):
        pygame.display.update()
        pygame.time.delay(delay)
        pygame.time.Clock().tick(60)

    @staticmethod
    def draw_lines(window):
        for i in range(CELL_SIZE, 1000, CELL_SIZE):
            pygame.draw.line(window, (192, 192, 192), (i, 0), (i, 700))
        for i in range(CELL_SIZE, 700, CELL_SIZE):
            pygame.draw.line(window, (192, 192, 192), (0, i), (1000, i))

    def survived(self):
        for x, _ in enumerate(self.cells):
            for y, _ in enumerate(self.cells[0]):
                self.cells[x][y].live = self.cells[x][y].next

    def count_neighbours(self):
        for x, _ in enumerate(self.cells):
            for y, c in enumerate(self.cells[x]):
                n = 0
                for x1 in range(3):
                    for y1 in range(3):
                        if 0 <= x - 1 + x1 < len(self.cells) and 0 <= y - 1 + y1 < len(self.cells[0]) and \
                                not (x1 == 1 and y1 == 1):
                            n = n + 1 if self.cells[x - 1 + x1][y - 1 + y1].live else n

                if c.live:
                    c.next = n == 2 or n == 3
                else:
                    c.next = n == 3
