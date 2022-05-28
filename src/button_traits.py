from traitlets import HasTraits, Int, default, Any
from constants import *


class Button(HasTraits):
    x = Int()
    y = Int()
    highlighted = Any()
    image = Any()
    rect = Any()

    @default('rect')
    def _default_rect(self):
        self.rect = self.image.get_rect()
        self.rect.topleft = (self.x, self.y)
        return self.rect

    # Functions
    def draw_button(self, window, mouse):
        if self.rect.collidepoint(mouse[0] - 5, mouse[1] - 5):
            window.blit(self.highlighted, (self.rect.x, self.rect.y))
        else:
            window.blit(self.image, (self.rect.x, self.rect.y))

    def is_mouse_over(self, mouse_pos):
        if self.rect.collidepoint(mouse_pos):
            return True
        else:
            return False

    def draw_changing_button(self, window, mouse, button, check: bool):
        # This function is used for buttons which have multiple images
        # representing them, here we can decide which one to show.
        if not check:
            self.draw(window, mouse)
        else:
            button.draw(window, mouse)

class Play(Button):
    y = int(175)

    @default('x')
    def _default_x(self):
        return WIDTH // 2 - 200

    @default('highlighted')
    def _default_highlighted(self):
        return TEST

    @default('image')
    def _default_image(self):
        return TEST

