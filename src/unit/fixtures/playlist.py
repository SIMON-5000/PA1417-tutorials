class Playlist:
    """A named playlist that holds an ordered list of tracks.

    methods:
        add_track(track)    -- add a track to the end of the playlist
        remove_track(track) -- remove a track by name; raises ValueError if not found
        contains(track)     -- return True if the track is in the playlist
        track_count()       -- return the number of tracks in the playlist
    """

    def __init__(self, name: str):
        """Initialise a new empty playlist with the given name.

        parameters:
            name -- the display name for this playlist

        returns:
            none
        """
        self.name = name
        self._tracks = []

    def add_track(self, track: str):
        """Append a track to the end of this playlist.

        parameters:
            track -- the name of the track to add

        returns:
            none
        """
        self._tracks.append(track)

    def remove_track(self, track: str):
        """Remove the first occurrence of a track from this playlist.

        parameters:
            track -- the name of the track to remove

        returns:
            none

        raises:
            ValueError -- if track is not in the playlist
        """
        if track not in self._tracks:
            raise ValueError(f"'{track}' is not in the playlist")
        self._tracks.remove(track)

    def contains(self, track: str) -> bool:
        """Return True if the given track is present in this playlist.

        parameters:
            track -- the name of the track to look for

        returns:
            True  -- if track is present in the playlist
            False -- if track is not present in the playlist
        """
        return track in self._tracks

    def track_count(self) -> int:
        """Return the number of tracks currently in this playlist.

        parameters:
            none

        returns:
            an integer count of tracks
        """
        return len(self._tracks)
