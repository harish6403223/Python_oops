import threading
from Parking import *
from collections import defaultdict
from Vehicle import *
import time
from type import *


class GateSystem(threading.Thread):
    def __init__(s, parking : Parking):
        super().__init__()
        s.parking = parking
        s.lock = threading.Lock()
        s.vehicle_dict = defaultdict(None)

    def check_and_occupy(s, seq, vehicle: Vehicle):
        with s.lock:
            floor, slot_no =s.parking.check_lot(vehicle.vehicle_type, seq)
            if floor:
                vehicle.assign_details(floor, slot_no)
                s.vehicle_dict[vehicle.name_plate] = vehicle
                time.sleep(2)
                return True
            else: 
                time.sleep(2)
                return False
                
            
    def release_parking(s, name_plate):
        s.parking.release_lot(s.vehicle_dict[name_plate].floor, s.vehicle_dict[name_plate].parking_number)
        total_cost, time = s.vehicle_dict[name_plate].calculate_cost()
        del s.vehicle_dict[name_plate]
        return [total_cost, time]
        


class Gate:
    def __init__(s, gatesystem: GateSystem, name = "Gate1"):
        s.name = name
        s.gatesystem = gatesystem
        s.seq = list()

    def add_seq(s, seq_no):
        s.seq.append(seq_no)

    def remove_seq(s, seq_no):
        s.seq.remove(seq_no)

    def check_in(s, name_plate, vehicle_type):
        vehicle = None
        if(vehicle_type == Vehicle_Type.Bike):
            vehicle = Bike(name_plate)
        elif(vehicle_type == Vehicle_Type.Car):
            vehicle = Car(name_plate)
        else:
            print(f"Vehicle type {vehicle_type} got error while checking in at {s.name}  at {s.name}")
            return
        if s.gatesystem.check_and_occupy(s.seq, vehicle):
            print(f"Successfully completed check in for vehicle {name_plate}, vehicle type {vehicle.vehicle_type} at {s.name}")
        else:
            print(f"Failed to  check in for vehicle {name_plate}  at {s.name}")

    def check_out(s, name_plate):
        total_cost, time = s.gatesystem.release_parking(name_plate)
        print(f"Successfully completed check out for vehicle {name_plate} at {s.name} and total cost is {total_cost} for time differnce {time}")

