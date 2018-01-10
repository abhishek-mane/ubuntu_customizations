import                  \
    os,                 \
    os.path as path,    \
    shutil,             \
    logging as logger

# Globals
FILENAME = 'TEMPBASH'
HOME_DIR = os.environ['HOME']
PREREQ_PACKAGES = [
    'git'
]

def doPrereq():
    print "test"

def backupBashrc():
    src = path.join(HOME_DIR, FILENAME)
    dst = path.join(HOME_DIR, FILENAME + '.bak')
    shutil.copyfile(src, dst)

def getCustomizations():
    with open('./bashrc', 'r') as bashFile:
        return bashFile.read()

def rewriteBashrc(data):
    with open(path.join(HOME_DIR, FILENAME), 'a') as bashFile:
        bashFile.write('\n\n'+data)


def initialize():
    logger.info('Installing dependencies...')
    # required dependencies
    logger.info('Backing up bashrc file...')
    backupBashrc()
    logger.info('modifying bashrc file')
    rewriteBashrc(getCustomizations())