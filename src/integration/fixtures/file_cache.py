import os


class FileCache:
    """A simple key-value store backed by individual files in a directory.

    Each key maps to a file named <key>.txt inside the cache directory.
    Because files persist on disk, tests that do not clean up the directory
    will observe stale data on subsequent runs.

    Methods:
        store(key, value)  — write value to <key>.txt
        retrieve(key)      — read and return the contents of <key>.txt
        has(key)           — return True if <key>.txt exists
    """

    def __init__(self, directory: str) -> None:
        """Initialise a FileCache that stores files in the given directory.

        parameters:
            directory -- path to the directory where cache files are stored

        returns:
            none
        """
        self._directory = directory

    def _path(self, key: str) -> str:
        """Return the full file path for the given cache key.

        parameters:
            key -- the cache key whose path to compute

        returns:
            the path to <key>.txt inside the cache directory
        """
        return os.path.join(self._directory, f"{key}.txt")

    def store(self, key: str, value: str) -> None:
        """Write a value to the cache file for the given key.

        parameters:
            key   -- the cache key used as the filename stem
            value -- the string to store

        side-effects:
            creates or overwrites the file at <directory>/<key>.txt

        returns:
            none
        """
        with open(self._path(key), "w", encoding="utf-8") as f:
            f.write(value)

    def retrieve(self, key: str) -> str:
        """Read and return the cached value for the given key.

        parameters:
            key -- the cache key to look up

        returns:
            the string previously stored under key
        """
        with open(self._path(key), "r", encoding="utf-8") as f:
            return f.read()

    def has(self, key: str) -> bool:
        """Return True if a cached value exists for the given key.

        parameters:
            key -- the cache key to check

        returns:
            True  -- if <key>.txt exists in the cache directory
            False -- if <key>.txt does not exist
        """
        return os.path.exists(self._path(key))
