*** Settings ***
Documentation  I want to create my character. 
Test Template  TestCharacterInitWithName
Library        CharacterLibrary.py

*** Test Cases ***    DEFAULT_NAME  Name
test_init             Default       None
test_init             Blank         Dorian

*** Keywords ***
TestCharacterInitWithName
  [Arguments]  ${default_name}  ${name}
TestCharacterInitWithName ${default_name}
TestCharacterInitWithName ${name}


