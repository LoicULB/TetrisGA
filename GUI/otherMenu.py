import pygame
import pygame_gui

HEURISTIC_LABELS = ["Holes", "Height", "Bumpiness", "Line cleared", "Hollow columns", "Row Transition", "Column Transition",
             "Pitcount"]


MAIN_HEURISTICS = ["Holes", "Height", "Bumpiness", "Line cleared"]


def run():

    pygame.init()

    pygame.display.set_caption('Tetris Menu')
    window_surface = pygame.display.set_mode((800, 600))

    background = pygame.Surface((800, 600))
    background.fill(pygame.Color('#000000'))

    manager = pygame_gui.UIManager((800, 600))
    text_box_nb_gen = pygame_gui.elements.ui_text_box.UITextBox(html_text="Number of generation", relative_rect=pygame.Rect((100, 275), (200, 50)), manager=manager)
    text_entry_nb_gen = pygame_gui.elements.ui_text_entry_line.UITextEntryLine(relative_rect=pygame.Rect((350, 275), (100, 50)), manager=manager)

    text_box_limit_time = pygame_gui.elements.ui_text_box.UITextBox(html_text="Time limit for one gen",
                                                                relative_rect=pygame.Rect((100, 200), (200, 50)),
                                                                manager=manager)
    text_entry_limit_time = pygame_gui.elements.ui_text_entry_line.UITextEntryLine(relative_rect=pygame.Rect((350, 200), (100, 50)),
                                                                      manager=manager)
    text_box_heuristic_selector =  pygame_gui.elements.ui_text_box.UITextBox(html_text="Heuristics to consider",
                                                                relative_rect=pygame.Rect((150, 50), (200, 50)),
                                                                manager=manager)
    heuristic_selector = pygame_gui.elements.ui_selection_list.UISelectionList(relative_rect=pygame.Rect((350, 50), (250,100)),
                                                                               item_list=HEURISTIC_LABELS,
                                                                               manager=manager,
                                                                               allow_multi_select=True,
                                                                               default_selection=MAIN_HEURISTICS)

    run_button = pygame_gui.elements.ui_button.UIButton(relative_rect=pygame.Rect((350, 500), (100, 50)), text="Run", manager=manager)



    clock = pygame.time.Clock()
    is_running = True

    while is_running:
        time_delta = clock.tick(60) / 1000.0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = False
            if event.type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == run_button:
                    str = ""
                    print(f"Number of generation : {text_entry_nb_gen.text} ")
                    print(f"Time Limit : {text_entry_limit_time.text} ")
                    print(f"Weights to consider : {heuristic_selector.get_multi_selection()}")

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


if __name__ == '__main__':
    run()