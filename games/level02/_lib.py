from games._lib.grid_game import GridGame
from games._lib.grid_map import GridMap
from games._lib.objects import Lock


class SimpleKeysGame(GridGame):
    def __init__(self, grid):
        super().__init__(grid, 'Simple keys', False)
        self.message = "Hello. Try and open all the locks to get to the diamond.\n" \
                       "Walk up to the first lock. Use the right() function."

        lock = Lock(7)
        lock.message_in_front = "Open the door by calling the open_lock() function.\n" \
                                "You will need to pass a code. For this door it's number 7"
        self.locks.append(lock)

        lock = Lock(55, 99)
        lock.message_in_front = "You need 2 codes for this door: 55 and 99"
        self.locks.append(lock)

        lock = Lock("hello", 5, "cats and dogs")
        lock.message_in_front = "You need 3 codes for this door. The first one is the word hello.\n" \
                                "The second one is number 5. The third is a phrase: cats and dogs."
        self.locks.append(lock)

        self._redraw()


def create_game():
    global game
    map = GridMap('map.txt', 1, 2)
    game = SimpleKeysGame(map)


def right(steps=1):
    for x in range(steps):
        game.move(1, 0)


def open_lock(*args):
    game.open_lock(*args)


def run():
    game.run()
