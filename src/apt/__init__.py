'''
    * Module for managing apt packages
'''


def installPkg(pkg):
    from install import install
    install(pkg)


def installPkgs(listOfPkgs):
    from install import installFromRemote
    installFromRemote(listOfPkgs)


def updateSources():
    from update import update
    update()


def addPPA(ppa):
    from ppa import add
    add(ppa)
