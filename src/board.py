import random
from constants import *


class Board:
    def __init__(self):
        # Used in options menu to determine how big the field is.
        self.grid_size = 10

        # This is set up in the reset function.
        self._cell_size = None
        self._covered_cells = None
        self._field = None
        self.amount_of_flags = None

        # Variables
        self.question_mark_tile = False
        self.game_over = False
        self.first_move = True
        self.opened_cells = 0
        self.mine_count = 0
        self._flagged_positions = {}

    @staticmethod
    def _scale_images(cell_size: int):
        new_image_size = (cell_size, cell_size)
        for i in range(len(DRAWING)):
            DRAWING[i] = pygame.transform.scale(DRAWING[i], new_image_size)

    @staticmethod
    def _draw_rect(window, fill_color, outline_color, rect, border=1.5):
        window.fill(outline_color, rect)
        window.fill(fill_color, rect.inflate(-border * 2, -border * 2))

    def draw_grid(self, window: pygame.display, mouse: tuple):
        mouse_x, mouse_y = (mouse[1] - 100) // self._cell_size, mouse[0] // self._cell_size

        top_label = pygame.Rect(0, 0, 800, 100)
        self._draw_rect(window, GRAY, WHITE, top_label, 5)

        for i in range(self.grid_size):
            for j in range(self.grid_size):
                position = (j * self._cell_size, i * self._cell_size + 100)

                # Draw a gray cell if the tile isn't open,
                # DRAWING is defined in constants.py
                if not self._covered_cells[i][j]:
                    if j == mouse_y and i == mouse_x:
                        window.blit(DRAWING[12], position)
                    else:
                        window.blit(DRAWING[11], position)

                    if self._field[i][j] == 10:
                        window.blit(DRAWING[10], position)
                # Otherwise, draw whatever that tile represents in the field.
                else:
                    if self._field[i][j] != 9:
                        window.blit(DRAWING[self._field[i][j]], position)
                    else:
                        # 0 is an image of an empty tile, 9 is an image of a mine.
                        window.blit(DRAWING[0], position)
                        window.blit(DRAWING[9], position)

    def play_first_move(self, mouse: tuple):
        x, y = (mouse[1] - 100) // int(self._cell_size), mouse[0] // int(self._cell_size)

        if self._field[x][y] != 10:
            self._covered_cells[x][y] = True
            self.opened_cells += 1

            # Randomize only after the move has been made,
            # we don't want a mine on the first move.
            self._randomize_mines((x, y))

            # If the user enabled question tiles, we randomly
            # distribute them on the field.
            if self.question_mark_tile:
                self._randomize_question_mark()

            for i in range(x - 1, x + 2):
                for j in range(y - 1, y + 2):
                    self._flood_fill(i, j)

    def place_flag(self, mouse: tuple):
        # Places and removes flags from the grid,
        # uses a dictionary to store previous grid value.
        x, y = (mouse[1] - 100) // int(self._cell_size), mouse[0] // int(self._cell_size)

        if not self._covered_cells[x][y]:
            if (x, y) not in self._flagged_positions:
                # Place flags only if we have them.
                if self.amount_of_flags:
                    self._flagged_positions[(x, y)] = self._field[x][y]

                    if self._field[x][y] == 9:
                        self.opened_cells += 1

                    self._field[x][y] = 10
                    self.amount_of_flags -= 1
            else:
                self._field[x][y] = self._flagged_positions[(x, y)]

                if self._field[x][y] == 9:
                    self.opened_cells -= 1

                del self._flagged_positions[(x, y)]
                self.amount_of_flags += 1

    def open_cell(self, mouse: tuple):
        x, y = (mouse[1] - 100) // int(self._cell_size), mouse[0] // int(self._cell_size)

        if self._field[x][y] == 9:
            self._open_all_mines()

        if not self._covered_cells[x][y] and self._field[x][y] != 10:
            self._covered_cells[x][y] = True
            self.opened_cells += 1

            for i in range(x - 1, x + 2):
                for j in range(y - 1, y + 2):
                    self._flood_fill(i, j)

    def _flood_fill(self, x: int, y: int):
        # Algorithm that will open cells around the one
        # we clicked if that cell isn't a flag/mine/already explored.
        if x < 0 or x > self.grid_size - 1:
            return
        if y < 0 or y > self.grid_size - 1:
            return

        if self._field[x][y] != 9 and not self._field[x][y] == 10 \
           and not self._covered_cells[x][y]:
            self._covered_cells[x][y] = True
            self.opened_cells += 1

            if self._field[x][y] == 0:
                self._flood_fill(x + 1, y)
                self._flood_fill(x - 1, y)
                self._flood_fill(x, y + 1)
                self._flood_fill(x, y - 1)

    def _randomize_mines(self, clicked_position: tuple):
        for i in range(self.mine_count, 0, -1):
            x = random.randint(0, self.grid_size - 1)
            y = random.randint(0, self.grid_size - 1)
            if self._field[x][y] == 9 or (x, y) == clicked_position:
                i += 1
            else:
                self._field[x][y] = 9

        # Count the number of mines around each cell
        # and put the matching number in that field position.
        for i in range(0, self.grid_size - 1):
            for j in range(0, self.grid_size - 1):
                if self._field[i][j] != 9 and self._field[i][j] != 10:
                    self._field[i][j] = self._count_mines(i, j)

    def _randomize_question_mark(self):
        amount_of_question_tiles = self.grid_size**2 // 10

        for i in range(amount_of_question_tiles, 0, -1):
            x = random.randint(0, self.grid_size - 1)
            y = random.randint(0, self.grid_size - 1)

            # Don't put the question mark over
            # a mine or over an empty tile.
            if self._field[x][y] != 9 and self._field[x][y] != 0:
                self._field[x][y] = 13
            else:
                i += 1

    def _count_mines(self, x: int, y: int) -> int:
        mines_around = 0

        for i in range(x - 1, x + 2):
            for j in range(y - 1, y + 2):
                if 0 <= i < self.grid_size and 0 <= j < self.grid_size:
                    if self._field[i][j] == 9:
                        mines_around += 1

        return mines_around

    def _open_all_mines(self):
        # When you click on a mine, it will show
        # all of them and the game will be over.
        for i in range(self.grid_size):
            for j in range(self.grid_size):
                if self._field[i][j] == 10:
                    if self._flagged_positions[(i, j)] == 9:
                        self._field[i][j] = 9

                if self._field[i][j] == 9:
                    self._covered_cells[i][j] = True

        self.game_over = True

    def reset(self):
        self._cell_size = WIDTH / self.grid_size

        self._covered_cells = [[False for _ in range(self.grid_size)] for _ in range(self.grid_size)]
        self._field = [[0 for _ in range(self.grid_size)] for _ in range(self.grid_size)]

        # Scale image depending on the cell size.
        self._scale_images(self._cell_size)

        self.game_over = False
        self.first_move = True
        self.opened_cells = 0
        self.amount_of_flags = self.mine_count
