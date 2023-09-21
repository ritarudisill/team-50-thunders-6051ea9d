from levelup.character import Character

class TestCharacterInitWithName(Character):
    def test_init(self):
        DEFAULT_NAME = "MyName"
        testobj = Character(DEFAULT_NAME)
        self.assertEqual(DEFAULT_NAME, testobj.name)
        
