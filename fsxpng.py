import os
from PIL import Image, ImageFilter
import shutil
"""
Converts FSX BMP screenshots to PNG
"""


def pick_number():
    """
    Asks user for number to start with
    """
    still_going = True
    while still_going:
        number = raw_input("What number should I start on? ")
        try:
            number = int(number)
            still_going = False
            return number
        except ValueError:
            print 'Couldn\'t convert "{}" to an integer'.format(number)


def bmptopng(file_, number, newpath, basefile, filename_='Me'):
    """
    Converts BMP images to PNG
    @:param file_ : a filename
    @:param number : a number to append to the filename
    @:param newpath : folder path for the PNG image to go
    @:param basefile : the parent folder absolute path
    """
    if 'DS_Store' not in file_ and '.' in file_:
        filename = '{}{}.PNG'.format(filename_, number)
        try:
            im = Image.open(file_)
            im = im.filter(ImageFilter.SHARPEN)
            im.save(filename)
            print 'Created {}'.format(filename)
            shutil.move(os.path.join(basefile, filename), newpath)
        except IOError as e:
            print 'Unable to convert "{}" because of {}'.format(filename, e)


def run_converter():
    """
    Runs the program
    """
    numbers = pick_number()
    folderpaths = ''
    while True:
        folderpaths = raw_input('What is the absolute folder path of the pictures? ')
        if not os.path.exists(folderpaths):
            print '"{}" isn\'t a valid folder path!'.format(folderpaths)
        else:
            break
    base = os.path.split(folderpaths)[0]
    newfolderpath = os.path.join(base, 'newpics')
    os.mkdir(newfolderpath)
    os.chdir(folderpaths)

    for photo in os.listdir(folderpaths):
        bmptopng(photo, numbers, newfolderpath, base)
        numbers += 1
    print 'Converted {} images!'.format(len([name for name in os.listdir(newfolderpath) if 'Me' in name]))
    print 'New images located in {}     (probably at the bottom)'.format(newfolderpath)


if __name__ == '__main__':
    run_converter()
