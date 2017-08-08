NORTH = 0
EAST = 1
SOUTH = 2
WEST = 3

NEW_DIRECTION = {0: NORTH,
                 1: EAST,
                 2: SOUTH,
                 3: WEST
                 }


class Robot(object):
    def __init__(self, bearing=NORTH, x_coordinate=0, y_coordinate=0):
        self.bearing = bearing
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate
        self.coordinates = (self.x_coordinate, self.y_coordinate)

    def advance(self):
        if self.bearing == NORTH:
            self.y_coordinate += 1
        elif self.bearing == EAST:
            self.x_coordinate += 1
        elif self.bearing == SOUTH:
            self.y_coordinate -= 1
        elif self.bearing == WEST:
            self.x_coordinate -= 1

        self.coordinates = (self.x_coordinate, self.y_coordinate)

    def simulate(self, program):
        for instruction in program:
            if instruction == 'A':
                self.advance()
            elif instruction == 'R':
                self.turn_right()
            elif instruction == 'L':
                self.turn_left()

    def turn_left(self):
        new_bearing = self.bearing - 1
        if new_bearing < 0:
            self.bearing = NEW_DIRECTION[3]
        else:
            self.bearing = NEW_DIRECTION[new_bearing]

    def turn_right(self):
        new_bearing = self.bearing + 1
        if new_bearing > 3:
            self.bearing = NEW_DIRECTION[0]
        else:
            self.bearing = NEW_DIRECTION[new_bearing]