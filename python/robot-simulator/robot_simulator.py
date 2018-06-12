# Globals for the bearings
# Change the values as you see fit
EAST = 0
NORTH = 1
WEST = 2
SOUTH = 3


class Robot:
    def __init__(self, bearing=NORTH, x=0, y=0):
        self.bearing = bearing
        self.coordinates = (x, y)
        
    def turn_right(self):
        self.bearing = (self.bearing - 1) % 4
        
    def turn_left(self):
        self.bearing = (self.bearing + 1) % 4
        
    def advance(self):
        x, y = self.coordinates
        if self.bearing == NORTH:
            self.coordinates = (x, y+1)
        elif self.bearing == SOUTH:
            self.coordinates = (x, y-1)
        elif self.bearing == EAST:
            self.coordinates = (x+1, y)
        elif self.bearing == WEST:
            self.coordinates = (x-1, y)
            
    def simulate(self, path):
        for i in path:
            if i == 'A':
                self.advance()
            if i == 'L':
                self.turn_left()
            if i == 'R':
                self.turn_right()
