from board import *
from button_traits import Play, Settings, Exit


class Game:
    def __init__(self):
        # Window settings
        self.window = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_icon(WINDOW_ICON)
        pygame.display.set_caption("Minesweeper")

        # Buttons
        self.play_button = Play()
        self.settings_button = Settings()
        self.exit_button = Exit()

        self.board = Board()
        self.mouse_pos = (0, 0)

    # Menu Functions
    def main_menu(self):
        # Function that sets up the main menu and runs its game-loop.
        self.window.fill(GRAY)
        while True:
            self.mouse_pos = pygame.mouse.get_pos()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if self.play_button.is_mouse_over(self.mouse_pos):
                            self.run()
                        elif self.settings_button.is_mouse_over(self.mouse_pos):
                            self.settings_menu()
                        elif self.exit_button.is_mouse_over(self.mouse_pos):
                            pygame.quit()
                            quit()

            self.play_button.draw_button(self.window, self.mouse_pos)
            self.settings_button.draw_button(self.window, self.mouse_pos)
            self.exit_button.draw_button(self.window, self.mouse_pos)

            pygame.display.update()

    def settings_menu(self):
        # Function that sets up the main menu and runs its game-loop.
        self.window.fill(GRAY)
        while True:
            self.mouse_pos = pygame.mouse.get_pos()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.main_menu()

            pygame.display.update()

    # Game Functions
    def update_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.board.reset()
                    self.main_menu()
            elif event.type == pygame.KEYDOWN:
                # Resetting the board when pressing 'r'.
                if event.key == pygame.K_r:
                    self.board.reset()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if self.board.game_over:
                        self.board.reset()
                    elif self.board.first_move:
                        # First move can never be a mine, so we handle
                        # that here, then move on normally.
                        self.board.play_first_move(self.mouse_pos)
                        self.board.first_move = False
                    else:
                        self.board.open_cell(self.mouse_pos)
                elif event.button == 3:
                    # Right mouse button places a flag.
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
            self.update_events()
            self.update()
            self.render()
