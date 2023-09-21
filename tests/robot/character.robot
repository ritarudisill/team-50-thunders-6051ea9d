*** Settings ***
Documentation  I want to create my character. 
Test Template  TestCharacterInitWithName
Library        CharacterLibrary.py

*** Test Cases ***    DEFAULT_NAME  Name
Default name when none  Default     None
Accept name when given  Blank       Dorian

*** Keywords ***
TestCharacterInitWithName
  [Arguments]  ${default_name}  ${name}
TestCharacterInitWithName ${default_name}
TestCharacterInitWithName ${name}


