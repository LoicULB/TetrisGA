from dataclasses import dataclass
import pygame_gui
import pygame
from Menu import Menu
from pygame_gui.elements.ui_text_box import UITextBox

HEURISTIC_LABELS = ["Holes", "Height", "Bumpiness", "Line cleared", "Hollow columns", "Row Transition",
                    "Column Transition",
                    "Pitcount"]
MAIN_HEURISTICS = HEURISTIC_LABELS[0:4]


@dataclass
class StartMenu(Menu):

    def __init__(self, screen_width, screen_height, color_str: str):
        super().__init__(screen_width, screen_height, color_str, "Start Menu")
        self.nb_gen_entry = None
        self.time_limit_entry = None
        self.run_button = None
        self.heuristics_selection = None
        self.init_commands()

    def init_commands(self):
        heuristics_tb, self.heuristics_selection = self.initialize_selection("Heuristics to consider", 150, 50,
                                                                             HEURISTIC_LABELS, MAIN_HEURISTICS)

        nb_gen_tb, nb_gen_entry = self.initialize_entry_line("Nb Generations", 100, 275)
        time_limit_tb, time_limit_entry = self.initialize_entry_line("Time limit", 100, 200)
        run_button = self.initialize_button("Run", 350, 500)

        nb_gen_entry.set_allowed_characters("numbers")
        time_limit_entry.set_allowed_characters("numbers")
        self.run_button = run_button
        self.nb_gen_entry = nb_gen_entry
        self.time_limit_entry = time_limit_entry

    def handle_events(self, event, is_running):
        super(StartMenu, self).handle_events(event, is_running)

        if event.type == pygame_gui.UI_BUTTON_PRESSED:
            if event.ui_element == self.run_button:
                # error_text.visible = False
                str = ""
                print(f"Number of generation : {self.nb_gen_entry.text} ")
                print(f"Time Limit : {self.time_limit_entry.text} ")
                print(f"Weights to consider : {self.heuristics_selection.get_multi_selection()}")
                # handle_run(text_entry_nb_gen.text, text_entry_limit_time.text, heuristic_selector.get_multi_selection(),
                # error_text)
        return is_running

if __name__ == '__main__':
    menu = StartMenu(screen_width=800, screen_height=600, color_str="#000000")
    menu.run()
