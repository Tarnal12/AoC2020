class PartOneShip():
    def __init__(self):
        self.facing = 90
        self.x_displacement = 0
        self.y_displacement = 0
    
    def move(self, move_cmd):
        instruction = move_cmd[0]
        value = int(move_cmd[1:])
        instruction_to_execute = {
            "F": self.move_forward,
            "N": self.move_north,
            "S": self.move_south,
            "E": self.move_east,
            "W": self.move_west,
            "L": self.turn_left,
            "R": self.turn_right
        }
        return instruction_to_execute[instruction](value)

    def move_forward(self, value: int):
        if self.facing == 90:
            self.move_east(value)
        if self.facing == 180:
            self.move_south(value)
        if self.facing == 270:
            self.move_west(value)
        if self.facing == 0:
            self.move_north(value)

    def move_north(self, value: int):
        self.y_displacement += value

    def move_south(self, value: int):
        self.y_displacement -= value

    def move_east(self, value: int):
        self.x_displacement += value

    def move_west(self, value: int):
        self.x_displacement -= value

    def turn_left(self, value: int):
        self.facing -= value
        self.facing %= 360

    def turn_right(self, value: int):
        self.facing += value
        self.facing %= 360

    def manhattan_displacement(self) -> int:
        return abs(self.x_displacement) + abs(self.y_displacement)

class PartTwoShip():
    def __init__(self):
        self.waypoint_x = 10
        self.waypoint_y = 1
        self.x_displacement = 0
        self.y_displacement = 0
    
    def move(self, move_cmd):
        instruction = move_cmd[0]
        value = int(move_cmd[1:])
        instruction_to_execute = {
            "F": self.move_forward,
            "N": self.move_north,
            "S": self.move_south,
            "E": self.move_east,
            "W": self.move_west,
            "L": self.turn_left,
            "R": self.turn_right
        }
        return instruction_to_execute[instruction](value)

    def move_forward(self, value: int):
        self.x_displacement += self.waypoint_x * value
        self.y_displacement += self.waypoint_y * value

    def move_north(self, value: int):
        self.waypoint_y += value

    def move_south(self, value: int):
        self.move_north(0 - value)

    def move_east(self, value: int):
        self.waypoint_x += value

    def move_west(self, value: int):
        self.move_east(0 - value)

    def turn_right(self, value: int):
        value %= 360
        ninety_deg_turns = int(value / 90)
        for i in range(ninety_deg_turns):
            starting_coords = (self.waypoint_x, self.waypoint_y)
            self.waypoint_x = starting_coords[1]
            self.waypoint_y = 0 - starting_coords[0]

    def turn_left(self, value: int):
        value %= 360
        self.turn_right(360 - value)

    def manhattan_displacement(self) -> int:
        return abs(self.x_displacement) + abs(self.y_displacement)

def main():
    with open("Day12Input.txt", "r") as f:
        inputs = f.readlines()

    ship = PartOneShip()
    for move_cmd in inputs:
        ship.move(move_cmd)
    print(ship.manhattan_displacement())

    ship = PartTwoShip()
    for move_cmd in inputs:
        ship.move(move_cmd)
    print(ship.manhattan_displacement())


if __name__ == "__main__":
    main()