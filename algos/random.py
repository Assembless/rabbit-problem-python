from rabbit import Rabbit

class RandomRabbit(Rabbit):
    """A random algorithm searching for the hole, in which the rabbit dwells."""

    def __init__(self, holes: int):
        super().__init__("Random Rabbit", holes)

    def lifecycle(self):
        # Import randomint method from random module
        from random import randint

        # Generate a random number between 0 and 1 to decide in which direction the rabbit should go.
        nextHole = randint(0, self.holes - 1)

        # Check for result
        self.checkHole(nextHole)