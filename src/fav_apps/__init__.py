
import config

# Get apt package
apt = config.apt

PPAs = [
    'ppa:apt-fast/stable',              # apt-fast
    'ppa:numix/ppa',                    # numix-folders, numix-icon-theme-circle,
    'ppa:peek-developers/stable',       # peek
    'ppa:webupd8team/y-ppa-manager',    # y-ppa-manager
    'ppa:nilarimogard/webupd8',         #
]

PKGS = [
    # From added PPA's
    'apt-fast',
    'numix-folders', 'numix-icon-theme-circle',
    'peek',
    'y-ppa-manager',
    'woeusb',

    # From main sources
    'build-essential',
    'filezilla',
    'gparted',
    'geany',
    'guake',
    'vim',
    'wget',
    'curl',
    'vlc',
    'network-manager-openvpn',
    'network-manager-openvpn-gnome',
    'remmina'
]


def addPPAs():
    for ppa in PPAs:
        apt.addPPA(ppa)


def installPackages():
    apt.installPkgs(PKGS)


def install():
    addPPAs()
    installPackages()
