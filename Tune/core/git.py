import os
from git import Repo
from Tune.logging import LOGGER

def check_git():
    """Check git status"""
    try:
        if os.path.exists(".git"):
            LOGGER(__name__).info("Git Client Found [VPS DEPLOYER]")
        else:
            LOGGER(__name__).info("Git Client Not Found [LOCAL DEPLOYER]")
    except Exception:
        LOGGER(__name__).info("Git Client Not Found [LOCAL DEPLOYER]")