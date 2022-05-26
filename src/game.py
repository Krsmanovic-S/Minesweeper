from board import *


class Game:
    def __init__(self):
        # Window settings
        self.window = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Minesweeper")

        self.board = Board()
        self.mouse_pos = (0, 0)

    # Game Functions
    def update_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if self.board.game_over:
                        print('lol')
                        self.board.reset()
                    else:
                        self.board.open_cell(self.mouse_pos)
                elif event.button == 3:
                    self.board.place_flag(self.mouse_pos)

    def update(self):
        self.mouse_pos = pygame.mouse.get_pos()

        if self.board.opened_cells == 100:
            self.board.game_over = True

    def render(self):
        self.board.draw_grid(self.window)
        pygame.display.update()

    def run(self):
        self.board.randomize_mines()
        while True:
            self.update_events()
            self.update()
            self.render()
