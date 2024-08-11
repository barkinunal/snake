import random
from constants import Constants
from snake import snake


class Food:
    def __init__(self):
        self.position = None
        self.new_position()

    def new_position(self):
        possible_positions = [(x, y)
                              for x in range(0, Constants.WINDOW_WIDTH // Constants.BLOCK_SIZE)
                              for y in range(0, Constants.WINDOW_HEIGHT // Constants.BLOCK_SIZE)
                              if (x, y) not in snake.snake]

        self.position = possible_positions[random.randint(
            0, len(possible_positions))]


food = Food()
