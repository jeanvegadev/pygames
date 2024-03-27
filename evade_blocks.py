import pygame
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
FPS = 60

# Create the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Simple Game")

# Player
player_img = pygame.Surface((50, 50))
player_img.fill(RED)
player_rect = player_img.get_rect()
player_rect.center = (WIDTH // 2, HEIGHT - 50)

# Obstacles
obstacle_img = pygame.Surface((50, 50))
obstacle_img.fill(BLACK)
obstacles = []

# Clock
clock = pygame.time.Clock()

# Main game loop
running = True
while running:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move player
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_rect.x -= 5
    if keys[pygame.K_RIGHT]:
        player_rect.x += 5

    # Spawn obstacles
    if random.randint(1, 100) < 5:
        obstacle_rect = obstacle_img.get_rect()
        obstacle_rect.x = random.randint(0, WIDTH - obstacle_rect.width)
        obstacle_rect.y = 0
        obstacles.append(obstacle_rect)

    # Move obstacles
    for obstacle in obstacles:
        obstacle.y += 6
        if obstacle.colliderect(player_rect):
            running = False
        if obstacle.y > HEIGHT:
            obstacles.remove(obstacle)

    # Draw player
    screen.blit(player_img, player_rect)

    # Draw obstacles
    for obstacle in obstacles:
        screen.blit(obstacle_img, obstacle)

    pygame.display.flip()
    clock.tick(FPS)

# Quit Pygame
pygame.quit()
