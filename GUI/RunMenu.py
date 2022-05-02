from dataclasses import dataclass
import pygame_gui
import pygame

import TetrisParallelClass
import PlotUtils
from Menu import Menu

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
        self.error_text = pygame_gui.elements.ui_text_box.UITextBox(html_text="",
                                                           relative_rect= pygame.Rect((200, 350), (300, 100)),
                                                           manager=self.manager,
                                                           visible=False,
                                                           )
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
        is_running = super(StartMenu, self).handle_events(event, is_running)
        if not is_running:
            return is_running

        if event.type == pygame_gui.UI_BUTTON_PRESSED:
            if event.ui_element == self.run_button:
                self.error_text.visible = False
                self.handle_run()
        return is_running

    def handle_run(self):
        self.validate_nb_gen_entry()
        self.validate_time_entry()
        self.validate_heuristics()
        name_heuristics = self.heuristics_selection.get_multi_selection().copy()
        heuristics_to_consider = self.turn_heuristic_strings_into_indexes()
        print(heuristics_to_consider)
        if not self.error_text.visible:

            tetris_parallel = TetrisParallelClass.TetrisParallel(nb_gen=int(self.nb_gen_entry.text),
                                                                 limit_time=int(self.time_limit_entry.text),
                                                                 heuristics_selected=heuristics_to_consider)
            tetris_parallel.launch()
            PlotUtils.plot_training("../SavedModel", int(self.nb_gen_entry.text), name_heuristics)
            return

    def turn_heuristic_strings_into_indexes(self):
        weight_to_consider = []
        for heuristic in self.heuristics_selection.get_multi_selection():
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

    def validate_heuristics(self):
        if not self.heuristics_selection.get_multi_selection():
            self.error_text.set_text("Please my dear, choose at least one heuristic to train your Genetic Agents")
            self.error_text.visible = True

    def validate_nb_gen_entry(self):
        if self.nb_gen_entry.text == "":
            self.error_text.set_text("Please write something for the number of gen")
            self.error_text.visible = True
        elif int(self.nb_gen_entry.text) > 1000:
            self.error_text.set_text("The number of generation cannot exceed 1000")
            self.error_text.visible = True

    def validate_time_entry(self):
        if self.time_limit_entry.text == "":
            self.error_text.set_text("Please write something for the time limit")
            self.error_text.visible = True
        elif int(self.time_limit_entry.text) < 250 or int(self.time_limit_entry.text) > 5000:
            self.error_text.set_text("You cannot train your GA with a time lower 250 or above 5000")
            self.error_text.visible = True


if __name__ == '__main__':
    menu = StartMenu(screen_width=800, screen_height=600, color_str="#000000")
    menu.run()
