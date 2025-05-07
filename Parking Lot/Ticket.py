
class Ticket:
    ticket_seq = 0
    def __init__(s, name_plate, vehicle_type, slot):
        s.ticket_number = Ticket.ticket_seq
        Ticket.ticket_seq += 1
        s.name_plate = name_plate
        s.vehicle_type = vehicle_type
        s.parking_no = slot
        s.time =0
        s.floor = None
        s.parkinglot_name =""

    def assign_parkinglot_details(s, parkinglot_name, floor):
        s.parkinglot_name = parkinglot_name
        s.floor = floor

    def retrieve_details(s):
        return [s.ticket_number, s.name_plate, s.vehicle_type, s.parking_no, s.time, s.floor, s.parkinglot_name]

    def assign_time(s, time):
        s.time = time

    def print_details(s):
        print("\n\nTicket Details:")
        print("Ticket number: "+str(s.ticket_number))
        print("Name plate: "+ s.name_plate)
        print("Vehicle type: ", s.vehicle_type)
        print("Parking no: ",s.parking_no)
        print("Parkinglot name: "+s.parkinglot_name)
        print("Floor no: ", s.floor)
        print("Incoming time: ", s.time)
        print("")

