""""CSC111 Project 2: Movie Recommendation System Code
"""
import pygame

pygame.init()
SCREEN_SIZE = (800, 800)
BLACK = (12, 11, 0)
YELLOW = (222, 181, 34)

screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption("IMDb Movie Recommendation System")
titlefont = pygame.font.SysFont("arialblack", 37)
descriptionfont = pygame.font.SysFont("arialblack", 20)


def draw_text(text, font, color):
    """Draws the text"""
    txt = font.render(text, True, color)
    return txt


def menu() -> pygame.Surface:
    """Initialize the background of the main page"""
    background = pygame.Surface(SCREEN_SIZE)
    background.fill(BLACK)

    titlesurface = draw_text("IMDb Movie Recommendation System", titlefont,
                             YELLOW)
    titlerect = titlesurface.get_rect(center=(SCREEN_SIZE[0] // 2, SCREEN_SIZE[1] // 8))
    background.blit(titlesurface, titlerect)

    description = ("Hello, welcome to the CSC111 IMDb Movie Recommendation System! \n"
                   "You will answer a few questions from a questionnaire \n"
                   "and based on your chosen preferences, the program will recommend \n"
                   "the most suitable movies for you from a database of the top 1000 \n"
                   "highest rated movies on IMDb. No personal information will be required.")
    collection = description.splitlines()
    curr_pos = 300
    for words in collection:
        word_surface = draw_text(words, descriptionfont, YELLOW)
        word_rect = word_surface.get_rect(center=(SCREEN_SIZE[0] // 2, curr_pos))
        background.blit(word_surface, word_rect)
        curr_pos += 30
        background.blit(word_surface, word_rect)

    continue_surface = draw_text("Press SPACE to continue", descriptionfont, YELLOW)
    continue_rect = continue_surface.get_rect(center=(SCREEN_SIZE[0] // 2, curr_pos + 100))
    background.blit(continue_surface, continue_rect)
    return background


def questionnaire() -> pygame.surface:
    """Returns the questionnaire page for the program"""
    pass


def results() -> pygame.surface:
    """Returns the results page for the program"""
    pass


def main_loop() -> None:
    """The main loop of the GUI"""
    run = True
    background = menu()
    screen.blit(background, (0, 0))
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    run = False

        pygame.display.update()
    pygame.display.quit()
    pygame.quit()


if __name__ == "__main__":
    main_loop()
