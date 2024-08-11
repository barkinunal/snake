"""
Steps:
+ 1. Create a Board 
+ 2. Create a Grid
+ 3. Create a Snake
+ 4. Move the Snake
5. Create Food
6. Add the logic for eating the food
"""
# Example file showing a basic pygame "game loop"
import pygame
from constants import Constants
from snake import snake
from food import food


class Game:

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(
            (Constants.WINDOW_WIDTH, Constants.WINDOW_HEIGHT))
        self.clock = pygame.time.Clock()
        self.running = True

    def main(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT and snake.move != Constants.MOVE_RIGHT:
                        snake.move = Constants.MOVE_LEFT
                    if event.key == pygame.K_RIGHT and snake.move != Constants.MOVE_LEFT:
                        snake.move = Constants.MOVE_RIGHT
                    if event.key == pygame.K_UP and snake.move != Constants.MOVE_DOWN:
                        snake.move = Constants.MOVE_UP
                    if event.key == pygame.K_DOWN and snake.move != Constants.MOVE_UP:
                        snake.move = Constants.MOVE_DOWN

            # Move snake
            snake.move_snake()

            # Check if head is out of bounds
            if self.is_invalid_move():
                pygame.quit()

            # Check if the snake ate the food
            if self.did_snake_ate():
                snake.grow()
                food.new_position()

            # Draw Screen
            self.screen.fill(Constants.BLACK)
            self.draw_grid()
            self.draw_snake()
            self.draw_food()

            pygame.display.flip()

            self.clock.tick(5)

    def draw_grid(self):
        for row in range(0, Constants.WINDOW_WIDTH, Constants.BLOCK_SIZE):
            for column in range(0, Constants.WINDOW_HEIGHT, Constants.BLOCK_SIZE):
                rectangle = pygame.Rect(
                    row, column, Constants.BLOCK_SIZE, Constants.BLOCK_SIZE)
                pygame.draw.rect(self.screen, Constants.WHITE, rectangle, 1)

    def draw_snake(self):
        for snake_part in snake.snake:
            rectangle = pygame.Rect(
                snake_part[0] * Constants.BLOCK_SIZE, snake_part[1] * Constants.BLOCK_SIZE, Constants.BLOCK_SIZE, Constants.BLOCK_SIZE)
            pygame.Surface.fill(self.screen, Constants.GREEN, rectangle, 1)

    def draw_food(self):
        rectangle = pygame.Rect(food.position[0] * Constants.BLOCK_SIZE, food.position[1] *
                                Constants.BLOCK_SIZE, Constants.BLOCK_SIZE, Constants.BLOCK_SIZE)
        pygame.Surface.fill(self.screen, Constants.RED, rectangle, 1)

    def is_invalid_move(self):
        row_length = Constants.WINDOW_HEIGHT // Constants.BLOCK_SIZE
        snake_head = snake.head()
        column_length = Constants.WINDOW_WIDTH // Constants.BLOCK_SIZE

        for snake_part in range(1, len(snake.snake)):
            if snake.snake[snake_part] == snake.snake[0]:
                return True

        return snake_head[0] < 0 or snake_head[1] < 0 or snake_head[1] >= row_length or snake_head[0] >= column_length

    def did_snake_ate(self):
        return snake.head() == food.position


game = Game()

if __name__ == "__main__":
    game.main()
