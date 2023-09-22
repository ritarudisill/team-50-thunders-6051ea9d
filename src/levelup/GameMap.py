import logging
from dataclasses import dataclass
#from enum import Enum
from levelup.controller import GameController

#TODO: ADD THINGS YOU NEED FOR STATUS
class MapStatus:
    numPositions: int = 100
    #running: bool = False

#class Direction(Enum):
    #NORTH = "n"
    #SOUTH = "s"
    #EAST = "e"
    #WEST = "w"

class GameMap:
    status: MapStatus

    def __init__(self): 
        self.status = MapStatus()

    def getPositions(self):
        pass

    def calculatePositions(self,start_x,start_y, direction) -> None:
        self.start_x=start_x
        self.start_y=start_y
        if direction == "E":
            self.start_y += 1

        if direction == "W":
            self.start_x -= 1
        pass

    def isPositionValid(self,start_x,start_y) -> bool:
        self.start_x=start_x
        self.start_y=start_y
        if (self.start_x <= 0) or (self.start_y <= 0):
            return False



        pass

    def getTotalPositions(self, direction: int) -> None:
        pass
