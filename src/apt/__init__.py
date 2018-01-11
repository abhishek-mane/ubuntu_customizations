'''
    * Module for managing apt packages
'''


def installPkg(pkg):
    from install import install
    install(pkg)


def updateSources():
    from update import update
    update()
