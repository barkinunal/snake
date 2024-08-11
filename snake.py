from constants import Constants
from collections import deque
"""
    
    
    . . . .

    .
    . . .
"""


class Snake:
    def __init__(self):
        self.snake = deque()
        self.snake.appendleft(Constants.INITIAL_SNAKE_POSITION)
        self.move = Constants.MOVE_LEFT
        self.previous_head_position = None

    def head(self):
        return self.snake[0]

    def move_snake(self):
        # Move head
        self._move_head()

        # Move rest of the body
        self._move_body()

    def grow(self):
        self.snake.append(self.previous_head_position)

    def _move_head(self):
        head = self.snake.popleft()
        self.snake.appendleft(head)
        new_head = (head[0] + self.move[0], head[1] + self.move[1])
        self.snake.insert(0, new_head)
        self.previous_head_position = head

    def _move_body(self):
        if len(self.snake) > 1:
            self.snake.pop()


snake = Snake()
