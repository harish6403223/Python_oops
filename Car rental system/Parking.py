from collections import defaultdict
from type import *

class Floor:
    def __init__(s, id, slots = None):
        s.id =id 
        s.free_slots = slots
        if not slots:
            s.free_slots = set()
            for i in range(1, 11):
                s.free_slots.add(i)
        s.occupied =set()

    def add_slot(s, slot):
        s.free_slots.remove(slot)
        s.occupied.add(slot)
        print(f"Free slots: {s.free_slots}")
        print(f"Occupied slots: {s.occupied}")
    
    def remove_slot(self, slot:int):
        self.free_slots.add(slot)
        self.occupied.remove(slot)
        print(f"Free slots: {self.free_slots}")
        print(f"Occupied slots: {self.occupied}")

    def check_free_slot(s):
        for slot in s.free_slots:
            s.add_slot(slot)
            return slot
        return None
        
        
class ParkingLot:
    def __init__(s, name= "parkinglot1", Bike_Floor = Floor(1), Car_Floor = Floor(2)):
        s.name= name
        s.Bike_floors = Bike_Floor
        s.Car_floors = Car_Floor

    # def add(s, floor: Floor):
    #     s.floors.append(floor)
    
    # def remove(s, floor: Floor):
    #     try:
    #         s.floors.remove(floor)
    #     except:
    #         print(f"Floor {floor.id} not present in the parking lot")


class Parking:
    def __init__(s):
        s.parkinglot = defaultdict(None)

    def add_parkinglot(s, plot_name: int, parkinglot: ParkingLot):
        s.parkinglot[plot_name] = parkinglot


    def remove_parkinglot(s, plot_name: int):
        del s.parkinglot[plot_name]

    def check_lot(s, vehicle_type, seq):
        for i in seq:
            parkinglot = s.parkinglot[i]
            if vehicle_type == Vehicle_Type.Bike:
                free_slot = parkinglot.Bike_floors.check_free_slot()
                if free_slot:
                    print(f"Assigned parking_lot {parkinglot.name} in Bike floor, parking no. {free_slot}")
                    return [parkinglot.Bike_floors, free_slot]
                else: 
                    print("No free slot found for bikes")
            elif vehicle_type == Vehicle_Type.Car:
                free_slot = parkinglot.Car_floors.check_free_slot()
                if free_slot:
                    print(f"Assigned parking_lot {parkinglot.name} in Car floor, parking no. {free_slot}")
                    return [parkinglot.Car_floors, free_slot]
                else: 
                    print("No free slot found for cars")
            else:
                print("Vehicle type error")
            return [None,  None]
                
    def release_lot(s, floor, slot:int):
        floor.remove_slot(slot)




