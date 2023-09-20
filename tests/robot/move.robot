*** Settings ***
Documentation     I want to move my character. If they attempt to move past a boundary, the move results in no change in position.
...    Example test case using the data-driven (table) syntax.
...    https://github.com/level-up-program/team-50-thunders-6051ea9d/blob/main/tests/robot/images/WIN_20230920_15_26_53_Pro.jpg
...    https://github.com/level-up-program/team-50-thunders-6051ea9d/blob/main/tests/robot/images/lvlup.jpg
...    https://github.com/level-up-program/team-50-thunders-6051ea9d/blob/main/tests/robot/images/WIN_20230920_15_30_14_Pro.jpg
Test Template     Move character
Library           MoveLibrary.py

*** Test Cases ***                  StartingX     StartingY     StartingMoveCount     Direction     EndingX     EndingY     EndingMoveCount
Move in the middle of the board     0             0             1                     NORTH         0           1           2
Move on the edge of the board       0             0             5                     SOUTH         0           0           6
Move right in middle                5             6             1                     EAST          5           7           2
Move left in middle                 5             6             2                     WEST          5           5           3
Move up in middle                   5             6             3                     NORTH         4           6           4
Move down in middle                 5             6             4                     SOUTH         6           6           5
Corner left move up                 1             1             5                     NORTH         1           1           6
Corner left move left               1             1             6                     WEST          1           1           7
Corner right move up                1             10            7                     NORTH         1           10          8
Corner right move right             1             10            8                     EAST          1           10          9
Corner lower right move down        10            10            9                     SOUTH         10          10          10
Corner lower right move right       10            10            10                    EAST          10          10          11
Corner lower left move down         10            1             11                    SOUTH         10          1           12
Corner lower left move left         10            1             12                    WEST          10          1           13
Middle row border move up           1             5             13                    NORTH         1           5           14
Middle row border move left         5             1             14                    WEST          5           1           15
Middle row bottom move down         10            5             15                    SOUTH         10          5           16
Middle row bottom move right        5             10            16                    EAST          5           10          17


*** Keywords ***
Move character
    [Arguments]    ${startingX}    ${startingY}    ${startingMoveCount}    ${direction}    ${endingX}    ${endingY}    ${endingMoveCount}
    Initialize character xposition with  ${startingX}
    Initialize character yposition with  ${startingY}
    Initialize character moveCount with  ${startingMoveCount}
    Move in direction                    ${direction}
    Character xposition should be        ${endingX}
    Character yposition should be        ${endingY}
    Character moveCount should be        ${endingMoveCount}
