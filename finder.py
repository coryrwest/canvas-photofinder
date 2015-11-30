#!/usr/bin/python

import os, sys, getopt

extensions = set(['.jpeg', '.jpg', '.gif', '.png'])


def walker(path):
    for root, dirs, files in os.walk(path):
        path = root.split('/')
        print (len(path) - 1) * '-', os.path.basename(root)
        for photo in files:
            if photo.endswith(tuple(extensions)):
                print photo


def main(argv):
    # Parse path
    path = ''
    try:
        opts, args = getopt.getopt(argv, 'hp:', ['path='])
    except getopt.GetoptError:
        print 'finder.py -p <path>'
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print 'finder.py -p <path>'
            sys.exit()
        elif opt in ("-p", "--path"):
            path = arg
    # Walk the path and get photos
    walker(path)

if __name__ == '__main__':
    main(sys.argv[1:])
