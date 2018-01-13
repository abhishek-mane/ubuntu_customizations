import config
import logger
import bash
import fonts
import fav_apps

# Print
Print = config.Print
apt = config.apt


def apply():
    # Initialize the logger
    logger.initialize()

    # Update pkg sources
    apt.updateSources()

    # # Bash customization
    bash.initialize()

    # Install fonts
    fonts.install()

    # Install my fav apps
    fav_apps.install()

    # Restart terminal
    Print(__name__, 'Done !')
    Print(__name__, 'Please restart your terminal.')