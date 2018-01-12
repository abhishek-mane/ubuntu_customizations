import os
import os.path as path
import inspect
import shutil
import config

# Print function
Print = config.Print
installPkg = config.apt.installPkg

# Globals
FILENAME = 'TEMPBASH'
HOME_DIR = os.environ['HOME']
PREREQ_PACKAGES = [
    'git',
    'toilet',
    'quote'
]


def doPrereq():
    ''' Install prereq pkgs '''
    for pkg in PREREQ_PACKAGES:
        installPkg(pkg)


def backupBashrc():
    src = path.join(HOME_DIR, FILENAME)
    dst = path.join(HOME_DIR, FILENAME + '.bak')
    shutil.copyfile(src, dst)


def getCustomizations():
    CURRENT_DIR = path.dirname(path.abspath(
        inspect.getfile(inspect.currentframe()))
    )
    LOCAL_BASHRC = path.join(CURRENT_DIR, 'bashrc')
    with open(LOCAL_BASHRC, 'r') as bashFile:
        return bashFile.read()


def rewriteBashrc(data):
    with open(path.join(HOME_DIR, FILENAME), 'a') as bashFile:
        bashFile.write('\n\n' + data)


def initialize():
    ''' Start of the module '''
    Print(__name__, 'Installing dependencies...')
    doPrereq()

    Print(__name__, 'Backing up bashrc file...')
    backupBashrc()

    Print(__name__, 'Modifying bashrc file...')
    rewriteBashrc(getCustomizations())
