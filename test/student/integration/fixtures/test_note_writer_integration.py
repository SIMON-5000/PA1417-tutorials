import os
import pytest
from src.integration.fixtures.note_writer import NoteWriter

"""
Integration test for NoteWriter
"""

# TODO: Write integration tests for NoteWriter.

@pytest.fixture
def note_writer():
    note_writer = NoteWriter("test_file.txt")
    yield note_writer
    os.remove("test_file.txt")

@pytest.mark.integ
def test_note_writer_write(note_writer):
    note_writer.add("A new note")
    assert note_writer.all_notes() == ["A new note"]

@pytest.mark.integ
def test_note_writer_count(note_writer):
    note_writer.add("A new note")
    note_writer.add("A second note")
    assert note_writer.count() == 2

@pytest.mark.integ
def test_note_writer_read(note_writer):
    note_writer.add("A new note")
    note_writer.add("A second note")
    assert note_writer.all_notes() == ["A new note", "A second note"]
