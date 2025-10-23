import os
import tempfile

from folder_manager import mkdir_if_missing


def test_mkdir_if_missing_creates_directory():
    tmpdir = tempfile.mkdtemp()
    newdir = os.path.join(tmpdir, "subdir")
    try:
        # ensure it doesn't exist yet
        assert not os.path.exists(newdir)
        created = mkdir_if_missing(newdir)
        assert created is True
        assert os.path.isdir(newdir)
        # calling again should return False
        created_again = mkdir_if_missing(newdir)
        assert created_again is False
    finally:
        # cleanup
        if os.path.isdir(newdir):
            os.rmdir(newdir)
        if os.path.isdir(tmpdir):
            os.rmdir(tmpdir)
