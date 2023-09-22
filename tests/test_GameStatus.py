from unittest import TestCase
from levelup.character import Character
#from levelup.GameMap import GameMap
#from levelup.Position import Position

class GameStatus(TestCase):
    def GameStatus(Character,CurrentPosition,MoveCount):
        Character: String = DEFAULT_NAME
        CurrentPosition: tuple = (-100, -100)
        MoveCount: Integer = 0
        testobj = GameStatus(Character,CurrentPosition,MoveCount)
        self.assertEqual(GameStatus, testobj.GameStatus)

## class GameStatus:
##   running: bool = False
##    character_name: str = DEFAULT_CHARACTER_NAME
##    ## NOTE - Game status will have this as a tuple. The Position should probably be in a class
##    current_position: tuple = (-100,-100)
 ##   move_count: int = 0 */