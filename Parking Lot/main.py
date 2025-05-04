from Gate import *
from type import *
from Parking import *
from Vehicle import *
import time

Bike = Vehicle_Type.Bike
Car = Vehicle_Type.Car

if __name__ == "__main__":
    parking = Parking()

    parkinglot1 = ParkingLot("parkinglot1")
    parkinglot2 = ParkingLot("parkinglot2")

    parking.add_parkinglot(1, parkinglot1)
    parking.add_parkinglot(2, parkinglot2)

    gatesystem = GateSystem(parking)

    gate1 = Gate(gatesystem, "Gate1")
    gate1.add_seq(1)
    gate1.add_seq(2)

    gate2 = Gate(gatesystem, "Gate2")
    gate2.add_seq(2)
    gate2.add_seq(1)

    print("starting chcekin and checkout")

    gate1.check_in("TS1", Bike)
    gate1.check_in("TS1.1", Bike)
    gate1.check_in("TS2", Car)

    gate2.check_in("TS3", Bike)

    gate2.check_out("TS1")
    gate2.check_out("TS1.1")

    gate2.check_in("TS4", Bike)

    gate1.check_out("TS2")
    gate1.check_out("TS3")
    gate1.check_out("TS4")




    

