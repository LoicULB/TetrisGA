from GUI_RunMenu import Menu, StartMenu


def main():
    menu = StartMenu(screen_width=1200, screen_height=800, color_str="#000000")
    menu.run()


if __name__ == '__main__':
    main()