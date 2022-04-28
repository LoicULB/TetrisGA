import pygame
import pygame_gui
import TetrisParallelClass

HEURISTIC_LABELS = ["Holes", "Height", "Bumpiness", "Line cleared", "Hollow columns", "Row Transition",
                    "Column Transition",
                    "Pitcount"]

MAIN_HEURISTICS = ["Holes", "Height", "Bumpiness", "Line cleared"]

ERROR_RECTANGLE = pygame.Rect((200, 350), (300, 100))


def handle_run(text_entry_nb_gen,
               text_entry_limit_time,
               heuristic_selector,
               error_text: pygame_gui.elements.ui_text_box.UITextBox):
    validate_nb_gen_entry(text_entry_nb_gen, error_text)
    validate_time_entry(text_entry_limit_time, error_text)
    validate_heuristics(heuristic_selector, error_text)
    heuristics_to_consider = turn_heuristic_strings_into_indexes(heuristic_selector)
    print(heuristics_to_consider)
    if not error_text.visible:
        print("Let's Get the party started!")
        tetris_parallel = TetrisParallelClass.TetrisParallel(nb_gen=int(text_entry_nb_gen),
                                                             limit_time=int(text_entry_limit_time),
                                                             heuristics_selected=heuristics_to_consider)
        tetris_parallel.launch()
        return

def turn_heuristic_strings_into_indexes(heuristics_to_consider):
    weight_to_consider = []
    for heuristic in heuristics_to_consider:
        if heuristic == "Holes":
            weight_to_consider.append(0)
        elif heuristic == "Height":
            weight_to_consider.append(1)
        elif heuristic == "Bumpiness":
            weight_to_consider.append(2)
        elif heuristic == "Line cleared":
            weight_to_consider.append(3)
        elif heuristic == "Hollow columns":
            weight_to_consider.append(4)
        elif heuristic == "Row Transition":
            weight_to_consider.append(5)
        elif heuristic == "Column Transition":
            weight_to_consider.append(6)
        elif heuristic == "Pitcount":
            weight_to_consider.append(7)
    return weight_to_consider


def validate_heuristics(heuristic_selected:list, error_text: pygame_gui.elements.ui_text_box.UITextBox):
    if not heuristic_selected:
        error_text.set_text("Please my dear, choose at least one heuristic to train your Genetic Agents")
        error_text.visible = True


def validate_nb_gen_entry(entry: str,
                          error_text: pygame_gui.elements.ui_text_box.UITextBox):
    if entry =="":
        error_text.set_text("Please write something for the number of gen")
        error_text.visible = True
    elif int(entry) > 1000:
        error_text.set_text("The number of generation cannot exceed 1000")
        error_text.visible = True


def validate_time_entry(entry:str,
                          error_text: pygame_gui.elements.ui_text_box.UITextBox):
    if entry=="":
        error_text.set_text("Please write something for the time limit")
        error_text.visible = True
    elif int(entry) < 250 or int(entry) > 5000:
        error_text.set_text("You cannot train your GA with a time lower 250 or above 5000")
        error_text.visible = True


def run():
    pygame.init()

    background, window_surface, manager, error_text = init_window()

    heuristic_selector, run_button, text_entry_limit_time, text_entry_nb_gen = initialize_buttons(manager)

    clock = pygame.time.Clock()
    is_running = True

    while is_running:
        time_delta = clock.tick(60) / 1000.0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = False
            if event.type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == run_button:
                    error_text.visible = False
                    str = ""
                    print(f"Number of generation : {text_entry_nb_gen.text} ")
                    print(f"Time Limit : {text_entry_limit_time.text} ")
                    print(f"Weights to consider : {heuristic_selector.get_multi_selection()}")
                    handle_run(text_entry_nb_gen.text, text_entry_limit_time.text, heuristic_selector.get_multi_selection(), error_text)

                """
                if event.ui_element == hello_button:
                    print('Hello World!')
                if event.ui_element == run:
                    print("I will clear everything")
                    manager.clear_and_reset()
                """

            manager.process_events(event)

        manager.update(time_delta)

        window_surface.blit(background, (0, 0))
        manager.draw_ui(window_surface)

        pygame.display.update()


def init_window():
    pygame.display.set_caption('Tetris Menu')
    window_surface = pygame.display.set_mode(size=(TetrisParallelClass.SCREEN_WIDTH, TetrisParallelClass.SCREEN_HEIGHT))
    #window_surface = pygame.display.set_mode((800, 600))
    background = pygame.Surface((800, 600))
    background.fill(pygame.Color('#000000'))
    manager = pygame_gui.UIManager((800, 600))
    text_error = pygame_gui.elements.ui_text_box.UITextBox(html_text="",
                                                           relative_rect=ERROR_RECTANGLE,
                                                           manager=manager,
                                                           visible=False,
                                                           )
    return background, window_surface, manager, text_error


def initialize_buttons(manager):
    text_box_nb_gen = pygame_gui.elements.ui_text_box.UITextBox(html_text="Number of generation",
                                                                relative_rect=pygame.Rect((100, 275), (200, 50)),
                                                                manager=manager)
    text_entry_nb_gen = pygame_gui.elements.ui_text_entry_line.UITextEntryLine(
        relative_rect=pygame.Rect((350, 275), (100, 50)), manager=manager)
    text_box_limit_time = pygame_gui.elements.ui_text_box.UITextBox(html_text="Time limit for one gen",
                                                                    relative_rect=pygame.Rect((100, 200), (200, 50)),
                                                                    manager=manager)
    text_entry_limit_time = pygame_gui.elements.ui_text_entry_line.UITextEntryLine(
        relative_rect=pygame.Rect((350, 200), (100, 50)),
        manager=manager)
    text_box_heuristic_selector = pygame_gui.elements.ui_text_box.UITextBox(html_text="Heuristics to consider",
                                                                            relative_rect=pygame.Rect((150, 50),
                                                                                                      (200, 50)),
                                                                            manager=manager)
    heuristic_selector = pygame_gui.elements.ui_selection_list.UISelectionList(
        relative_rect=pygame.Rect((350, 50), (250, 100)),
        item_list=HEURISTIC_LABELS,
        manager=manager,
        allow_multi_select=True,
        default_selection=MAIN_HEURISTICS)
    run_button = pygame_gui.elements.ui_button.UIButton(relative_rect=pygame.Rect((350, 500), (100, 50)), text="Run",
                                                        manager=manager)


    return heuristic_selector, run_button, text_entry_limit_time, text_entry_nb_gen


if __name__ == '__main__':
    run()
