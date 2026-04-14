import os
import pytest
from src.integration.fixtures.note_writer import NoteWriter


# This is an integration test — NoteWriter touches a real file on disk,
# so it is no longer testing logic in isolation.
#
# This is where a fixture with teardown becomes genuinely necessary,
# not just convenient. A plain Python function could create the file
# before the test, but it has no way to delete it afterwards.
#
# Without teardown, the file stays on disk after each test. The next
# test then opens a file that already contains notes from the previous
# test, and the counts are wrong. The failure is order-dependent and
# hard to diagnose.
#
# yield solves this. Everything before yield is setup (runs before the
# test). Everything after yield is teardown (runs after the test,
# whether it passed or failed).

@pytest.fixture
def writer():
    filepath = "test_notes.txt"
    # Setup: create an empty file for the test to use
    # Opening in 'w' mode creates the file if it does not exist and
    # truncates it to empty if it does. We have nothing to write, so
    # the body is pass. The with statement ensures the file handle is
    # closed safely even if an exception occurs.
    with open(filepath, 'w', encoding='utf-8'):
        pass
    w = NoteWriter(filepath)
    yield w
    # Teardown: delete the file so it does not affect the next test
    os.remove(filepath)


def test_count_starts_at_zero(writer):
    # Arrange
    # (handled by fixture)
    # Act
    result = writer.count()
    # Assert
    assert result == 0


def test_add_increases_count(writer):
    # Arrange
    # (handled by fixture)
    # Act
    writer.add("buy milk")
    result = writer.count()
    # Assert
    assert result == 1


def test_all_notes_returns_added_note(writer):
    # Arrange
    # (handled by fixture)
    # Act
    writer.add("buy milk")
    result = writer.all_notes()
    # Assert
    assert result == ["buy milk"]


def test_multiple_notes_are_stored(writer):
    # Arrange
    # (handled by fixture)
    # Act
    writer.add("buy milk")
    writer.add("call dentist")
    result = writer.all_notes()
    # Assert
    assert result == ["buy milk", "call dentist"]
