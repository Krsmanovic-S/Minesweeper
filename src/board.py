import random
from constants import *


class Board:
    def __init__(self):
        self.opened = [[False for _ in range(10)] for _ in range(10)]
        self.field = [[0 for _ in range(10)] for _ in range(10)]

        self.game_over = False
        self.opened_cells = 0
        self.mine_count = 20
        self.current_mines = 0
        self.current_cell = (0, 0)

    @staticmethod
    def draw_rect(window, fill_color, outline_color, rect, border=1):
        window.fill(outline_color, rect)
        window.fill(fill_color, rect.inflate(-border * 2, -border * 2))

    def draw_grid(self, window):
        for i in range(10):
            for j in range(10):
                cell = pygame.Rect(j * 100, i * 100, 100, 100)

                # 0 is closed cell, 1 is opened cell
                if not self.opened[i][j]:
                    self.draw_rect(window, GRAY, BLACK, cell, 2)
                else:
                    if self.field[i][j] == 0:
                        self.draw_rect(window, OPENED, BLACK, cell, 2)
                    elif self.field[i][j] == 1:
                        window.blit(ONE, (j * 100, i * 100))
                    elif self.field[i][j] == 2:
                        window.blit(TWO, (j * 100, i * 100))
                    elif self.field[i][j] == 3:
                        window.blit(THREE, (j * 100, i * 100))
                    elif self.field[i][j] == 4:
                        window.blit(FOUR, (j * 100, i * 100))
                    elif self.field[i][j] == 5:
                        window.blit(FIVE, (j * 100, i * 100))
                    elif self.field[i][j] == 6:
                        window.blit(SIX, (j * 100, i * 100))
                    elif self.field[i][j] == 7:
                        window.blit(SEVEN, (j * 100, i * 100))
                    elif self.field[i][j] == 8:
                        window.blit(EIGHT, (j * 100, i * 100))
                    else:
                        self.draw_rect(window, RED, BLACK, cell, 2)

    def place_flag(self, mouse):
        x, y = mouse[1] // 100, mouse[0] // 100

        if not self.opened[x][y]:
            pass

    def randomize_mines(self):
        # Randomly distribute the mines on the field,
        # how much depends on the mine_count variable.
        for i in range(self.mine_count, -1, -1):
            x = random.randint(0, 9)
            y = random.randint(0, 9)
            if self.field[x][y] == 9:
                i += 1
            else:
                self.field[x][y] = 9

        # Now for each field, count the number of mines around
        # it and put the matching number in that field position.
        for i in range(0, 10):
            for j in range(0, 10):
                if self.field[i][j] != 9:
                    self.field[i][j] = self.count_mines(i, j)

    def count_mines(self, x, y):
        mines_around = 0

        for i in range(x - 1, x + 2):
            for j in range(y - 1, y + 2):
                if 0 <= i < 10 and 0 <= j < 10:
                    if self.field[i][j] == 9:
                        mines_around += 1

        return mines_around

    def open_cell(self, mouse):
        x, y = mouse[1] // 100, mouse[0] // 100

        if not self.opened[x][y] and self.field[x][y] != 9:
            self.opened[x][y] = True

            for i in range(x - 1, x + 2):
                for j in range(y - 1, y + 2):
                    self.flood(i, j)

    def flood(self, x, y):
        if x < 0 or x > 9:
            return
        if y < 0 or y > 9:
            return

        if self.field[x][y] != 9 and not self.opened[x][y]:
            self.opened[x][y] = True

            if self.field[x][y] == 0:
                self.flood(x + 1, y)
                self.flood(x - 1, y)
                self.flood(x, y + 1)
                self.flood(x, y - 1)

    def reset(self):
        self.field = [[0 for _ in range(10)] for _ in range(10)]
        self.opened = [[False for _ in range(10)] for _ in range(10)]

        self.game_over = False
        self.opened_cells = 0
        self.randomize_mines()
