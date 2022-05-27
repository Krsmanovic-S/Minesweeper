import random
from constants import *


class Board:
    def __init__(self):
        # Two fields, one stores mines and the mine count,
        # other one stores which cells are opened/not opened.
        self._covered_cells = [[False for _ in range(10)] for _ in range(10)]
        self._field = [[0 for _ in range(10)] for _ in range(10)]

        # Variables
        self.game_over = False
        self.first_move = True
        self.opened_cells = 0
        self.mine_count = 20
        self._flagged_positions = {}

    @staticmethod
    def draw_rect(window, fill_color, outline_color, rect, border=1.5):
        window.fill(outline_color, rect)
        window.fill(fill_color, rect.inflate(-border * 2, -border * 2))

    def draw_grid(self, window):
        for i in range(10):
            for j in range(10):
                cell = pygame.Rect(j * 100, i * 100, CELL_SIZE, CELL_SIZE)
                position = (j * 100, i * 100)

                if not self._covered_cells[i][j]:
                    self.draw_rect(window, GRAY, BORDER, cell)

                    if self._field[i][j] == 10:
                        window.blit(FLAG, position)
                else:
                    window.blit(DRAWING[self._field[i][j]], position)

    def play_first_move(self, mouse):
        x, y = mouse[1] // 100, mouse[0] // 100

        if self._field[x][y] != 10:
            self._covered_cells[x][y] = True
            self.opened_cells += 1

            self.randomize_mines((x, y))

            for i in range(x - 1, x + 2):
                for j in range(y - 1, y + 2):
                    self.flood_fill(i, j)

    def place_flag(self, mouse):
        # Places and removes flags from the grid,
        # uses a dictionary to store previous grid value.
        x, y = mouse[1] // 100, mouse[0] // 100

        if not self._covered_cells[x][y]:
            if (x, y) not in self._flagged_positions:
                self._flagged_positions[(x, y)] = self._field[x][y]

                if self._field[x][y] == 9:
                    self.opened_cells += 1

                self._field[x][y] = 10
            else:
                self._field[x][y] = self._flagged_positions[(x, y)]

                if self._field[x][y] == 9:
                    self.opened_cells -= 1

                del self._flagged_positions[(x, y)]

    def open_cell(self, mouse):
        x, y = mouse[1] // 100, mouse[0] // 100

        if self._field[x][y] == 9:
            self.open_all_mines()

        if not self._covered_cells[x][y] and self._field[x][y] != 10:
            self._covered_cells[x][y] = True
            self.opened_cells += 1

            for i in range(x - 1, x + 2):
                for j in range(y - 1, y + 2):
                    self.flood_fill(i, j)

    def open_all_mines(self):
        # When you click on a mine, it will show
        # all of them and the game will be over.
        for i in range(10):
            for j in range(10):
                if self._field[i][j] == 9:
                    self._covered_cells[i][j] = True
                elif self._field[i][j] == 10:
                    if self._flagged_positions[(i, j)] == 9:
                        self._field[i][j] = 9
                        self._covered_cells[i][j] = True

        self.game_over = True

    def flood_fill(self, x, y):
        # Algorithm that will open cells around the one
        # we clicked if that cell isn't a flag/mine/already explored.
        if x < 0 or x > 9:
            return
        if y < 0 or y > 9:
            return

        if self._field[x][y] != 9 and not self._field[x][y] == 10 \
           and not self._covered_cells[x][y]:
            self._covered_cells[x][y] = True
            self.opened_cells += 1

            if self._field[x][y] == 0:
                self.flood_fill(x + 1, y)
                self.flood_fill(x - 1, y)
                self.flood_fill(x, y + 1)
                self.flood_fill(x, y - 1)

    def randomize_mines(self, clicked_position):
        for i in range(self.mine_count, -1, -1):
            x = random.randint(0, 9)
            y = random.randint(0, 9)
            if self._field[x][y] == 9 or (x, y) == clicked_position:
                i += 1
            else:
                self._field[x][y] = 9

        # For each cell, count the number of mines around
        # it and put the matching number in that field position.
        for i in range(0, 10):
            for j in range(0, 10):
                if self._field[i][j] != 9:
                    self._field[i][j] = self.count_mines(i, j)

    def count_mines(self, x, y):
        mines_around = 0

        for i in range(x - 1, x + 2):
            for j in range(y - 1, y + 2):
                if 0 <= i < 10 and 0 <= j < 10:
                    if self._field[i][j] == 9:
                        mines_around += 1

        return mines_around

    def reset(self):
        self._field = [[0 for _ in range(10)] for _ in range(10)]
        self._covered_cells = [[False for _ in range(10)] for _ in range(10)]

        self.game_over = False
        self.first_move = True
        self.opened_cells = 0
