
# Import classes from local folders.
from algos.random import RandomRabbit
from algos.linear import LinearRabbit

# Defaults for initializing the Rabbit instances.
default_holes = 10

# Initialize a Rabbit instance.
randomRabbit = RandomRabbit(default_holes) # RandomRabbit is a class extending Rabbit, which implements it's own seeking algo.
linearRabbit = LinearRabbit(default_holes)

# Prevent program from closing itself. Actually just waits for users input.
input()