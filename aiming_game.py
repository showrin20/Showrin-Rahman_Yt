import pygame
import random
import sys

pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Aiming Game")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Clock
clock = pygame.time.Clock()

# Target
TARGET_RADIUS = 30
target_pos = [random.randint(TARGET_RADIUS, SCREEN_WIDTH - TARGET_RADIUS),
              random.randint(TARGET_RADIUS, SCREEN_HEIGHT - TARGET_RADIUS)]
target_speed = [4, 4]  # x and y speed

# Font
font = pygame.font.Font(None, 36)

score = 0
time_limit = 30  # seconds
start_ticks = pygame.time.get_ticks()

# Main game loop
running = True
while running:
    screen.fill(WHITE)
    
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Check if the target is hit
            mouse_pos = pygame.mouse.get_pos()
            distance = ((mouse_pos[0] - target_pos[0]) ** 2 + (mouse_pos[1] - target_pos[1]) ** 2) ** 0.5
            if distance <= TARGET_RADIUS:
                score += 1
                # Move the target to a new random location
                target_pos = [random.randint(TARGET_RADIUS, SCREEN_WIDTH - TARGET_RADIUS),
                              random.randint(TARGET_RADIUS, SCREEN_HEIGHT - TARGET_RADIUS)]

    # Move target
    target_pos[0] += target_speed[0]
    target_pos[1] += target_speed[1]

    if target_pos[0] - TARGET_RADIUS <= 0 or target_pos[0] + TARGET_RADIUS >= SCREEN_WIDTH:
        target_speed[0] = -target_speed[0]
    if target_pos[1] - TARGET_RADIUS <= 0 or target_pos[1] + TARGET_RADIUS >= SCREEN_HEIGHT:
        target_speed[1] = -target_speed[1]

    # Draw target
    pygame.draw.circle(screen, RED, target_pos, TARGET_RADIUS)

    # Draw crosshair
    mouse_pos = pygame.mouse.get_pos()
    pygame.draw.line(screen, BLACK, (mouse_pos[0] - 20, mouse_pos[1]), (mouse_pos[0] + 20, mouse_pos[1]), 2)
    pygame.draw.line(screen, BLACK, (mouse_pos[0], mouse_pos[1] - 20), (mouse_pos[0], mouse_pos[1] + 20), 2)

    # Draw score
    score_text = font.render(f"Score: {score}", True, BLACK)
    screen.blit(score_text, (10, 10))

    # Draw timer
    seconds = time_limit - (pygame.time.get_ticks() - start_ticks) // 1000
    timer_text = font.render(f"Time Left: {seconds}s", True, BLACK)
    screen.blit(timer_text, (SCREEN_WIDTH - 200, 10))

    # Check if time is up
    if seconds <= 0:
        running = False

    pygame.display.flip()
    clock.tick(60)


screen.fill(WHITE)
game_over_text = font.render("Game Over!", True, RED)
final_score_text = font.render(f"Your Score: {score}", True, BLACK)
screen.blit(game_over_text, (SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 - 50))
screen.blit(final_score_text, (SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2))
pygame.display.flip()
pygame.time.wait(3000)

# Quit Pygame
pygame.quit()
sys.exit()
