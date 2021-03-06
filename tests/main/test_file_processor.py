""" Tests for FileProcessor class. """
import tempfile
from datetime import datetime
from pathlib import Path

from main.file_processor import FileProcessor


def test_init(writable_path):
    """Unit test for initializer."""
    file_processor = FileProcessor("dummy_file", writable_path, None)
    assert isinstance(file_processor.file_object, Path)
    assert file_processor.date.replace(microsecond=0) == datetime.today().replace(
        microsecond=0
    )

    dummy_path = "/dummy"
    dummy_date = datetime(2022, 1, 1)
    file_processor = FileProcessor("dummy_file", path=dummy_path, date=dummy_date)
    assert file_processor.path == Path(dummy_path)
    assert file_processor.date == dummy_date


def test_file_exists(writable_path):
    """Unit test for file_exists()."""
    file_processor = FileProcessor("non_existent_file", writable_path, None)
    assert not file_processor.file_exists()
    with tempfile.TemporaryFile(dir=file_processor.path) as temp:
        name = temp.name.replace("\\", "/").split("/")[-1]
        file_processor = FileProcessor(name, writable_path, None)
        assert file_processor.file_exists()


def test_archive(writable_path):
    """Unit test for archive()."""
    file_processor = FileProcessor("dummy", writable_path, None)
    with open(file_processor.path / "dummy", "wb") as _:
        pass
    archived_file = file_processor.archive()
    new_location = Path(archived_file)
    assert new_location.exists()
    new_location.unlink()
    file_processor.file_object.unlink()
