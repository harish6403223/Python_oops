from .Strategy import NormalDriveStrategy

from .Vehicle import Vehicle

class GoodsVehicle(Vehicle):
    def __init__(self):
        super().__init__(NormalDriveStrategy())