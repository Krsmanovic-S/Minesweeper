import random
from constants import *


class Board:
    def __init__(self):
        self._covered_cells = [[False for _ in range(10)] for _ in range(10)]
        self._field = [[0 for _ in range(10)] for _ in range(10)]

        self.game_over = False
        self.opened_cells = 0
        self.mine_count = 20
        self._flagged_positions = {}

    @staticmethod
    def draw_rect(window, fill_color, outline_color, rect, border=1):
        window.fill(outline_color, rect)
        window.fill(fill_color, rect.inflate(-border * 2, -border * 2))

    def draw_grid(self, window):
        for i in range(10):
            for j in range(10):
                cell = pygame.Rect(j * 100, i * 100, 100, 100)

                # 0 is closed cell, 1 is opened cell
                if self._field[i][j] == 10:
                    self.draw_rect(window, GRAY, BORDER, cell, 2)
                    window.blit(FLAG, (j * 100, i * 100))
                elif not self._covered_cells[i][j]:
                    self.draw_rect(window, GRAY, BORDER, cell, 2)
                else:
                    if self._field[i][j] == 0:
                        self.draw_rect(window, OPENED, BORDER, cell, 2)
                    elif self._field[i][j] == 1:
                        window.blit(ONE, (j * 100, i * 100))
                    elif self._field[i][j] == 2:
                        window.blit(TWO, (j * 100, i * 100))
                    elif self._field[i][j] == 3:
                        window.blit(THREE, (j * 100, i * 100))
                    elif self._field[i][j] == 4:
                        window.blit(FOUR, (j * 100, i * 100))
                    elif self._field[i][j] == 5:
                        window.blit(FIVE, (j * 100, i * 100))
                    elif self._field[i][j] == 6:
                        window.blit(SIX, (j * 100, i * 100))
                    elif self._field[i][j] == 7:
                        window.blit(SEVEN, (j * 100, i * 100))
                    elif self._field[i][j] == 8:
                        window.blit(EIGHT, (j * 100, i * 100))
                    else:
                        self.draw_rect(window, RED, BORDER, cell, 2)
                        window.blit(MINE, (j * 100, i * 100))

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

    def randomize_mines(self):
        # Randomly distribute the mines on the field,
        # how much depends on the mine_count variable.
        for i in range(self.mine_count, -1, -1):
            x = random.randint(0, 9)
            y = random.randint(0, 9)
            if self._field[x][y] == 9:
                i += 1
            else:
                self._field[x][y] = 9

        # Now for each cell, count the number of mines around
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

    def open_cell(self, mouse):
        x, y = mouse[1] // 100, mouse[0] // 100

        if self._field[x][y] == 9:
            self.open_all_mines()

        if not self._covered_cells[x][y] and self._field[x][y] != 10:
            self._covered_cells[x][y] = True
            self.opened_cells += 1

            for i in range(x - 1, x + 2):
                for j in range(y - 1, y + 2):
                    self.flood(i, j)

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

    def flood(self, x, y):
        if x < 0 or x > 9:
            return
        if y < 0 or y > 9:
            return

        if self._field[x][y] != 9 and not self._field[x][y] == 10 and not self._covered_cells[x][y]:
            self._covered_cells[x][y] = True
            self.opened_cells += 1

            if self._field[x][y] == 0:
                self.flood(x + 1, y)
                self.flood(x - 1, y)
                self.flood(x, y + 1)
                self.flood(x, y - 1)

    def reset(self):
        self._field = [[0 for _ in range(10)] for _ in range(10)]
        self._covered_cells = [[False for _ in range(10)] for _ in range(10)]

        self.game_over = False
        self.opened_cells = 0
        self.randomize_mines()
