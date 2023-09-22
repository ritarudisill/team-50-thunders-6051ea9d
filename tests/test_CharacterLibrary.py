from unittest import TestCase
from levelup.character import Character
from levelup.GameMap import GameMap
#from levelup.Position import Position

class TestCharacterWithName(TestCase):
    def test_with_default(self):
        DEFAULT_NAME = "MyName"
        testobj = Character(DEFAULT_NAME)
        self.assertEqual(DEFAULT_NAME, testobj.name)

    def test_with_name(self):
        name: String
        name = "Dorian"
        testobj = Character(name)
        self.assertEqual(name, testobj.name)
        
    def getName(self):
        name: String
        name = input("Input")
        testobj = Character(name)
        self.assertEqual(name, testobj.name)

    def enterMap(GameMap):
        MapName: String
       # MapName = ""
        testobj = map(MapName)
        self.assertEqual(MapName, testobj.MapName) 

    def getPosition():
        Position: String
        testobj = String(Position)
        self.assertEqual(Position, testobj.Position)

    def move(Direction): 
        Direction: String
        testobj = Direction(Direction)
        self.assertEqual(Direction, testobj.Direction)