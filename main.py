# Libraries and modules.
import pygame
import time
import random

# Initializations.
pygame.font.init()

# Screen constants.
WIDTH = 500
HEIGHT = 400

# Player constants.
PLAYER_WIDTH = 40
PLAYER_HEIGHT = 60
PLAYER_VELOCITY = 10

# Arrow constants.
ARROW_WIDTH = 20
ARROW_HEIGHT = 50
ARROW_VELOCITY = 5

# Game constants.
WIN_CONDITION = 500

# Resources.
FONT = pygame.font.SysFont("comicsans", 30)
BACKGROUND = pygame.transform.scale(
    pygame.image.load("images/background_1.png"), (WIDTH, HEIGHT)
)
ARROW = pygame.transform.scale(
    pygame.image.load("images/arrow_1.png"), (ARROW_WIDTH, ARROW_HEIGHT)
)
PLAYER = pygame.transform.scale(
    pygame.image.load("images/player_1.png"), (PLAYER_WIDTH, PLAYER_HEIGHT)
)

# Set pygame window.
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Escape from Arrows")


# Draw game frame.
def draw(player, elapsed_time, arrows):
    # Background.
    WINDOW.blit(BACKGROUND, (0, 0))

    # Score text.
    time_text = FONT.render(f"Time: {round(elapsed_time)}s", 1, "white")
    WINDOW.blit(time_text, (10, 10))

    # Arrows.
    for arrow in arrows:
        WINDOW.blit(ARROW, arrow)

    # Player
    WINDOW.blit(PLAYER, player)

    # Update the  display.
    pygame.display.update()


# Main function.
def main():
    ...


# Check the file run directly or as a module.
if __name__ == "__main__":
    main()
