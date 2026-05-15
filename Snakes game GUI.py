import tkinter as tk
import random

# -----------------------------
# Game settings
# -----------------------------
CELL_SIZE = 20
GRID_WIDTH = 30
GRID_HEIGHT = 20

WINDOW_WIDTH = CELL_SIZE * GRID_WIDTH
WINDOW_HEIGHT = CELL_SIZE * GRID_HEIGHT

SPEED = 120

SNAKE_COLOUR = "lime green"
FOOD_COLOUR = "red"
BACKGROUND_COLOUR = "black"
TEXT_COLOUR = "white"


class SnakeGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Snake Game")

        self.score = 0
        self.direction = "Right"
        self.next_direction = "Right"
        self.game_running = True

        self.canvas = tk.Canvas(
            root,
            width=WINDOW_WIDTH,
            height=WINDOW_HEIGHT,
            bg=BACKGROUND_COLOUR
        )
        self.canvas.pack()

        self.score_label = tk.Label(
            root,
            text="Score: 0",
            font=("Arial", 16)
        )
        self.score_label.pack()

        self.root.bind("<KeyPress>", self.change_direction)

        self.start_game()

    def start_game(self):
        self.score = 0
        self.direction = "Right"
        self.next_direction = "Right"
        self.game_running = True

        start_x = GRID_WIDTH // 2
        start_y = GRID_HEIGHT // 2

        self.snake = [
            (start_x, start_y),
            (start_x - 1, start_y),
            (start_x - 2, start_y)
        ]

        self.food = self.create_food()
        self.update_score()
        self.draw_game()
        self.game_loop()

    def create_food(self):
        while True:
            food_x = random.randint(0, GRID_WIDTH - 1)
            food_y = random.randint(0, GRID_HEIGHT - 1)
            food_position = (food_x, food_y)

            if food_position not in self.snake:
                return food_position

    def change_direction(self, event):
        key = event.keysym

        if key == "Up" and self.direction != "Down":
            self.next_direction = "Up"
        elif key == "Down" and self.direction != "Up":
            self.next_direction = "Down"
        elif key == "Left" and self.direction != "Right":
            self.next_direction = "Left"
        elif key == "Right" and self.direction != "Left":
            self.next_direction = "Right"
        elif key == "r" or key == "R":
            if not self.game_running:
                self.start_game()

    def move_snake(self):
        self.direction = self.next_direction

        head_x, head_y = self.snake[0]

        if self.direction == "Up":
            head_y -= 1
        elif self.direction == "Down":
            head_y += 1
        elif self.direction == "Left":
            head_x -= 1
        elif self.direction == "Right":
            head_x += 1

        new_head = (head_x, head_y)
        self.snake.insert(0, new_head)

        if new_head == self.food:
            self.score += 1
            self.food = self.create_food()
            self.update_score()
        else:
            self.snake.pop()

    def check_collision(self):
        head_x, head_y = self.snake[0]

        hit_left_wall = head_x < 0
        hit_right_wall = head_x >= GRID_WIDTH
        hit_top_wall = head_y < 0
        hit_bottom_wall = head_y >= GRID_HEIGHT

        if hit_left_wall or hit_right_wall or hit_top_wall or hit_bottom_wall:
            return True

        if self.snake[0] in self.snake[1:]:
            return True

        return False

    def draw_game(self):
        self.canvas.delete("all")

        # Draw food
        food_x, food_y = self.food
        self.draw_cell(food_x, food_y, FOOD_COLOUR)

        # Draw snake
        for x, y in self.snake:
            self.draw_cell(x, y, SNAKE_COLOUR)

    def draw_cell(self, grid_x, grid_y, colour):
        pixel_x = grid_x * CELL_SIZE
        pixel_y = grid_y * CELL_SIZE

        self.canvas.create_rectangle(
            pixel_x,
            pixel_y,
            pixel_x + CELL_SIZE,
            pixel_y + CELL_SIZE,
            fill=colour,
            outline=BACKGROUND_COLOUR
        )

    def update_score(self):
        self.score_label.config(text=f"Score: {self.score}")

    def game_loop(self):
        if self.game_running:
            self.move_snake()

            if self.check_collision():
                self.end_game()
            else:
                self.draw_game()
                self.root.after(SPEED, self.game_loop)

    def end_game(self):
        self.game_running = False

        self.canvas.create_text(
            WINDOW_WIDTH // 2,
            WINDOW_HEIGHT // 2 - 20,
            text="GAME OVER",
            fill=TEXT_COLOUR,
            font=("Arial", 28, "bold")
        )

        self.canvas.create_text(
            WINDOW_WIDTH // 2,
            WINDOW_HEIGHT // 2 + 20,
            text="Press R to restart",
            fill=TEXT_COLOUR,
            font=("Arial", 16)
        )


# -----------------------------
# Run the game
# -----------------------------
root = tk.Tk()
game = SnakeGame(root)
root.mainloop()
