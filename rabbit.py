from utils import set_interval


class Rabbit():
    """A Rabbit class"""
    name = "Unnamed Rabbit"
    holes = 10
    position = 0
    success = 0
    cycles = 0

    def __init__(self, name: str, holes: int):
        """Initialize a Rabbit object"""
        # Initialize the holes
        self.holes = holes | 10
        # Initialize rabbit instance name
        self.name = name

        def interval_callback():
            self.__move()
            self.lifecycle()

        set_interval(interval_callback, 1.5)

    def __move(self):
        """Move rabbit to a nearby hole."""
        # Import random module.
        from random import randint
        # Generate a random number between 0 and 1 to decide in which direction the rabbit should go.
        nextHole = randint(0, 1) == 0 and self.position - 1 or self.position + 1

        # If the rabbit is at the edge of the board, it should hit the barrier.
        if nextHole < 0:
            nextHole = 0
        elif nextHole >= self.holes: 
            nextHole = nextHole

        # Move the rabbit to the next hole.
        self.position = nextHole

    def __resetPosition(self):
        """Reset the rabbit position"""
        # Import random module.
        from random import randint
        self.position = randint(0, self.holes - 1)

    def lifecycle(self):
        """A lifecycle function running in each iteration. Write your algorithm code here."""

    def checkHole(self, hole: int) -> bool:
        """Check if the rabbit is at the hole"""
        # Set the result
        result = self.position == hole

        # Increment the cycles counter
        self.cycles += 1

        # Print the result + the header
        if (result):
            # Increment the success counter
            self.success += 1
            # TODO: Format strings to be more readable.
            print("=== {} ===\n🎉🎉 Rabbit was caught at hole {}! 🎉🎉\n✅ Success => {}\n🔁 Cycles => {}\n\n".format(self.name, self.position, self.success, self.cycles))
            self.__resetPosition();
        else:
            print("=== {} ===\nNo luck at hole {}. Rabbit is at hole {}.\n✅ Success => {}\n🔁 Cycles => {}\n\n".format(self.name, hole, self.position, self.success, self.cycles))
        return result