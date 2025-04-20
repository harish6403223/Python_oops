from .Strategy import SportsDriveStrategy

from .Vehicle import Vehicle

class OffRoadVehicle(Vehicle):
    def __init__(self):
        super().__init__(SportsDriveStrategy())