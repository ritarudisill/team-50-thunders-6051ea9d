*** Settings ***
Documentation  I want to create my character. 
Test Template  TestCharacterInitWithName
Library        test_character.py

*** Test Cases ***    DEFAULT_NAME  Name
Default name when none  Default     None
Accept name when given  Blank       Dorian

*** Keywords ***
TestCharacterInitWithName
  [Arguments]  ${default_name}  ${name}
Initialize character  ${default_name}
Initialize character with ${name}


