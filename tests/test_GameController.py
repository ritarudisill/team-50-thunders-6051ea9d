from unittest import TestCase
from enum import Enum
#from levelup.character import Character
#from levelup.GameMap import GameMap
#from levelup.Position import Position

class GameController(TestCase):
    def MovePosition(MovePosition):
        MovePosition: Direction
        testobj = MovePosition(Direction)
        self.assertEqual(MovePosition, testobj.MovePosition)

    def Character(Character):
        Character: String
        testobj = Character(String)
        self.assertEqual(Character, testobj.Character)    


    def StartGame():
        StartPositionX: Integer
        StartPositionY: Integer
        CreateCharacter: String
        MoveCount: Integer
        testobj = StartGame(String,Integer)
        self.assertEqual(StartGame, testobj.StartGame) 

class Direction(Enum):
    NORTH = "n"
    SOUTH = "s"
    EAST = "e"
    WEST = "w"