# Import Libraries
import pygame
from pygame.locals import *
import random
import sys
import subprocess


# Coordinate size of the display
size = width, height = (800, 800)
road_w = int(width/1.6)
roadmark_w = int(width/80)
right_lane = width/2 + road_w/4
left_lane = width/2 - road_w/4
speed = 1


# Initialize the game
pygame.init()

# Initialize sound mixer
pygame.mixer.init()

# Load Background music
pygame.mixer.music.load("music/game_theme.mp3")
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1)

# Make a loop that keeps the game running
running = True

# Window Size
screen = pygame.display.set_mode(size)

# Set the title of the game window
pygame.display.set_caption("Sonic PyGame")

# Set background color
screen.fill((60, 220, 0))


# Load images

# Sonic sprite animation frames
sonic_running = [
    pygame.image.load("sprites/sonic/sonic007.png"),
    pygame.image.load("sprites/sonic/sonic008.png"),
    pygame.image.load("sprites/sonic/sonic009.png"),
    pygame.image.load("sprites/sonic/sonic010.png"),
    pygame.image.load("sprites/sonic/sonic011.png"),
    pygame.image.load("sprites/sonic/sonic012.png")
]

# Animation settings
player_frame_index = 0
player_frame_speed = 150
player_frame_update = pygame.time.get_ticks()

player = sonic_running[player_frame_index]
player_loc = player.get_rect()
player_loc.center = right_lane, height * 0.8


# Eggman sprite
enemy = pygame.image.load("sprites/eggman/eggman001.png")
enemy_loc = enemy.get_rect()
enemy_loc.center = left_lane, height * 0.2

counter = 0

# Make a loop that keeps the game running
while running:

    # Increasing the game speed
    counter += 1
    if counter == 5000:
        speed += 0.15
        counter = 0
        print("Level up", speed)
    # Animate enemy
    enemy_loc[1] += speed

    # Make enemy reappear
    if enemy_loc[1] > height:
        enemy_loc[1] = -200
        if random.randint(0, 1) == 0:
            enemy_loc.center = right_lane, -200
        else:
            enemy_loc.center = left_lane, -200

    # End the game when player and enemy collide each other
    if player_loc.colliderect(enemy_loc):
        pygame.quit()
        subprocess.run(["python3", "game_over.py"])  # Go to the Game over screen
        sys.exit()


    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        if event.type == KEYDOWN:
            if event.key in [K_a, K_LEFT]:
                player_loc = player_loc.move([-int(road_w/2), 0])
            if event.key in [K_d, K_RIGHT]:
                player_loc = player_loc.move([int(road_w/2), 0])
    
    current_animation = pygame.time.get_ticks()
    if current_animation - player_frame_update > player_frame_speed:
        player_frame_index = (player_frame_index + 1) % len(sonic_running)
        player = sonic_running[player_frame_index]
        player_frame_update = current_animation
    
    # Draw graphics
    pygame.draw.rect(
        screen,
        (50, 50, 50),
        (width/2 - road_w/2, 0, road_w, height)
    )

    pygame.draw.rect(
        screen,
        (255, 240, 60),
        (width/2 - roadmark_w/2, 0, roadmark_w, height)
    )

    pygame.draw.rect(
        screen,
        (255, 255, 255),
        (width/2 + road_w/2 - roadmark_w * 2, 0, roadmark_w, height)
    )

    pygame.draw.rect(
        screen,
        (255, 255, 255),
        (width/2 - road_w/2 + roadmark_w * 3, 0, roadmark_w, height)
    )

    screen.blit(player, player_loc)
    screen.blit(enemy, enemy_loc)
    pygame.display.update()


# Close the game
pygame.quit()
sys.exit()