"""folder_manager package

Small utility to manage folders — starter module.
"""

__all__ = ["mkdir_if_missing"]

import os


def mkdir_if_missing(path: str) -> bool:
    """Create directory `path` if it doesn't exist.

    Returns True if directory was created, False if it already existed.
    Raises OSError on failure.
    """
    if os.path.isdir(path):
        return False
    os.makedirs(path, exist_ok=True)
    return True
