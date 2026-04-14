import csv


class CsvLogger:
    """Appends rows to a CSV file on disk.

    Because each call to log() appends to the file rather than overwriting
    it, tests that do not clean up the file will see stale rows on subsequent
    runs.

    Methods:
        log(row)     — append a list of values as one CSV row
        row_count()  — return the number of rows currently in the file
        read_all()   — return all rows as a list of lists of strings
    """

    def __init__(self, filepath: str) -> None:
        """Initialise a CsvLogger that writes to the given file.

        parameters:
            filepath -- path to the CSV file to write to

        returns:
            none
        """
        self._filepath = filepath

    def log(self, row: list) -> None:
        """Append a row of values to the CSV file.

        parameters:
            row -- a list of values to write as a single CSV row

        side-effects:
            appends one row to the CSV file at self._filepath

        returns:
            none
        """
        with open(self._filepath, "a", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(row)

    def row_count(self) -> int:
        """Return the number of rows currently in the CSV file.

        parameters:
            none

        returns:
            an integer count of rows
        """
        return len(self.read_all())

    def read_all(self) -> list[list[str]]:
        """Return every row in the CSV file as a list of string lists.

        parameters:
            none

        returns:
            a list of rows, where each row is a list of strings
        """
        with open(self._filepath, "r", encoding="utf-8") as f:
            reader = csv.reader(f)
            return [row for row in reader if row]
