import os
import pytest
from src.integration.fixtures.csv_logger import CsvLogger


@pytest.fixture
def logger():
    filepath = "test_log.csv"
    # Setup: create an empty file so CsvLogger has something to open
    with open(filepath, "w", encoding="utf-8"):
        pass
    yield CsvLogger(filepath)
    # Teardown: delete the file so the next test starts clean
    os.remove(filepath)


def test_new_file_has_zero_rows(logger):
    assert logger.row_count() == 0


def test_log_one_row_increases_count(logger):
    logger.log(["2024-01-01", "event_a"])
    assert logger.row_count() == 1


def test_log_two_rows_increases_count(logger):
    logger.log(["2024-01-01", "event_a"])
    logger.log(["2024-01-02", "event_b"])
    assert logger.row_count() == 2


def test_read_all_returns_logged_data(logger):
    logger.log(["2024-01-01", "login"])
    logger.log(["2024-01-02", "logout"])
    rows = logger.read_all()
    assert rows[0] == ["2024-01-01", "login"]
    assert rows[1] == ["2024-01-02", "logout"]
