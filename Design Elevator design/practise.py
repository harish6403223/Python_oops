from enum import Enum
import time
import threading
import sys
import random

class Direction(Enum):
    UP = "UP"
    DOWN = "DOWN"
    IDLE = "IDLE"

class ElevatorState(Enum):
    MOVING = "MOVING"
    STOPPED ="STOPPED"
    IDLE = "IDLE"

class Request:
    def __init__(self, floor, direction):
        self.floor = floor
        self.direction =direction

class Door:
    def __init__(self):
        self.open = False

    def open_door(self):
        self.open = True
        print("Door opened")
    
    def close_door(self):
        self.open = False
        print("Door closed")

class ElevatorButton:
    def __init__(self, floorbutton, elevator):
        self.floor = floorbutton
        self.elevator = elevator

    def press(self):
        print(f"🔘 Floor {self.floor} button pressed inside Elevator {self.elevator.id}")
        self.elevator.add_target(self.floor)

class FloorButton:
    def __init__(self, floor, direction):
        self.floor = floor
        self.direction = direction

    def press(self, ElevatorSystem):
        req = Request(self.floor, self.direction)
        ElevatorSystem.handle_request(req)

class Elevator(threading.Thread):
    def __init__(s, id, current_floor =0):
        super().__init__()
        s.id = id
        s.current_floor = current_floor
        s.target_floors = set()
        s.state = ElevatorState.IDLE
        s.direction = Direction.IDLE
        s.door = Door()
        s.lock = threading.Lock()
        s.running = True
        s.max = 10

    def add_target(s, floor):
        with s.lock:
            s.target_floors.add(floor)

    def run(s):
        while s.running:
            with s.lock:
                if s.target_floors:
                    target= s.retrieve_floor()
                    s.state = ElevatorState.MOVING
                    while s.current_floor is not target:
                        if s.direction == Direction.UP:
                            s.current_floor+=1
                        else:
                            s.current_floor-=1
                        print(f"Elevator {s.id} at floor {s.current_floor}")
                        time.sleep(0.2)
                    s.state = ElevatorState.STOPPED
                    print(f"✅ Elevator {s.id} arrived at floor {target}")
                    s.door.open_door()
                    time.sleep(0.5)
                    s.door.close_door()
                    s.state = ElevatorState.IDLE
                    s.direction = Direction.IDLE
                    
                else: 
                    s.state = ElevatorState.IDLE
            time.sleep(0.1)  # prevent busy waiting

    def retrieve_floor(s):
        dwn, up = -sys.maxsize, sys.maxsize
        ans =sys.maxsize
        if(s.direction == Direction.IDLE):
            for i in range(s.current_floor, 9):
                if i in s.target_floors:
                    up =i
                    break
            if(abs(s.current_floor-up)< ans):
                s.direction = Direction.UP
                ans=up
            for i in range(s.current_floor, -1, -1):
                if i in s.target_floors:
                    dwn =i
                    break
            if(abs(s.current_floor-dwn)< ans):
                s.direction = Direction.DOWN
                ans=dwn
            s.target_floors.remove(ans)
            return ans
        elif(s.direction == Direction.UP):
            for i in range(s.current_floor, 9):
                if i in s.target_floors:
                    up =i
                    break
            if(up == sys.maxsize):
                s.direction = Direction.DOWN
                return s.retrieve_floor()
            else:
                s.target_floors.remove(up)
                return up
        else:
            for i in range(s.current_floor, -1, -1):
                if i in s.target_floors:
                    dwn =i
                    break
            if(dwn == -sys.maxsize):
                s.direction = Direction.UP
                return s.retrieve_floor()
            else:
                s.target_floors.remove(dwn)
                return dwn
            
    def stop(s):
        s.running = False

class ElevatorSystem:
    def __init__(self, num_elevators):
        self.elevators = [Elevator(id=i) for i in range(num_elevators)]
        for e in self.elevators:
            e.start()

    def handle_request(s, request: Request):
        elevator = s.select_best_elevator(request)
        print(f"🔧 Assigned Elevator {elevator.id} to floor {request.floor}")
        elevator.add_target(request.floor)

    def select_best_elevator(self, request: Request):
        idle_elevators = [e for e in self.elevators if e.state == ElevatorState.IDLE]
        if idle_elevators:
            return random.choice(idle_elevators)

        return min(self.elevators, key=lambda e: abs(e.current_floor - request.floor))

    def press_inside_button(self, elevator_id, floor):
        button = ElevatorButton(floor, self.elevators[elevator_id])
        button.press()

    def shutdown(self):
        for e in self.elevators:
            e.stop()
        for e in self.elevators:
            e.join()

if __name__ == "__main__":
    system = ElevatorSystem(2)

    try:
        # External request
        FloorButton(4, Direction.UP).press(system)
        FloorButton(2, Direction.DOWN).press(system)

        time.sleep(1)

        # Internal buttons inside elevator 0
        system.press_inside_button(0, 7)
        system.press_inside_button(0, 1)

        # Internal buttons inside elevator 1
        system.press_inside_button(1, 6)

        # Let them run a bit
        time.sleep(10)
    finally:
        system.shutdown()













 



