import os
import shutil
import pytest
from src.integration.fixtures.file_cache import FileCache


@pytest.fixture
def cache():
    directory = "test_cache_dir"
    os.makedirs(directory)
    yield FileCache(directory)
    # Teardown: remove the entire directory and all files inside it
    shutil.rmtree(directory)


def test_key_does_not_exist_before_storing(cache):
    assert cache.has("greeting") is False


def test_stored_value_can_be_retrieved(cache):
    cache.store("greeting", "hello")
    assert cache.retrieve("greeting") == "hello"


def test_key_exists_after_storing(cache):
    cache.store("greeting", "hello")
    assert cache.has("greeting") is True


def test_two_keys_stored_independently(cache):
    cache.store("first", "one")
    cache.store("second", "two")
    assert cache.retrieve("first") == "one"
    assert cache.retrieve("second") == "two"


def test_overwrite_updates_value(cache):
    cache.store("key", "original")
    cache.store("key", "updated")
    assert cache.retrieve("key") == "updated"
