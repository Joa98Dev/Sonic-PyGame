# Import Libraries
import pygame
from pygame.locals import *
import sys
import subprocess

# Initialize PyGame
pygame.init()

# Initialize sound mixer
pygame.mixer.init()

# Load Background music
pygame.mixer.music.load("music/main_menu.mp3")
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1)

# Screen Setup
WIDTH, HEIGHT = 800, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Main Menu")


# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
font = pygame.font.Font(None, 50)

# Set a Background image
bg = pygame.image.load("images/sonic_pygame_title.jpg")

# Menu options
start_text = font.render("PRESS ENTER to Start", True, WHITE)
quit_text = font.render("PRESS ESC to Close the game", True, WHITE)

# Main Menu Loop
running = True
while running:
    screen.blit(bg, (0,0))
    screen.blit(start_text, (WIDTH//2 - start_text.get_width()//2, 350))
    screen.blit(quit_text, (WIDTH//2 - quit_text.get_width()//2, 450))

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:  # Start game on ENTER key
                pygame.quit()
                subprocess.run(["python3", "game.py"])  # Run the game
                sys.exit()
            if event.key == pygame.K_ESCAPE:  # Quit game on ESC key
                running = False

    screen.blit(bg,(-700, 800))


pygame.quit()
sys.exit()