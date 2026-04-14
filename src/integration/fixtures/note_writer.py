class NoteWriter:
    """Writes and reads short text notes from a file.

    parameters:
        filepath -- path to the file to read and write

    methods:
        add(note)    -- append a note to the file
        all_notes()  -- return all notes as a list of strings
        count()      -- return the number of notes in the file
    """

    def __init__(self, filepath: str):
        """Initialise a NoteWriter that stores notes in the given file.

        parameters:
            filepath -- path to the file where notes are stored

        returns:
            none
        """
        self._filepath = filepath

    def add(self, note: str):
        """Append a single note as a new line in the file.

        parameters:
            note -- the text to append

        side-effects:
            appends one line to the file at self._filepath

        returns:
            none
        """
        with open(self._filepath, 'a', encoding='utf-8') as f:
            f.write(note + '\n')

    def all_notes(self) -> list:
        """Return all notes stored in the file as a list of strings.

        parameters:
            none

        returns:
            a list of strings, one entry per line, with trailing newlines stripped
        """
        with open(self._filepath, encoding='utf-8') as f:
            return [line.rstrip('\n') for line in f]

    def count(self) -> int:
        """Return the number of notes currently stored in the file.

        parameters:
            none

        returns:
            an integer count of notes
        """
        return len(self.all_notes())
