from board import *
from button_traits import Play


class Game:
    def __init__(self):
        # Window settings
        self.window = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_icon(WINDOW_ICON)
        pygame.display.set_caption("Minesweeper")

        # Buttons
        self.play_button = Play()

        self.board = Board()
        self.mouse_pos = (0, 0)

    def main_menu(self):
        # Function that sets up the main menu and runs its game-loop.
        self.window.fill(GRAY)
        #self.window.blit(BG_IMAGE, (120, 0))

        while True:
            self.mouse_pos = pygame.mouse.get_pos()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()


            self.play_button.draw_button(self.window, self.mouse_pos)
            pygame.display.update()

    # Game Functions
    def update_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                # Resetting the board when pressing 'r'.
                if event.key == pygame.K_r:
                    self.board.reset()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if self.board.game_over:
                        self.board.reset()
                    elif self.board.first_move:
                        self.board.play_first_move(self.mouse_pos)
                        self.board.first_move = False
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
        while True:
            self.main_menu()
            self.update_events()
            self.update()
            self.render()
