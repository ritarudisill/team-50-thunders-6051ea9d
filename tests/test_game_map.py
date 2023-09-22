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

        
class TestCalculatePosition(TestCase):
    def test_calc_position(self):
        start_x  = 1
        start_y = 1
        direction = "E"
        testObj = GameMap()
        testObj.calculatePositions(start_x,start_y,direction)
        self.assertEqual(testObj.start_x,1)
        self.assertEqual(testObj.start_y,2)

class TestInvalidPosition(TestCase):
    def test_calc_position(self):
        start_x  = 0
        start_y = 0
        direction = "W"
        testObj = GameMap()

        isvalid = testObj.isPositionValid(start_x,start_y)
        self.assertEqual(isvalid,False)
  