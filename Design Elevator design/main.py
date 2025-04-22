from Elevator_design_code import *

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