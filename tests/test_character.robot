*** Settings ***
Documentation  I want to create my character and give it a name that the player provides. If the player doesn't provide a name, default it.
Test Template  TestCharacterInitWithName
Library        test_CharacterLibrary.py

*** Test Cases ***        CharacterName
test_with_default         MyName
test_with_name            Dorian

*** Keywords ***
TestCharacterInitWithName
    [Arguments]                  ${characterName}
    Test Character With Name     ${characterName}


