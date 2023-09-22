from unittest import TestCase
from levelup.character import Character

class TestCharacterInitWithName(TestCase):
    def test_init(self):
        DEFAULT_NAME = "MyName"
        testobj = Character(DEFAULT_NAME)
        self.assertEqual(DEFAULT_NAME, testobj.name)

    def test_init(self):
        name: String    
        name = "Dorian"
        testobj = Character(name)
        self.assertEqual(name, testobj.name)
