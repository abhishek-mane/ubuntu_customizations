'''
    * Module is for installing fonts
'''

import os
import os.path as path
import inspect
import shutil
import config

# Print function
Print = config.Print

HOME_DIR = os.environ['HOME']
FONTS_DIR = path.join(HOME_DIR, '.fonts')


def createFontsDirectory():
    if not path.exists(FONTS_DIR):
        os.mkdir(FONTS_DIR)


def copyFonts():
    currentDir = path.dirname(path.abspath(
        inspect.getfile(inspect.currentframe())))
    localFontsDir = path.join(currentDir, 'fonts')
    for subdir, dirs, files in os.walk(localFontsDir):
        for file in files:
            Print(__name__, 'Installing font %s...' % (file))
            shutil.copyfile(
                path.join(subdir, file),
                path.join(FONTS_DIR, file)
            )


def loadInstalledFonts():
    os.system('fc-cache -f -v')


def install():
    Print(__name__, 'Checking fonts directory...')
    createFontsDirectory()

    Print(__name__, 'Installing fonts...')
    copyFonts()

    Print(__name__, 'Loading installed fonts...')
    loadInstalledFonts()
