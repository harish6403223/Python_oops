from collections import defaultdict
from type import *
from Vehicle import Vehicle
from Ticket import *

class Parking_spot:
    def __init__(s, name_plate, vehicle_type):
        s.name_plate= name_plate
        s.vehicle_type = vehicle_type
    
    def spot_details(s):
        return [s.name_plate, s.vehicle_type]
    

class Floor:
    def __init__(s, id, slots = None):
        s.id =id 
        s.free_slots = slots
        if not slots:
            s.free_slots = set()
            for i in range(1, 11):
                s.free_slots.add(i)
        s.occupied = defaultdict(lambda:None)

    def add_slot(s, slot, vehicle: Vehicle):
        s.free_slots.remove(slot)
        name_plate, vehicle_type, _ = vehicle.retrieve_vehicle_details()
        s.occupied[slot] = Parking_spot(name_plate, vehicle_type)
        ticket = s.generate_ticket(name_plate, vehicle_type, slot)
        print(f"Free slots: {s.free_slots}")
        print("Occupied slots: ")
        for i in s.occupied:
            print(i, end=" ")
        print("")
        return ticket

    def remove_slot(self, slot:int):
        self.free_slots.add(slot)
        self.occupied.pop(slot)
        print(f"Free slots: {self.free_slots}")
        print("Occupied slots: ")
        for i in self.occupied:
            print(i, end=" ")
        print("")

    def check_free_slot(s, vehicle: Vehicle):
        for slot in s.free_slots:
            ticket = s.add_slot(slot, vehicle)
            return ticket
        return None
    
    def generate_ticket(s, name_plate, vehicle_type, slot):
        return Ticket(name_plate, vehicle_type, slot)
    
    def verify_spot(s, ticket: Ticket):
        name_plate, vehicle_type, slot = ticket.retrieve_details()[1:4]

        if slot in s.occupied:
            slot_name_plate, slot_vehicle_type = s.occupied[slot].spot_details()
            if slot_name_plate== name_plate and slot_vehicle_type == vehicle_type:
                print(f"Ticket has been verified removing slot {str(slot)} in floor {s.id}")
                s.remove_slot(slot)
                return True
        print("Wrong ticket details ")
        return False

    def print_details(s):
        print(f"Free slots: {s.free_slots}")
        print("Occupied slots: ")
        for i in s.occupied:
            print(i, end=" ")
        print("")


class ParkingLot:
    def __init__(s, name= "parkinglot1"):
        s.name= name
        s.Bike_floors = Floor(1)
        s.Car_floors = Floor(2)

    def print_details(s):
        print("Parking lot name: "+s.name)
        s.Bike_floors.print_details()
        s.Car_floors.print_details()
        print(s.Bike_floors, s.Car_floors)

    def retrieve_name(s):
        return s.name

    # def add(s, floor: Floor):
    #     s.floors.append(floor)
    
    # def remove(s, floor: Floor):
    #     try:
    #         s.floors.remove(floor)
    #     except:
    #         print(f"Floor {floor.id} not present in the parking lot")


class Parking:
    def __init__(s):
        s.parkinglot = defaultdict(lambda:None)

    def add_parkinglot(s, plot_name: int, parkinglot: ParkingLot):
        s.parkinglot[plot_name] = parkinglot


    def remove_parkinglot(s, plot_name: int):
        del s.parkinglot[plot_name]

    def check_lot(s, vehicle: Vehicle, vehicle_type, seq):
        for i in seq:
            if i in s.parkinglot:
                parkinglot = s.parkinglot[i]
                if vehicle_type == Vehicle_Type.Bike:
                    ticket = parkinglot.Bike_floors.check_free_slot(vehicle)
                    if ticket:
                        occupied_slot = ticket.retrieve_details()[3]
                        ticket.assign_parkinglot_details(parkinglot.retrieve_name(), parkinglot.Bike_floors)
                        print(f"Assigned parking_lot name {parkinglot.retrieve_name()} in Bike floor, parking no. {occupied_slot}")
                        return ticket
                    else: 
                        print("No free slot found for bikes")
                elif vehicle_type == Vehicle_Type.Car:
                    ticket = parkinglot.Car_floors.check_free_slot(vehicle)
                    if ticket:
                        occupied_slot = ticket.retrieve_details()[3]
                        ticket.assign_parkinglot_details(parkinglot.retrieve_name(), parkinglot.Car_floors)
                        print(f"Assigned parking_lot name {parkinglot.retrieve_name()} in Car floor, parking no. {occupied_slot}")
                        return ticket
                    else: 
                        print("No free slot found for cars")
                else:
                    print("Vehicle type error")
            else:
                print("Parking lot doesn't exist lot no: ", i)
        return None
                
    def release_lot(s, ticket: Ticket):
        floor = ticket.retrieve_details()[-2]
        if floor.verify_spot(ticket):
            return True
        else: return False
        




