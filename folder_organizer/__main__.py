#! /usr/bin/python3

import os
from math import floor
import sys


def main():
    # Progress bar creation
    def progress_bar(progress, result, bar_length):
        fill = floor(progress / result * (bar_length - 2))
        empty = (bar_length - 2) - fill
        txt = "{} out of {} completed.".format(progress, result)
        bar = "[" + "#" * fill + " " * empty + "] " + txt
        return bar

    # Variables
    current_file = 0
    folders_in_cwd = 0

    # Sets current working directory according to parameter
    os.chdir(str(sys.argv[1]))

    # Counts folders in CWD
    for pathname in os.listdir():
        if os.path.isdir(pathname):
            folders_in_cwd += 1
        else:
            pass

    # Number of files without folders for progress bar
    total_files = len(os.listdir()) - folders_in_cwd

    # Gets extension of each file, then creates/moves said file to folder.
    # Also adds progress bar.
    for file in os.listdir():
        ext = os.path.splitext(file)[1]
        if ext:
            try:
                os.mkdir(ext.replace('.', ''))
                os.rename(os.path.join(os.getcwd(), file), os.path.join(os.getcwd(), ext.replace('.', ''), file))
            except FileExistsError:
                os.rename(os.path.join(os.getcwd(), file), os.path.join(os.getcwd(), ext.replace('.', ''), file))
            current_file += 1
            print('\033[0K\r' + progress_bar(current_file, total_files, 20), end='')
        else:
            pass
