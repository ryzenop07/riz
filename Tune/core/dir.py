import os
from Tune.logging import LOGGER

def create_directories():
    """Create necessary directories"""
    directories = [
        "downloads",
        "cache", 
        "logs",
        "assets/temp"
    ]
    
    for directory in directories:
        if not os.path.exists(directory):
            os.makedirs(directory)
    
    LOGGER(__name__).info("Directories Updated.")