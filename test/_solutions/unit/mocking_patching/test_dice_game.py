from unittest.mock import patch
from src.unit.mocking_patching.dice_game import DiceGame


# DiceGame calls random.randint(1, 6) — a non-deterministic function.
# Tests that depend on random output are unreliable. We patch it to
# control the result and make each test deterministic.
#
# dice_game.py does "import random", so random is a name in that module's
# namespace. The patch path follows the import chain: src.dice_game.random.randint


def test_roll_returns_mocked_value():
    # Arrange
    with patch("src.unit.mocking_patching.dice_game.random.randint") as mock_randint:
        mock_randint.return_value = 4
        game = DiceGame()
        # Act
        result = game.roll()
        # Assert
        assert result == 4


def test_is_winner_when_roll_meets_target():
    # Arrange
    with patch("src.unit.mocking_patching.dice_game.random.randint") as mock_randint:
        mock_randint.return_value = 5
        game = DiceGame()
        # Act / Assert
        assert game.is_winner(5) is True


def test_is_not_winner_when_roll_below_target():
    # Arrange
    with patch("src.unit.mocking_patching.dice_game.random.randint") as mock_randint:
        mock_randint.return_value = 2
        game = DiceGame()
        # Act / Assert
        assert game.is_winner(5) is False
