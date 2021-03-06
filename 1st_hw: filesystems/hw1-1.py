from os import listdir, remove, link
from os.path import isfile, join
from filecmp import cmp
from itertools import combinations
import sys


def get_files(path):
    '''
    Returns list of filenames from given path, ignoring folders if any.

    Parameters:
        path (str): path to the folder

    Returns:
        list of the filenames from given path
    '''
    return [file for file in listdir(path) if isfile(join(path, file))]


def create_hardlinks(path):
    '''
    Disk space management.
    Creates hardlinks to the same files if any.
    '''
    files_list = get_files(path)

    for file1, file2 in combinations(files_list, 2):
        if cmp(join(path, file1), join(path, file2)):
            remove(join(path, file1))
            link(join(path, file2), join(path, file1))


def main(path):
    '''
    How to run:
        python3 hw1-1.py /absolute/path/to/the/folder

    This program was tested on actual movies: 9.2GBx2 and 732MBx3 samples.
    Worked smoothly in less than a minute. Check hw1-1.*.jpg screenshot.
    '''
    create_hardlinks(path)


if __name__ == '__main__':
    main(sys.argv[1])