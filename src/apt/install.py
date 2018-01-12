'''
    * Installs a specified package
'''

import os
import os.path as path
import stat
import inspect
import shutil
import config
import scripts

# define print function
Print = config.Print

CURRENT_DIR = path.dirname(path.abspath(
    inspect.getfile(inspect.currentframe()))
)

SCRIPTS_DIR = path.join(CURRENT_DIR, 'scripts')


def installFromRemote(pkg):
    COMMAND = "sudo apt-get install %s -y"
    os.system(COMMAND % (pkg))


def installFromLocal(pkg):
    HOME_DIR = os.environ['HOME']
    LOCAL_BIN = path.join(HOME_DIR, '.bin')
    if not path.exists(LOCAL_BIN):
        os.mkdir(LOCAL_BIN)
    shutil.copyfile(
        path.join(SCRIPTS_DIR, pkg),
        path.join(LOCAL_BIN, pkg)
    )
    st = os.stat(path.join(LOCAL_BIN, pkg))
    os.chmod(path.join(LOCAL_BIN, pkg), st.st_mode | stat.S_IEXEC)


def install(pkg):
    Print(__name__, 'Installing package %s...' % (pkg))
    if(scripts.exist(pkg)):
        installFromLocal(pkg)
        return
    installFromRemote(pkg)
