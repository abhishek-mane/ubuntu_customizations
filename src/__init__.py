import logger
import bash
from apt import updateSources
from fonts import installFonts


def apply():
    # Initialize the logger
    logger.initialize()

    # Update pkg sources
    updateSources()

    # # Bash customization
    bash.initialize()

    # Apps must have
    # code for installing apps

    # Install fonts
    installFonts()

    # # apply fonts
