import pygame
import time
from pygame.locals import *
import random

# Function to display the score
def score(score):
    num = score_font.render("Score: " + str(score), True, red)
    window.blit(num, [0, 0])

# Function to draw the snake
def game_snake(snake, snake_length_list):
    for x in snake_length_list:
        pygame.draw.rect(window, blue, [x[0], x[1], snake, snake])

# Function to display a message
def message(msg):
    msg = font_style.render(msg, True, red)
    window.blit(msg, [win_width / 3, win_height / 3])

# Main game loop
def loop():
    gameOver = False
    gameClose = False
    x1 = win_width / 2
    y1 = win_height / 2
    x1_change = 0
    y1_change = 0
    snake_length_list = []
    snake_length = 1
    # Generate initial food position
    foodx = round(random.randrange(0, win_width - snake) / 10.0) * 10.0
    foody = round(random.randrange(0, win_height - snake) / 10.0) * 10.0

    while not gameOver:
        while gameClose:
            window.fill(black)
            message("You Lost!! Press P to Play Again or Q to Quit")
            score(snake_length - 1)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameOver = True  # Exit the main loop and quit
                        gameClose = False
                    if event.key == pygame.K_p:
                        loop()  # Restart the game

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameOver = True
            if event.type == pygame.KEYDOWN:
                if event.key == K_LEFT:
                    x1_change = -snake
                    y1_change = 0
                if event.key == K_RIGHT:
                    x1_change = snake
                    y1_change = 0
                if event.key == K_UP:
                    x1_change = 0
                    y1_change = -snake
                if event.key == K_DOWN:
                    x1_change = 0
                    y1_change = snake

        # Check for collision with boundaries
        if x1 >= win_width or x1 < 0 or y1 >= win_height or y1 < 0:
            gameClose = True
        x1 += x1_change
        y1 += y1_change
        window.fill(black)
        pygame.draw.rect(window, yellow, [foodx, foody, snake, snake])
        snake_size = []
        snake_size.append(x1)
        snake_size.append(y1)
        snake_length_list.append(snake_size)
        if len(snake_length_list) > snake_length:
            del snake_length_list[0]

        # Check for collision with itself
        for block in snake_length_list[:-1]:
            if block == snake_size:
                gameClose = True

        game_snake(snake, snake_length_list)
        score(snake_length - 1)
        pygame.display.update()

        # Check if snake has eaten the food
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, win_width - snake) / 10.0) * 10.0
            foody = round(random.randrange(0, win_height - snake) / 10.0) * 10.0
            snake_length += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()

# Initialize pygame
pygame.init()
red = (200, 0, 54)
blue = (0, 141, 218)
black = (2, 21, 38)
yellow = (255, 201, 111)

# Set window dimensions
win_width = 900
win_height = 600
window = pygame.display.set_mode((win_width, win_height))
pygame.display.set_caption("Snake Game")
time.sleep(5)

snake = 10
snake_speed = 15
clock = pygame.time.Clock()
font_style = pygame.font.SysFont("lucidsans", 26)
score_font = pygame.font.SysFont("lucidaconsole", 30)

# Start the game
loop()
