# Direction Constants
NORTH, EAST, SOUTH, WEST = range(4)


class Robot(object):
    def __init__(self, bearing=NORTH, x_coordinate=0, y_coordinate=0):
        self.bearing = bearing  # Current direction robot is facing
        self.x_coordinate = x_coordinate  # Current x position
        self.y_coordinate = y_coordinate  # Current y position
        self.coordinates = (self.x_coordinate, self.y_coordinate)  # List of the x-y coordinates

    def advance(self):
        # Advance robot 1 space along its current facing
        if self.bearing == NORTH:
            self.y_coordinate += 1
        elif self.bearing == EAST:
            self.x_coordinate += 1
        elif self.bearing == SOUTH:
            self.y_coordinate -= 1
        elif self.bearing == WEST:
            self.x_coordinate -= 1

        # Update the new coordinates
        self.coordinates = (self.x_coordinate, self.y_coordinate)

    def simulate(self, program):
        # Takes a string that is the current program and executes each character
        for instruction in program:
            if instruction == 'A':
                self.advance()
            elif instruction == 'R':
                self.turn_right()
            elif instruction == 'L':
                self.turn_left()

    def turn_left(self):
        # To get the new bearing after turning left the old bearing value
        # is subtracted by one.  Using modulo handles turning from North to West
        self.bearing = (self.bearing - 1) % 4

    def turn_right(self):
        # To get the new bearing after turning right the one is added to the
        # old bearing value.  Using modulo handles turning from West to North
        self.bearing = (self.bearing + 1) % 4
