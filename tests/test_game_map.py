from unittest import TestCase
from unittest.mock import MagicMock, create_autospec
from levelup.GameMap import GameMap

# THIS IS AN EXAMPLE UNIT TEST. 
# All the unit tests for the Game Map Controller should go here
# Unit tests for other classes should be in their own .py files (like test_character.py)
class TestGameMap(TestCase):
    def test_gameset_map(self):
        testObj = GameMap()
        assert testObj.status != None

        
class TestCalculatePosition(GameMap):
    def test_calc_position(GameMap):
        start_x  = 1
        start_y = 1
        direction = "E"
        testobj = calculatePositions(start_x,start_y, direction)
        self.assertEqual(start_x,start_y, direction)