import threading
from Parking import *
from collections import defaultdict
from Vehicle import *
import time
from type import *
from Payment_startegy import *


class GateSystem(threading.Thread):
    def __init__(s, parking : Parking):
        super().__init__()
        s.parking = parking
        s.lock = threading.Lock()
        s.vehicle_dict = defaultdict(None)

    def check_and_occupy(s, seq, vehicle: Vehicle):
        with s.lock:
            ticket =s.parking.check_lot(vehicle, vehicle.vehicle_type, seq)
            if ticket:
                details = ticket.retrieve_details()
                total_time = vehicle.assign_details(details[-2], details[-4], details[0])
                ticket.assign_time(total_time)
                s.vehicle_dict[vehicle.name_plate] = vehicle
                time.sleep(2)
                return ticket
            else: 
                time.sleep(2)
                return False
                
            
    def release_parking(s, ticket: Ticket):
        details = ticket.retrieve_details()
        if details[1] in s.vehicle_dict and s.vehicle_dict[details[1]].ticket_number == details[0]:
            response = s.parking.release_lot(ticket)
            if response:
                total_cost, time = s.vehicle_dict[details[1]].calculate_cost()
                del s.vehicle_dict[details[1]]
                return [total_cost, time, details[1]]
        else:
            print("Ticket doesn't exist")
        return [None, None]


class Entry_gate:
    def __init__(s, gatesystem: GateSystem):
        s.gatesystem = gatesystem
        s.seq = list()

    def add_seq(s, seq_no):
        s.seq.append(seq_no)

    def remove_seq(s, seq_no):
        s.seq.remove(seq_no)

    def check_in(s, name_plate, vehicle_type, entry_gate,  seq =None):
        vehicle = None
        if(vehicle_type == Vehicle_Type.Bike):
            vehicle = Bike(name_plate)
        elif(vehicle_type == Vehicle_Type.Car):
            vehicle = Car(name_plate)
        else:
            print(f"Vehicle type {vehicle_type} got error while checking in at {entry_gate}  at {entry_gate}")
            return
        if not seq:
            seq= s.seq
        ticket = s.gatesystem.check_and_occupy(seq, vehicle)
        if ticket:
            ticket.print_details()
            print(f"Successfully completed check in for vehicle {name_plate}, vehicle type {vehicle.vehicle_type} at {entry_gate}")
            return ticket
        else:
            print(f"Failed to  check in for vehicle {name_plate}  at {entry_gate}")
            return None

class Exit_gate:
    def __init__(self, gatesystem: GateSystem):
        self.gatesystem = gatesystem

    def check_out(s, ticket):
        ticket.print_details()
        total_cost, time, name_plate = s.gatesystem.release_parking(ticket)
        if total_cost:
            payment_strategy = Payment_strategy()
            payment_strategy.payment_service(total_cost)
            print(f"Successfully completed check out for vehicle {name_plate} at Exit_gate and total cost is {total_cost} for time differnce {time}")

    


