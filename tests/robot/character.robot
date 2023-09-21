*** Settings ***
Documentation  I want to create my character and give it a name that the player provides. If the player doesn't provide a name, default it.
Test Template  TestCharacterInitWithName
Library        CharacterLibrary.py

*** Test Cases ***    DEFAULT_NAME  Name
test_init             MyName        None
test_init             Null          Dorian

*** Keywords ***
TestCharacterInitWithName
    [Arguments]  ${DEFAULT_NAME}  ${name}
    Test Character Init With Name     ${DEFAULT_NAME}
    Test Character Init With Name     ${name}


