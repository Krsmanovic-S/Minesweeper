from board import Board
from constants import *
from button_traits import Play, Settings, Exit, MineCount, Grid, LinkedIn, Git, Test2, Test3
from slider import Slider
import webbrowser


class Game:
    def __init__(self):
        # Window Settings
        self.window = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_icon(WINDOW_ICON)
        pygame.display.set_caption("Minesweeper")

        # Main Menu Buttons
        self.play_button = Play()
        self.settings_button = Settings()
        self.exit_button = Exit()

        # Settings Menu Buttons
        self._grid_settings = Grid()
        self._mine_count = MineCount()
        self.test_2 = Test2()
        self.test_3 = Test3()

        # Git & LinkedIn
        self._git_button = Git()
        self._linkedin_button = LinkedIn()

        # Values in the constructor are (in this order):
        # position of the slider, maximum value, current filled up part.
        self._grid_size_slider = Slider((50, 165), 40, 75)
        self._mine_count_slider = Slider((450, 165), 600, 150)

        self.board = Board()
        self.mouse_pos = (0, 0)

    # Menu Functions
    def _main_menu(self):
        # Function that sets up the main menu and runs its game-loop.
        self.window.blit(BG, (0, 0))

        while True:
            self.mouse_pos = pygame.mouse.get_pos()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if self.play_button.is_mouse_over(self.mouse_pos):
                            self.board.mine_count = self._mine_count_slider.get_value()
                            self.board.grid_size = self._grid_size_slider.get_value()
                            self.board.reset()
                            self._run()
                        # Transition into the options menu.
                        elif self.settings_button.is_mouse_over(self.mouse_pos):
                            self._settings_menu()
                        elif self.exit_button.is_mouse_over(self.mouse_pos):
                            pygame.quit()
                            quit()
                        # Open the git url if the icon is selected.
                        elif self._git_button.is_mouse_over(self.mouse_pos):
                            webbrowser.open(GIT_URL, new=0, autoraise=True)
                        # Open the LinkedIn url if the icon is selected.
                        elif self._linkedin_button.is_mouse_over(self.mouse_pos):
                            webbrowser.open(LINKEDIN_URL, new=0, autoraise=True)

            self.play_button.draw_button(self.window, self.mouse_pos)
            self.settings_button.draw_button(self.window, self.mouse_pos)
            self.exit_button.draw_button(self.window, self.mouse_pos)

            self._git_button.draw_button(self.window, self.mouse_pos)
            self._linkedin_button.draw_button(self.window, self.mouse_pos)

            pygame.display.update()

    def _settings_menu(self):
        # Function that sets up the settings menu and runs its game-loop.
        self.window.blit(BG, (0, 0))

        pressed_grid_slider = False
        pressed_mine_slider = False

        while True:
            self.mouse_pos = pygame.mouse.get_pos()

            # Update the maximum number of mines according to the grid settings.
            self._mine_count_slider.upper_value = self._grid_size_slider.get_value()**2 - 1

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if self._grid_settings.is_mouse_over(self.mouse_pos):
                            pressed_grid_slider = True
                        elif self._mine_count.is_mouse_over(self.mouse_pos):
                            pressed_mine_slider = True

                elif event.type == pygame.MOUSEBUTTONUP:
                    if event.button == 1:
                        # Cancel the dragging of the slider when
                        # we stop pressing the left mouse button.
                        pressed_grid_slider = False
                        pressed_mine_slider = False

                elif event.type == pygame.KEYDOWN:
                    # Transition back to main menu by pressing escape.
                    if event.key == pygame.K_ESCAPE:
                        self._main_menu()

            self._grid_settings.draw_button(self.window, self.mouse_pos)
            self._mine_count.draw_button(self.window, self.mouse_pos)
            self.test_2.draw_button(self.window, self.mouse_pos)
            self.test_3.draw_button(self.window, self.mouse_pos)

            self._grid_size_slider.draw_slider(self.window)
            self._mine_count_slider.draw_slider(self.window)

            # Keep track of when we press the mouse over the slider
            # and change its value if we are dragging the mouse.
            if pressed_grid_slider:
                self._grid_size_slider.change_slider_value(self.mouse_pos)
            if pressed_mine_slider:
                self._mine_count_slider.change_slider_value(self.mouse_pos)

            pygame.display.update()

    # Game Functions
    def _update_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.board.reset()
                    self._main_menu()
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

    def _update(self):
        self.mouse_pos = pygame.mouse.get_pos()

        if self.board.opened_cells == (self.board.grid_size * self.board.grid_size):
            self.board.game_over = True

    def _render(self):
        self.board.draw_grid(self.window)
        pygame.display.update()

    def _run(self):
        while True:
            self._update_events()
            self._update()
            self._render()
