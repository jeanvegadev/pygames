import pygame
import sys

# Initialize pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 600, 500
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
ORANGE = (255, 127, 80)
BALL_RADIUS = 11
PADDLE_WIDTH, PADDLE_HEIGHT = 100, 10
PADDLE_SPEED = 7
BALL_SPEED_X = 4
BALL_SPEED_Y = 4

# Initialize screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong")

# Paddle class
class Paddle:
    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)

    def draw(self, surface):
        pygame.draw.rect(surface, BLACK, self.rect)

    def move(self, direction):
        self.rect.x += direction * PADDLE_SPEED
        if self.rect.left < 0:
            self.rect.left = 0
        elif self.rect.right > WIDTH:
            self.rect.right = WIDTH

# Ball class
class Ball:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x - BALL_RADIUS, y - BALL_RADIUS, BALL_RADIUS * 2, BALL_RADIUS * 2)
        self.velocity = [BALL_SPEED_X, BALL_SPEED_Y]

    def draw(self, surface):
        pygame.draw.circle(surface, ORANGE, self.rect.center, BALL_RADIUS)

    def move(self):
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]
        if self.rect.x >= WIDTH or self.rect.x <= 0:
            self.velocity[0] = -self.velocity[0]
        if self.rect.top <= 0:
            self.velocity[1] = -self.velocity[1]


def check_collision(ball, paddle):
    if (paddle.rect.left <= ball.rect.x <= paddle.rect.right) and (
            paddle.rect.top <= ball.rect.y + BALL_RADIUS <= paddle.rect.bottom):
        return True
    return False


# Main function
def main():
    # Initialize variables
    paddle = Paddle(WIDTH // 2 - PADDLE_WIDTH // 2, HEIGHT - PADDLE_HEIGHT - 10, PADDLE_WIDTH, PADDLE_HEIGHT)
    ball = Ball(WIDTH // 2, 15)

    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            paddle.move(-1)
        if keys[pygame.K_RIGHT]:
            paddle.move(1)

        screen.fill(WHITE)
        paddle.draw(screen)
        ball.draw(screen)
        ball.move()

        if check_collision(ball, paddle):
            ball.velocity[1] = -ball.velocity[1]

        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()
