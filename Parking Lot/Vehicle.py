from Parking import *
from datetime import datetime
from abc import ABC,abstractmethod
from type import *


class Vehicle(ABC):
    def __init__(s, name_plate, vehicle_type):
        s.name_plate = name_plate
        s.vehicle_type = vehicle_type
        s.ticket_number = None
        s.time = None
        s.floor = None
        s.parking_lot = None
        s.parking_number = None


    def assign_details(s, floor, parking_no: int, ticket_number: int):
        s.floor = floor
        s.parking_number = parking_no
        s.ticket_number = ticket_number
        now = datetime.now()
        s.time = now.strftime("%H%M%S")
        return s.time

    def retrieve_parking_details(s):
        return [s.parking_lot, s.floor, s.parking_number]
    
    def retrieve_vehicle_details(s):
        return [s.name_plate, s.vehicle_type, s.time]
    
    @abstractmethod
    def calculate_cost(s):
        pass


class Bike(Vehicle):
    def __init__(s, name_plate, cost = 20):
        super().__init__(name_plate, Vehicle_Type.Bike)
        s.cost = cost

    def calculate_cost(s):
        now = datetime.now()
        time = now.strftime("%H%M%S")
        return [(int(time) - int(s.time))*s.cost, int(time) - int(s.time)]


class Car(Vehicle):
    def __init__(s, name_plate, cost = 40):
        super().__init__(name_plate, Vehicle_Type.Car)
        s.cost = cost

    def calculate_cost(s):
        now = datetime.now()
        time = now.strftime("%H%M%S")
        return [(int(time) - int(s.time))*s.cost, int(time) - int(s.time)]

    


