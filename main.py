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
    pygame.image.load("assets/background_1.png"), (WIDTH, HEIGHT)
)
ARROW = pygame.transform.scale(
    pygame.image.load("assets/arrow_1.png"), (ARROW_WIDTH, ARROW_HEIGHT)
)
PLAYER = pygame.transform.scale(
    pygame.image.load("assets/player_1.png"), (PLAYER_WIDTH, PLAYER_HEIGHT)
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
    run = True
    clock = pygame.time.Clock()
    start_time = time.time()
    elapsed_time = 0
    arrow_add_increment = 2000
    arrow_time = 0
    arrows = []
    hit = False

    # Create player.
    player = pygame.Rect(
        (WIDTH / 2) - (PLAYER_WIDTH / 2),  # X position.
        HEIGHT - PLAYER_HEIGHT,  # Y position.
        PLAYER_WIDTH,  # X scale.
        PLAYER_HEIGHT,  # Y scale.
    )

    # Game loop.
    while run:
        elapsed_time = time.time() - start_time
        arrow_time += clock.tick(60)

        # Close the game.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

        # Create arrows.
        if arrow_time > arrow_add_increment:
            for _ in range(3):
                arrow_x = random.randint(0, WIDTH - ARROW_WIDTH)
                arrow = pygame.Rect(
                    arrow_x,  # X position.
                    -ARROW_HEIGHT,  # Y position.
                    ARROW_WIDTH,  # X scale.
                    ARROW_HEIGHT,  # Y scale.
                )
                arrows.append(arrow)

            # Make the next vave harder.
            arrow_add_increment = max(WIN_CONDITION, arrow_add_increment - 50)

            arrow_time = 0

        # Check collision.
        for arrow in arrows[:]:
            arrow.y += ARROW_VELOCITY
            if arrow.y > HEIGHT:
                arrows.remove(arrow)
            elif arrow.y + ARROW_HEIGHT >= player.y and arrow.colliderect(player):
                arrows.remove(arrow)
                hit = True
                break

        # Character movement.
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player.x - PLAYER_VELOCITY >= 0:
            player.x -= PLAYER_VELOCITY
        if keys[pygame.K_RIGHT] and player.x + PLAYER_VELOCITY + PLAYER_WIDTH <= WIDTH:
            player.x += PLAYER_VELOCITY

        # Game over screen.
        if hit:
            lost_text = FONT.render("You Lost!", 1, "purple")
            WINDOW.blit(
                lost_text,
                (
                    WIDTH / 2 - lost_text.get_width() / 2,
                    HEIGHT / 2 - lost_text.get_height() / 2,
                ),
            )
            pygame.display.update()
            pygame.time.delay(3000)
            break

        # You win screen.
        if arrow_add_increment == WIN_CONDITION:
            win_text = FONT.render("You Win!", 1, "green")
            WINDOW.blit(
                win_text,
                (
                    WIDTH / 2 - win_text.get_width() / 2,
                    HEIGHT / 2 - win_text.get_height() / 2,
                ),
            )
            pygame.display.update()
            pygame.time.delay(3000)
            break

        # Draw game frame.
        draw(player, elapsed_time, arrows)

    # Exit game when finished.
    pygame.quit()


# Check the file run directly or as a module.
if __name__ == "__main__":
    main()
