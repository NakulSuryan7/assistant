
import os
import shutil
from os import listdir
from os.path import isfile, join

import filetype

desktophello: str = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop\hello')
directory_i = "images"
parent_dir_i = desktophello
path_i = os.path.join(parent_dir_i, directory_i)
if not os.path.exists(path_i):
    os.mkdir(path_i)
directory_m: str = "music"
parent_dir_m = desktophello
path_m = os.path.join(parent_dir_m, directory_m)
if not os.path.exists(path_m):
    os.mkdir(path_m)
directory_v: str = "ideo"
parent_dir_v = desktophello
path_v = os.path.join(parent_dir_v, directory_v)
if not os.path.exists(path_v):
    os.mkdir(path_v)
directory_o: str = "others"
parent_dir_o = desktophello
path_o = os.path.join(parent_dir_o, directory_o)
if not os.path.exists(path_o):
    os.mkdir(path_o)


def main():
    desktopimages = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop\hello\images')
    desktopothers = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop\hello\others')
    desktopmusic = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop\hello\music')
    desktopideo = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop\hello\ideo')
    onlyfiles = [f for f in listdir(desktophello) if isfile(join(desktophello, f))]
    for x in onlyfiles:
        kind = filetype.guess(desktophello + "\\" + x)
        if kind is None:
            shutil.move(desktophello + "\\" + x, desktopothers + "\\" + x)
        elif kind.extension == 'jpg':
            shutil.move(desktophello + "\\" + x, desktopimages + "\\" + x)
        elif kind.extension == 'mp3':
            shutil.move(desktophello + "\\" + x, desktopmusic + "\\" + x)
        elif kind.extension == 'mp4':
            shutil.move(desktophello + "\\" + x, desktopideo + "\\" + x)


while True:
    main()