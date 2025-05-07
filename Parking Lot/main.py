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
    parkinglot1.print_details()
    time.sleep(0.1)
    parkinglot2 = ParkingLot("parkinglot2")
    parkinglot2.print_details()

    parking.add_parkinglot(1, parkinglot1)
    parking.add_parkinglot(2, parkinglot2)

    gatesystem = GateSystem(parking)

    entry_gate = Entry_gate(gatesystem)
    entry_gate.add_seq(1)
    entry_gate.add_seq(2)

    exit_gate = Exit_gate(gatesystem)


    print("starting chcekin and checkout")

    ticket1 = entry_gate.check_in("TS1", Bike, "Gate1")
    ticket2 = entry_gate.check_in("TS1.1", Bike, "Gate1", [2,1])
    ticket3 = entry_gate.check_in("TS2", Car, "Gate2")

    ticket4 = entry_gate.check_in("TS3", Bike, "Gate1", [2])

    exit_gate.check_out(ticket2)
    exit_gate.check_out(ticket1)

    ticket5 = entry_gate.check_in("TS4", Bike, "Gate2")

    exit_gate.check_out(ticket5)
    exit_gate.check_out(ticket3)
    exit_gate.check_out(ticket4)




    

