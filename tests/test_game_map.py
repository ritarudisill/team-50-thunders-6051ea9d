from unittest import TestCase
from unittest.mock import MagicMock, create_autospec
from levelup.GameMap import GameMap

# THIS IS AN EXAMPLE UNIT TEST. 
# All the unit tests for the Game Map Controller should go here
# Unit tests for other classes should be in their own .py files (like test_character.py)
class TestGameMap(TestCase):
    def test_init(self):
        testObj = GameMap()
        assert testObj.status != None
        
