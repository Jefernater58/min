import argparse
import curses

VERSION = "1.0.0"
TITLE_STRING = f"MIN v{VERSION}"


def main(stdscr):
    parser = argparse.ArgumentParser(prog='min', description='A basic command-line text editor')
    parser.add_argument('filename', nargs="?", default=None)
    args = parser.parse_args()

    curses.noecho()
    curses.cbreak()

    curses.start_color()
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)

    titlebar = curses.newwin(1, curses.COLS, 0, 0)
    titlebar.bkgd(" ", curses.color_pair(1))
    display_filename = args.filename if args.filename is not None else "new file"
    titlebar.addstr(0, 0, TITLE_STRING + display_filename.center(curses.COLS)[len(TITLE_STRING) + 1:])

    textarea = curses.newwin(curses.LINES - 1, curses.COLS, 1, 0)

    run = True
    while run:
        titlebar.refresh()
        textarea.refresh()
        char = textarea.getch()
        textarea.addch(char)


curses.wrapper(main)
