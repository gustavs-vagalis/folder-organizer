import os
from math import floor


def progress_bar(progress, result, bar_length):
    fill = floor(progress / result * (bar_length - 2))
    empty = (bar_length - 2) - fill
    txt = "{} out of {} completed.".format(progress, result)
    bar = "[" + "#" * fill + " " * empty + "] " + txt
    return bar


current_file = 0
folders_in_cwd = 0 

os.chdir("/home/gustavs/Downloads")

for pathname in os.listdir():
    if os.path.isdir(pathname):
        folders_in_cwd += 1
    else:
        pass

total_files = len(os.listdir()) - folders_in_cwd

for file in os.listdir():
    ext = os.path.splitext(file)[1]
    if ext:
        try:
            os.mkdir(ext)
            os.rename(os.path.join(os.getcwd(), file), os.path.join(os.getcwd(), ext, file))
        except FileExistsError:
            os.rename(os.path.join(os.getcwd(), file), os.path.join(os.getcwd(), ext, file))
        current_file += 1
        print('\033[0K\r' + progress_bar(current_file, total_files, 20), end='')
    else:
        pass
