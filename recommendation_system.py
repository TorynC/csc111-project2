""""CSC111 Project 2: Movie Recommendation System Code
"""
import pygame
import sys
import pygame_gui
from weighted_decision import recommendation_system

pygame.init()
SCREEN_SIZE = (1000, 800)
BLACK = (12, 11, 0)
YELLOW = (222, 181, 34)

SCREEN = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption("IMDb Movie Recommendation System")
titlefont = pygame.font.SysFont("arialblack", 37)
descriptionfont = pygame.font.SysFont("arialblack", 20)
CLOCK = pygame.time.Clock()
MANAGER = pygame_gui.UIManager(SCREEN_SIZE)
to_be_printed = []
TEXT_INPUT1 = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((300, 140), (400, 50),
                                                  manager=MANAGER, object_id="text1"))
TEXT_INPUT2 = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((300, 300), (400, 50),
                                                  manager=MANAGER, object_id="text2"))
TEXT_INPUT3 = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((300, 370), (400, 50),
                                                  manager=MANAGER, object_id="text3"))
TEXT_INPUT4 = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((50, 450), (300, 50),
                                                  manager=MANAGER, object_id="text4"))
TEXT_INPUT5 = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((350, 450), (300, 50),
                                                  manager=MANAGER, object_id="text5"))
TEXT_INPUT6 = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((650, 450), (300, 50),
                                                  manager=MANAGER, object_id="text6"))
TEXT_INPUT7 = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((300, 220), (400, 50),
                                                  manager=MANAGER, object_id="text7"))


def draw_text(text: str, font: pygame.Font, color: tuple[int, int, int]) -> pygame.Surface:
    """Draws the text"""
    txt = font.render(text, True, color)
    return txt


def is_integer(userinput: int | str) -> bool:
    """tests input value to see if it is an integer or string"""
    try:
        int(userinput)
        return True
    except ValueError:
        return False


class Main:
    """Class that creates an object of the main program"""
    def __init__(self):
        self.screen = SCREEN
        self.state_manager = StateManager("start")
        self.start = Start(self.screen, self.state_manager)
        self.questionnaire = Questionnaire(self.screen, self.state_manager)
        self.outputs = {"year": "", "runtime": "", "genre": "", "director": "",
                        "actor1": "", "actor2": "", "actor3": ""}
        self.results = Results(self.screen, self.state_manager)
        self.inputs = []

        self.states = {'start': self.start, "questionnaire": self.questionnaire,
                       "results": self.results}

    def run(self) -> None:
        """Method that will run the main loop of the program"""
        while True:
            ui_refresh_rate = CLOCK.tick(60) / 1000

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame_gui.UI_TEXT_ENTRY_FINISHED:
                    self.inputs.append(event.text)
                    self.states['questionnaire'].clear_error_message()
                if event.type == pygame.KEYDOWN:
                    if (event.key == pygame.K_ESCAPE and
                            self.state_manager.get_state() == "questionnaire"):
                        self.state_manager.set_state("start")
                        self.inputs.clear()
                    if event.key == pygame.K_TAB:
                        if len(self.inputs) < 7:
                            self.questionnaire.errormessage(0)
                        elif len(self.inputs) > 7:
                            self.questionnaire.errormessage(2)
                        else:
                            if is_integer(self.inputs[0]) and is_integer(self.inputs[1]):
                                if (self.inputs[0] == '' or self.inputs[1] == '' or
                                        self.inputs[2] == ''):
                                    self.questionnaire.errormessage(3)
                                else:
                                    self.outputs["year"] = self.inputs[0]
                                    self.outputs["runtime"] = self.inputs[1]
                                    self.outputs["genre"] = self.inputs[2]
                                    self.outputs["director"] = self.inputs[3]
                                    self.outputs["actor1"] = self.inputs[4]
                                    self.outputs["actor2"] = self.inputs[5]
                                    self.outputs["actor3"] = self.inputs[6]

                                    to_be_printed.extend(recommendation_system("data/imdb_top_1000.csv",
                                                                               self.outputs))
                                    self.state_manager.set_state("results")
                            else:
                                self.questionnaire.errormessage(1)
                    if self.state_manager.get_state() == "results":
                        if event.key == pygame.K_BACKSPACE:
                            pygame.quit()
                            sys.exit()
                MANAGER.process_events(event)
            MANAGER.update(ui_refresh_rate)
            self.states[self.state_manager.get_state()].run()

            pygame.display.update()


