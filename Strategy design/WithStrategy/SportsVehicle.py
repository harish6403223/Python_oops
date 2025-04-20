from .Strategy import *

from .Vehicle import Vehicle

class SportsVehicle(Vehicle):
    def __init__(self):
        t=SportsDriveStrategy()
        super().__init__(t)