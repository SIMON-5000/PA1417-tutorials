import pytest
from src.unit.fixtures.playlist import Playlist


# A fixture for unit tests is mostly about convenience.
#
# Without the fixture, every test below would have to repeat these
# four lines in its Arrange section:
#
#   playlist = Playlist("My Mix")
#   playlist.add_track("Song A")
#   playlist.add_track("Song B")
#   playlist.add_track("Song C")
#
# Technically a plain Python function would work identically here.
# We use a fixture because it is the pytest convention for shared
# setup, and it prepares you for integration tests where the fixture's
# teardown (yield) becomes genuinely necessary.
#
# Notice this fixture uses return, not yield. There is nothing to
# clean up — the playlist only exists in memory and is discarded
# automatically when the test finishes.

@pytest.fixture
def playlist():
    p = Playlist("My Mix")
    p.add_track("Song A")
    p.add_track("Song B")
    p.add_track("Song C")
    return p


def test_track_count(playlist):
    # Arrange
    # (handled by fixture)
    # Act
    result = playlist.track_count()
    # Assert
    assert result == 3


def test_contains_existing_track(playlist):
    # Arrange
    # (handled by fixture)
    # Act
    result = playlist.contains("Song A")
    # Assert
    assert result


def test_contains_missing_track(playlist):
    # Arrange
    # (handled by fixture)
    # Act
    result = playlist.contains("Song D")
    # Assert
    assert not result


def test_remove_track_decreases_count(playlist):
    # Arrange
    # (handled by fixture)
    # Act
    playlist.remove_track("Song B")
    result = playlist.track_count()
    # Assert
    assert result == 2


def test_remove_nonexistent_track_raises(playlist):
    # Arrange
    # (handled by fixture)
    # Act / Assert
    with pytest.raises(ValueError):
        playlist.remove_track("Song D")
