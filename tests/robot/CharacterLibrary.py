from levelup.character import Character

class TestCharacterInitWithName(Character):
    def test_init_with_default(Character):
        DEFAULT_NAME = "MyName"
        testobj = Character(DEFAULT_NAME)
        self.assertEqual(DEFAULT_NAME, testobj.name)

    def test_init_with_name(Character):
        name: String
        name = "Dorian"
        testobj = Character(name)
        self.assertEqual(name, testobj.name)
