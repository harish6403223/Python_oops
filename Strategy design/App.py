from WithStrategy import *
from WithStrategy.Strategy import NormalDriveStrategy

def main():
    veh = SportsVehicle()
    veh.drive()
    veh = GoodsVehicle()
    veh.drive()
    veh = OffRoadVehicle()
    veh.drive()



if __name__=="__main__":
    main()