class Results:
    """Class that will create the results page of the GUI"""
    def __init__(self, display, state_manager):
        self.display = display
        self.state_manager = state_manager

    def run(self) -> None:
        """Method that will run display the results page of the GUI"""
        self.display.fill(BLACK)
        text1surface = draw_text("Results", titlefont, YELLOW)
        text1rect = text1surface.get_rect(center=(SCREEN_SIZE[0] // 2, SCREEN_SIZE[1] // 10))
        self.display.blit(text1surface, text1rect)

        exitmessage = draw_text("Press BACKSPACE to exit", descriptionfont, YELLOW)
        exitrect = exitmessage.get_rect(center=(SCREEN_SIZE[0] // 2, 700))
        self.display.blit(exitmessage, exitrect)

        results1 = draw_text(to_be_printed[0], descriptionfont, YELLOW)
        results1rect = results1.get_rect(center=(SCREEN_SIZE[0] // 2, 200))
        self.display.blit(results1, results1rect)

        results2 = draw_text(to_be_printed[1], descriptionfont, YELLOW)
        results2rect = results2.get_rect(center=(SCREEN_SIZE[0] // 2, 300))
        self.display.blit(results2, results2rect)

        results3 = draw_text(to_be_printed[2], descriptionfont, YELLOW)
        results3rect = results3.get_rect(center=(SCREEN_SIZE[0] // 2, 400))
        self.display.blit(results3, results3rect)

        results4 = draw_text(to_be_printed[3], descriptionfont, YELLOW)
        results4rect = results4.get_rect(center=(SCREEN_SIZE[0] // 2, 500))
        self.display.blit(results4, results4rect)

        results5 = draw_text(to_be_printed[4], descriptionfont, YELLOW)
        results5rect = results5.get_rect(center=(SCREEN_SIZE[0] // 2, 600))
        self.display.blit(results5, results5rect)


class Questionnaire:
    """Class that will create an object for the questionnaire class and display the questionnaire
    page for the GUI"""
    def __init__(self, display, state_manager):
        self.display = display
        self.state_manager = state_manager
        self.current_error_message = None

    def run(self) -> None:
        """Display and update the questionnaire page for the GUI"""
        self.display.fill(BLACK)
        text1surface = draw_text("Please answer the following questions "
                                 "(press enter for each text box entry)", descriptionfont, YELLOW)
        text1rect = text1surface.get_rect(center=(SCREEN_SIZE[0] // 2, 10))
        self.display.blit(text1surface, text1rect)

        question1surf = draw_text("Enter your preferred release year of movies", descriptionfont,
                                  YELLOW)
        question1rect = question1surf.get_rect(center=(SCREEN_SIZE[0] // 2, 120))
        self.display.blit(question1surf, question1rect)

        question2surf = draw_text("Enter your preferred runtime (minutes)", descriptionfont, YELLOW)
        question2rect = question2surf.get_rect(center=(SCREEN_SIZE[0] // 2, 200))
        self.display.blit(question2surf, question2rect)

        question3surf = draw_text("Enter your preferred genre", descriptionfont, YELLOW)
        question3rect = question3surf.get_rect(center=(SCREEN_SIZE[0] // 2, 280))
        self.display.blit(question3surf, question3rect)

        question4surf = draw_text("Enter your preferred director (optional, press enter "
                                  "in empty entry)", descriptionfont, YELLOW)
        question4rect = question4surf.get_rect(center=(SCREEN_SIZE[0] // 2, 360))
        self.display.blit(question4surf, question4rect)

        question5surf = draw_text("Enter your 3 preferred actors (optional, press enter "
                                  "in empty entry)", descriptionfont, YELLOW)
        question5rect = question5surf.get_rect(center=(SCREEN_SIZE[0] // 2, 440))
        self.display.blit(question5surf, question5rect)

        text2surf = draw_text("Press ESC to restart/Press TAB to continue", descriptionfont, YELLOW)
        text2rect = text2surf.get_rect(center=(SCREEN_SIZE[0] // 2, 550))
        self.display.blit(text2surf, text2rect)

        MANAGER.draw_ui(self.display)

        if self.current_error_message:
            errorsurf = draw_text(self.current_error_message, descriptionfont, YELLOW)
            errorrect = errorsurf.get_rect(center=(SCREEN_SIZE[0] // 2, 600))
            self.display.blit(errorsurf, errorrect)

    def errormessage(self, signal: int) -> None:
        """Will update the error message that will be displayed on the questionnaire page"""
        if signal == 0:
            self.current_error_message = "Error: answer all questions"
        elif signal == 1:
            self.current_error_message = "Error: please enter an integer for entries 1 and 2"
        elif signal == 2:
            self.current_error_message = "Error: too many inputs, restart and clear all entries"
        elif signal == 3:
            self.current_error_message = "Error: entries 1, 2 and 3 must not be empty"
        else:
            self.current_error_message = None

    def clear_error_message(self) -> None:
        """Set the error page to nothing if there is no error"""
        self.current_error_message = None


class Start:
    """Class that will create the starting page of the GUI"""
    def __init__(self, display, state_manager):
        self.display = display
        self.state_manager = state_manager

    def run(self) -> None:
        """Method that will update the starting page screen of the GUI"""
        self.display.fill(BLACK)

        keys = pygame.key.get_pressed()
        titlesurface = draw_text("IMDb Movie Recommendation System", titlefont,
                                 YELLOW)
        titlerect = titlesurface.get_rect(center=(SCREEN_SIZE[0] // 2, SCREEN_SIZE[1] // 8))
        self.display.blit(titlesurface, titlerect)
        description = ("Hello, welcome to the CSC111 IMDb Movie Recommendation System! \n"
                       "You will answer a few questions from a questionnaire \n"
                       "and based on your chosen preferences, the program will recommend \n"
                       "the 5 most suitable movies for you from a database of the top 1000 \n"
                       "highest rated movies on IMDb. No personal information will be required.")
        collection = description.splitlines()
        curr_pos = 300
        for words in collection:
            word_surface = draw_text(words, descriptionfont, YELLOW)
            word_rect = word_surface.get_rect(center=(SCREEN_SIZE[0] // 2, curr_pos))
            self.display.blit(word_surface, word_rect)
            curr_pos += 30
            self.display.blit(word_surface, word_rect)
        continue_surface = draw_text("Press SPACE to continue", descriptionfont, YELLOW)
        continue_rect = continue_surface.get_rect(center=(SCREEN_SIZE[0] // 2, curr_pos + 100))
        self.display.blit(continue_surface, continue_rect)

        if keys[pygame.K_SPACE]:
            self.state_manager.set_state("questionnaire")


class StateManager:
    """Class that will create the object to allow transition between different pages of the
    program"""
    def __init__(self, currentstate):
        self.currentstate = currentstate

    def get_state(self) -> None:
        """returns the current page being displayed"""
        return self.currentstate

    def set_state(self, state) -> None:
        """changes the current page"""
        self.currentstate = state


if __name__ == "__main__":
    main = Main()
    main.run()
