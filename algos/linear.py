from rabbit import Rabbit

class LinearRabbit(Rabbit):
    """A linear algorithm searching for the hole, in which the rabbit dwells."""

    seekerPosition = 0 # current position of the seeker (not the rabbit!)
    seekerDirection = 1 # 0 - left / 1 - right

    def __init__(self, holes: int):
        super().__init__("Linear Rabbit", holes)

    def lifecycle(self):
        pos = self.seekerPosition
        dir = self.seekerDirection

        if (dir == 1):
            # Increment seeker position (linear algo)
            pos += 1

            # Create a barrier if the seeker hits the edge (on the left side)
            if(pos >= self.holes):
                pos = self.holes
                dir = 0
        else:
            # Decrement seeker position (linear algo)
            pos -= 1

            # Create a barrier if the seeker hits the edge (on the right side)
            if(pos < 0):
                pos = 0
                dir = 1
        
        # Update the seeker position & direction
        self.seekerPosition = pos
        self.seekerDirection = dir

        # Check for result
        result = self.checkHole(self.seekerPosition)

        if(result == True):
            # Reset the seeker position & direction
            self.seekerPosition = 0
            self.seekerDirection = 1