import os
import sys
from subprocess import call

import random
import time


def getfolders(rootdir):
    folders = []
    listing = os.walk(rootdir)
    for listed in listing:
        folders.append(listed)
    return(folders)


def getpaths(rootdir):
    folders = getfolders(rootdir)
    paths = []

    for listed in folders:
        folder = listed[0]
        pictures = listed[2]
        for pic in pictures:
            paths.append(str(folder) + '/' + str(pic))

    return(paths)


def main(pictures, delay):
    while(True):
        randpic = random.randint(0, len(pictures))
        picture = pictures[randpic]
        argument = "--set-wallpaper=" + picture
        call(["pcmanfm", argument])
        time.sleep(delay)


if __name__ == "__main__":
    if len(sys.argv) == 3:
        parentDir = sys.argv[1]
        delay = eval(sys.argv[2])
        pictures = getpaths(parentDir)
        main(pictures, delay)
        sys.exit(0)
    else:
        print("invalid input.")
        print("use: python walpaperchanger.py pictureDir delay")
        sys.exit(1)
