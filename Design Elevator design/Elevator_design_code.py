import threading
import time
import random
from enum import Enum


class Direction(Enum):
    UP = "UP"
    DOWN = "DOWN"
    IDLE = "IDLE"

class ElevatorState(Enum):
    MOVING = "MOVING"
    STOPPED = "STOPPED"
    IDLE = "IDLE"

class Request:
    def __init__(self, floor: int, direction: Direction = None):
        self.floor = floor
        self.direction = direction  # only used by external request

class Door:
    def __init__(self):
        self.open = False

    def open_door(self):
        self.open = True
        print("🚪 Door opened")

    def close_door(self):
        self.open = False
        print("🚪 Door closed")


class ElevatorButton:
    def __init__(self, floor: int, elevator):
        self.floor = floor
        self.elevator = elevator

    def press(self):
        print(f"🔘 Floor {self.floor} button pressed inside Elevator {self.elevator.id}")
        self.elevator.add_target(self.floor)


class Elevator(threading.Thread):
    def __init__(self, id, current_floor=0):
        super().__init__()
        self.id = id
        self.current_floor = current_floor
        self.state = ElevatorState.IDLE
        self.direction = Direction.IDLE
        self.door = Door()
        self.lock = threading.Lock()
        self.target_floors = []
        self.running = True

    def add_target(self, floor):
        with self.lock:
            if floor not in self.target_floors:
                self.target_floors.append(floor)
                self.target_floors.sort(reverse=self.direction == Direction.DOWN)

    def run(self):
        while self.running:
            with self.lock:
                if self.target_floors:
                    target = self.target_floors.pop(0)
                    self.state = ElevatorState.MOVING
                    print(f"🚀 Elevator {self.id} moving from floor {self.current_floor} to {target}")
                    while self.current_floor != target:
                        if self.current_floor < target:
                            self.direction = Direction.UP
                            self.current_floor += 1
                        else:
                            self.direction = Direction.DOWN
                            self.current_floor -= 1
                        print(f"Elevator {self.id} at floor {self.current_floor}")
                        time.sleep(0.2)

                    self.state = ElevatorState.STOPPED
                    print(f"✅ Elevator {self.id} arrived at floor {target}")
                    self.door.open_door()
                    time.sleep(0.5)
                    self.door.close_door()
                    self.state = ElevatorState.IDLE
                    self.direction = Direction.IDLE
                else:
                    self.state = ElevatorState.IDLE
            time.sleep(0.1)  # prevent busy waiting

    def stop(self):
        self.running = False


class FloorButton:
    def __init__(self, floor, direction: Direction):
        self.floor = floor
        self.direction = direction

    def press(self, elevator_system):
        print(f"📞 Button pressed on floor {self.floor} to go {self.direction.name}")
        request = Request(self.floor, self.direction)
        elevator_system.handle_request(request)


class ElevatorSystem:
    def __init__(self, num_elevators):
        self.elevators = [Elevator(id=i) for i in range(num_elevators)]
        for e in self.elevators:
            e.start()

    def handle_request(self, request: Request):
        best_elevator = self.select_best_elevator(request)
        print(f"🔧 Assigned Elevator {best_elevator.id} to floor {request.floor}")
        best_elevator.add_target(request.floor)

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
