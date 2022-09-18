from board import Board
from constants import *
from button_traits import Play, Settings, Exit, MineCount, Grid, LinkedIn,\
                          Git, QuestionTile, Timer, Smiley, Back
from slider import Slider
import webbrowser
import time


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
        self._question_tile = QuestionTile()
        self._timer_button = Timer()
        self._back_button = Back()

        # Top-Bar Field GUI
        self.smiley = Smiley()
        self.game_state = 0

        # Git & LinkedIn
        self._git_button = Git()
        self._linkedin_button = LinkedIn()

        # Values in the constructor are (in this order):
        # position of the slider (x, y), maximum value, current filled up part.
        self._grid_size_slider = Slider((50, 165), 40, 75)
        self._mine_count_slider = Slider((450, 165), 500, 50)
        self._timer_slider = Slider((450, 415), 999, 0)

        # Variables
        self.board = Board()
        self.mouse_pos = (0, 0)
        self.timer_value = 0
        self.start_time = time.time()
        self.elapsed_time = 0
        self.clicked = False
        self.clicked_tile = (-1, -1)

    # Menu Functions
    def main_menu(self):
        # Function that sets up the main menu and runs its game-loop.
        self.window = pygame.display.set_mode((WIDTH, HEIGHT))
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
                            self.window = pygame.display.set_mode((800, 900))

                            self.board.mine_count = self._mine_count_slider.get_value()
                            self.board.grid_size = self._grid_size_slider.get_value()

                            self.start_time = time.time()
                            self.board.reset()
                            self._run()
                        # Transition into the option's menu.
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
        pressed_time_slider = False

        while True:
            self.mouse_pos = pygame.mouse.get_pos()

            # Update the maximum number of mines according to the mine
            # slider, as well as the timer value from its slider.
            self._mine_count_slider.upper_value = self._grid_size_slider.get_value()**2 - 1
            self.timer_value = self._timer_slider.get_value()

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
                        elif self._timer_button.is_mouse_over(self.mouse_pos):
                            pressed_time_slider = True

                        elif self._question_tile.is_mouse_over(self.mouse_pos):
                            # This variable is used to control which
                            # button appears for the question mark tile.
                            self.board.question_mark_tile = not self.board.question_mark_tile
                        elif self._back_button.is_mouse_over(self.mouse_pos):
                            self.main_menu()

                elif event.type == pygame.MOUSEBUTTONUP:
                    if event.button == 1:
                        # Cancel the dragging of the slider when
                        # we stop pressing the left mouse button.
                        pressed_grid_slider = False
                        pressed_mine_slider = False
                        pressed_time_slider = False

                elif event.type == pygame.KEYDOWN:
                    # Transition back to main menu by pressing escape.
                    if event.key == pygame.K_ESCAPE:
                        self.main_menu()

            self._grid_settings.draw_button(self.window, self.mouse_pos)
            self._mine_count.draw_button(self.window, self.mouse_pos)

            self._question_tile.update_question_tile(self.board.question_mark_tile)
            self._question_tile.draw_button(self.window, self.mouse_pos)

            self._timer_button.draw_button(self.window, self.mouse_pos)
            self._back_button.draw_button(self.window, self.mouse_pos)

            self._grid_size_slider.draw_slider(self.window)
            self._mine_count_slider.draw_slider(self.window)
            self._timer_slider.draw_slider(self.window)

            # Keep track of when we press the mouse over the slider
            # and change its value if we are dragging the mouse.
            if pressed_grid_slider:
                self._grid_size_slider.change_slider_value(self.mouse_pos)
            elif pressed_mine_slider:
                self._mine_count_slider.change_slider_value(self.mouse_pos)
            elif pressed_time_slider:
                self._timer_slider.change_slider_value(self.mouse_pos)

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
                    self.main_menu()
                # Resetting the board when pressing 'r'.
                if event.key == pygame.K_r:
                    self.board.reset()
                    self.start_time = time.time()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if self.mouse_pos[1] < 100:
                        if self.smiley.is_mouse_over(self.mouse_pos):
                            self.board.reset()
                            self.start_time = time.time()
                    elif self.mouse_pos[1] > 100:
                        self.clicked = True
                        if self.board.game_over:
                            self.board.reset()
                            self.start_time = time.time()
                elif event.button == 3 and self.mouse_pos[1] > 100:
                    # Right mouse button places a flag.
                    self.board.place_flag(self.mouse_pos)
            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    if self.clicked:
                        if self.board.first_move:
                            # First move can never be a mine, so we handle
                            # that here, then move on normally.
                            self.board.play_first_move(self.mouse_pos)
                            self.board.first_move = False
                        else:
                            self.board.open_cell(self.mouse_pos)
                        self.clicked = False

    def _update(self):
        self.mouse_pos = pygame.mouse.get_pos()

        if self.elapsed_time <= 999 and not self.board.game_over:
            self.elapsed_time = int(time.time() - self.start_time)

        # Here we want to get the game state which we use
        # below to determine which smiley face gets drawn.
        if not self.board.game_over:
            self.game_state = 1

        if self.board.opened_cells == self.board.grid_size ** 2:
            self.board.game_over = True
            self.game_state = 2
        elif self.board.game_over:
            self.game_state = 0

        self.smiley.update_smiley_picture(self.game_state)

    def _render(self):
        self.board.draw_grid(self.window, self.mouse_pos)
        self.smiley.draw_button(self.window, self.mouse_pos)

        # Draw the clock and the amount of flags.
        current_flag_amount = self.board.amount_of_flags
        current_time = self.elapsed_time
        for i in range(3, 0, -1):
            clock_digit = current_time % 10
            flag_digit = current_flag_amount % 10

            current_time = current_time // 10
            current_flag_amount = current_flag_amount // 10

            self.window.blit(CLOCK_DIGITS[flag_digit], (25 + 55 * (i - 1), 10))
            self.window.blit(CLOCK_DIGITS[clock_digit], (625 + 55 * (i - 1), 10))

        pygame.display.update()

    def _run(self):
        while True:
            self._update_events()
            self._update()
            self._render()
