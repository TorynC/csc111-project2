""""CSC111 Project 2: Movie Recommendation System Code
"""
import pygame

pygame.init()
SCREEN_SIZE = (800, 800)
BLACK = (12, 11, 0)
YELLOW = (222, 181, 34)

screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption("IMDb Movie Recommendation System")
font1 = pygame.font.SysFont("arialblack", 40)


class Button:
    """An Abstract class that is used to initialize button objects"""
    def __init__(self, image, x, y, text_input, font, color):
        self.x = x
        self.y = y
        self.font = font
        self.color = color
        self.text_input = text_input
        self.image = image
        self.rect = self.image.get_rect(center=(self.x, self.y))


def draw_text(text, font, text_col, x, y):
    """Draws the text"""
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))


def main() -> None:
    """The main loop of the GUI"""
    run = True

    while run:
        screen.fill(BLACK)
        draw_text("Press SPACE to pause", font1, YELLOW, 160, 250)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        pygame.display.update()
    pygame.display.quit()
    pygame.quit()


'''if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)

    import python_ta
    import python_ta.contracts

    python_ta.contracts.check_all_contracts()
    python_ta.check_all(config={
        'max-line-length': 120
    })'''
