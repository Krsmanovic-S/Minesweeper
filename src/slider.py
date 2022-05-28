from constants import *


class Slider:
    def __init__(self, position: tuple, upper_value: int,
                 slider_width: int, outline_size: tuple = (300, 35)) -> None:
        self._position = position
        self._upper_value = upper_value
        self._slider_width = slider_width
        self._outline_size = outline_size
        self._font = pygame.font.Font(pygame.font.get_default_font(), self._slider_width - 10)

        self._rect = pygame.Rect(self._position[0], self._position[1], self._outline_size[0], self._outline_size[1])

    def get_value(self) -> int:
        # Returns the current value of the slider.
        return self._slider_width // (self._outline_size[0] // self._upper_value)

    def draw_slider(self, window: pygame.display) -> None:
        # Render the slider's outline.
        pygame.draw.rect(window, BLACK, (self._position[0], self._position[1],
                                         self._outline_size[0], self._outline_size[1]), 2)

        # Render the slider's inner rectangle.
        pygame.draw.rect(window, GRAY, (self._position[0], self._position[1],
                                        self._slider_width, self._outline_size[1]))

        # Creates a text representation from the value of the slider.
        integer_value = self._font.render(f"{round(self.get_value())}", True, (255, 255, 255))

        # Centre the text on the slider.
        text_x = self._position[0] + (self._outline_size[0] / 2) - (integer_value.get_rect().width / 2)
        text_y = self._position[1] + (self._outline_size[1] / 2) - (integer_value.get_rect().height / 2)

        window.blit(integer_value, (text_x, text_y))

    def change_value(self, mouse) -> None:
        # Function for changing the value of the slider by dragging it.
        self._slider_width = mouse[0] - self._position[0]

        # Limit the size of the slider.
        if self._slider_width < 1:
            self._slider_width = 0
        elif self._slider_width > self._outline_size[0]:
            self._slider_width = self._outline_size[0]
