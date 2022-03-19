# rabbit-problem-python
 🐇 The rabbit problem implemented in Python language.

## Run rabbit

To run the rabbit program, execute the command below in the root directory of the project.
`python main.go`


more coming soon...

## Implementing own custom algorithm

In order to create your own algorithm, attempting to find the rabbit problem, the following steps are necessary:

1. Create a new file in `algos/__name__.py`.
2. Extend the Rabbit class:
```python
from rabbit import Rabbit

class UnnamedRabbit(Rabbit):
    """..."""

    def __init__(self, holes: int):
        super().__init__("Unnamed Rabbit", holes)

    # The main function being run on every cycle/rabbit move.
    def lifecycle(self):
        # Check whether the rabbit is in the given hole.
        self.checkHole(0)
```
3. Import and initialize an instance of your new algorithm in `main.py` located in the root directory.
```python
from algos.__name__ import UnnamedRabbit

...

unnamedRabbit = UnnamedRabbit(default_holes)
```
4. Have fun writing your algorithm!

## Directory tree

```
rabbit-problem-python
│   main.py     - The entry file, run it to see the result.
│   rabbit.py   - The rabbit class powering the various custom algorighms.
│   setup.py    - The setup file, run it to install the package. *NOT WORKING YET!*
│   utils.py    - The utils file, contains various functions used by the other files.
│
├───algos
│       linear.py - The linear algorithm attempting to find rabbit.
│       random.py - The random algorithm attempting to find rabbit.
```