#!/usr/bin/python
import os
import sys
from subprocess import call,Popen,PIPE

from random import choice
from time import sleep


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
        picture = random.choice(pictures)
        argument = "--set-wallpaper=" + picture
        call(["pcmanfm", argument])
        time.sleep(delay)


if __name__ == "__main__":
    p=Popen(("ps","-e"),stdout=PIPE)
    if call(("grep","pcmanfm"),stdin=p.stdout,stdout=PIPE)==1:
        print("PCMan File Manager not running.")
        sys.exit(1)
    if len(sys.argv) == 3:
        parentDir = sys.argv[1]
        if not os.path.isdir(parentDir):
            print("Can't open directory '"+parentDir+"'.")
            sys.exit(1)
        delay = eval(sys.argv[2])
        pictures = getpaths(parentDir)
        if len(pictures)==0:
            print("No files found in '"+parentDir+"'.")
            exit(1)
        main(pictures, delay)
        sys.exit(0)
    else:
        print("invalid input.")
        print("use: python walpaperchanger.py pictureDir delay")
        sys.exit(1)
