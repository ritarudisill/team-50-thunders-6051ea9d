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
            start_y += 1


        pass

    def isPositionValid(self: bool) -> None:
        pass

    def getTotalPositions(self, direction: int) -> None:
        pass
