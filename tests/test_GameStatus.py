from unittest import TestCase
from levelup.character import Character
#from levelup.GameMap import GameMap
#from levelup.Position import Position

class GameStatus(TestCase):
    def GameStatus(Character,CurrentPosition,MoveCount):
        Character: String
        CurrentPosition: Integer
        MoveCount: Integer
        testobj = GameStatus(Character,CurrentPosition,MoveCount)
        self.assertEqual(GameStatus, testobj.GameStatus)