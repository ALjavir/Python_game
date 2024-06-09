# import tkinter as tk
# import random

# # Function to update the target's position
# def move_target():
#     x = random.randint(10, 390)
#     y = random.randint(10, 380)
    
#     # Move the target to the new coordinates
#     canvas.coords(target, x-10, y-10, x+10, y+10)
    
#     # Schedule the next movement
#     window.after(1000, move_target)

# # Function to handle target clicks
# def target_clicked(event):
#     global score
    
#     # Check if the click event occurred within the target
#     if canvas.find_withtag(tk.CURRENT):
#         score += 1
#         score_label.config(text="Score: " + str(score))

# # Create the main window
# window = tk.Tk()
# window.title("Target Game")

# # Create a canvas to draw the target
# canvas = tk.Canvas(window, width=400, height=400)
# canvas.pack()

# # Create the target (initially hidden)
# target = canvas.create_oval(-10, -10, -10, -10, fill="red")

# # Bind the target click event to the target_clicked function
# canvas.tag_bind(target, "<Button-1>", target_clicked)import pygame


import pygame
import random
import math

# Initialize Pygame
pygame.init()

# Set up the game window
screen_width = 1500
screen_height = 1000
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Space Shooting Game")

# Set up the colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

# Set up the player spaceship
player_img = pygame.image.load("spaceship.png")
player_width = 250
player_height = 248
player_x = screen_width / 2 - player_width / 2
player_y = screen_height - player_height - 10
player_speed = 5

# Set up the bullet
bullet_img = pygame.image.load("bullet.png")
bullet_width = 50
bullet_height = 50
bullet_x = 0
bullet_y = player_y
bullet_speed = 10
bullet_state = "ready"  # "ready" - ready to fire, "fired" - bullet is moving

# Set up the enemy spaceships
enemy_img = pygame.image.load("enemy.png")
enemy_width = 150
enemy_height = 179
enemy_x = random.randint(0, screen_width - enemy_width)
enemy_y = random.randint(50, 150)
enemy_speed = 2

# Function to draw the player spaceship
def draw_player(x, y):
    screen.blit(player_img, (x, y))

# Function to draw the bullet
def draw_bullet(x, y):
    screen.blit(bullet_img, (x, y))

# Function to draw the enemy spaceship
def draw_enemy(x, y):
    screen.blit(enemy_img, (x, y))

# Function to check if bullet hit the enemy
def is_collision(enemy_x, enemy_y, bullet_x, bullet_y):
    distance = math.sqrt((enemy_x - bullet_x)**2 + (enemy_y - bullet_y)**2)
    if distance < 27:
        return True
    else:
        return False

# Game loop
running = True
while running:
    screen.fill((0, 0, 0))  # Fill the screen with black color
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        # Check for keystrokes to move the player spaceship
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_speed = -5
            if event.key == pygame.K_RIGHT:
                player_speed = 5
            if event.key == pygame.K_SPACE:
                if bullet_state == "ready":
                    bullet_x = player_x + player_width / 2 - bullet_width / 2
                    bullet_y = player_y
                    bullet_state = "fired"
                    bullet_sound = pygame.mixer.Sound("laser.wav")
                    bullet_sound.play()
        
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player_speed = 0

    # Move the player spaceship
    player_x += player_speed
    
    # Restrict the player spaceship within the screen boundaries
    if player_x < 0:
        player_x = 0
    elif player_x > screen_width - player_width:
        player_x = screen_width - player_width
    
    # Move the bullet
    if bullet_state == "fired":
        bullet_y -= bullet_speed
    
    # Check if the bullet is out of the screen
    if bullet_y <= 0:
        bullet_y = player_y
        bullet_state = "ready"
    
    # Draw the player spaceship, bullet, and enemy spaceship
    draw_player(player_x, player_y)
    if bullet_state == "fired":
        draw_bullet(bullet_x, bullet_y)
    draw_enemy(enemy_x, enemy_y)
    
    # Check for collision between bullet and enemy
    collision = is_collision(enemy_x, enemy_y, bullet_x, bullet_y)
    if collision:
        bullet_y = player_y
        bullet_state = "ready"
        enemy_x = random.randint(0, screen_width - enemy_width)
        enemy_y = random.randint(50, 150)
    
    # Move the enemy spaceship
    enemy_x += enemy_speed
    
    # Reverse the enemy spaceship's direction if it reaches the screen boundaries
    if enemy_x <= 0 or enemy_x >= screen_width - enemy_width:
        enemy_speed *= -1
    
    pygame.display.update()  # Update the screen

# Quit the game
pygame.quit()




