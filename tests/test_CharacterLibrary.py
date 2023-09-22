from unittest import TestCase
from levelup.character import Character

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
        name = "Dorian"
        testobj = Character(name)
        self.assertEqual(name, testobj.name)

    def enterMap(GameMap):
        MapName: String
       # MapName = ""
        testobj = map(MapName)
        self.assertEqual(MapName, testobj.MapName) 