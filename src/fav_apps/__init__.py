
import config

# Get apt package
apt = config.apt

PPAs = [
    'ppa:apt-fast/stable',              # apt-fast
    'ppa:numix/ppa',                    # numix-folders, numix-icon-theme-circle,
    'ppa:peek-developers/stable',       # peek
    'ppa:webupd8team/y-ppa-manager',    # y-ppa-manager
    'ppa:nilarimogard/webupd8',         #
    'ppa:nathan-renniewaldock/flux',    # f.lux
]

PKGS = [
    # From added PPA's
    'apt-fast',
    'numix-folders', 'numix-icon-theme-circle',
    'peek',
    'y-ppa-manager',
    'woeusb',
    'fluxgui',

    # From main sources
    'tree',
    'build-essential',
    'filezilla',
    'gparted',
    'geany',
    'guake',
    'bleachbit',
    'vim',
    'wget',
    'curl',
    'vlc',
    'samba',
    'network-manager',
    'network-manager-openvpn',
    'network-manager-openvpn-gnome',
    'remmina',
    'winusb',
]


def addPPAs():
    for ppa in PPAs:
        apt.addPPA(ppa)


def refreshSources():
    apt.updateSources()


def installPackages():
    apt.installPkgs(PKGS)


def install():
    addPPAs()
    refreshSources()
    installPackages()



# To be accomodate
# typora
# gitbook editor