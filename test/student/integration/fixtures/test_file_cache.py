from src.integration.fixtures.file_cache import FileCache
import os
import pytest
import shutil

@pytest.fixture
def file_cache():
    os.mkdir("test_dir")
    file_cache = FileCache("test_dir")
    yield file_cache
    shutil.rmtree("test_dir")

@pytest.mark.integ
@pytest.mark.parametrize("method_name, key, value, expected", [
    ("has", "my_key", "my_value", True),
    ("retrieve", "my_key", "my_value", "my_value"),
    ])
def test_file_cache_store(file_cache, method_name, key, value, expected):
    file_cache.store(key, value)
    # Kan vara användbart.
    method = getattr(file_cache, method_name)
    assert method(key) == expected
