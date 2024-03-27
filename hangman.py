import pygame
import random
import sys

# Initialize pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)
FONT_SIZE = 40
ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

# Load words
with open('words.txt', 'r') as file:
    words = [line.strip().upper() for line in file]

# Functions
def draw_hangman(screen, mistakes):
    if mistakes >= 1:  # Head
        pygame.draw.circle(screen, GREEN, (400, 200), 40)
    if mistakes >= 2:  # Body
        pygame.draw.line(screen, GREEN, (400, 240), (400, 400), 5)
    if mistakes >= 3:  # Left arm
        pygame.draw.line(screen, GREEN, (400, 280), (300, 200), 5)
    if mistakes >= 4:  # Right arm
        pygame.draw.line(screen, GREEN, (400, 280), (500, 200), 5)
    if mistakes >= 5:  # Left leg
        pygame.draw.line(screen, GREEN, (400, 400), (300, 500), 5)
    if mistakes >= 6:  # Right leg
        pygame.draw.line(screen, GREEN, (400, 400), (500, 500), 5)

def draw_word(screen, word, guessed_letters):
    font = pygame.font.Font(None, FONT_SIZE)
    display_word = ''
    for letter in word:
        if letter in guessed_letters:
            display_word += letter + ' '
        else:
            display_word += '_ '
    text = font.render(display_word, True, BLACK)
    screen.blit(text, (300, 500))

def draw_alphabet(screen, guessed_letters):
    font = pygame.font.Font(None, FONT_SIZE)
    x, y = 50, 50
    for letter in ALPHABET:
        if letter not in guessed_letters:
            text = font.render(letter, True, BLACK)
            screen.blit(text, (x, y))
        x += 40
        if x >= 750:
            x = 50
            y += 50

def display_message(screen, message, color):
    font = pygame.font.Font(None, 50)
    text = font.render(message, True, color)
    text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    screen.blit(text, text_rect)

def main():
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Hangman")

    mistakes = 0
    guessed_letters = set()
    word = random.choice(words)

    clock = pygame.time.Clock()

    while True:
        screen.fill(WHITE)
        draw_hangman(screen, mistakes)
        draw_word(screen, word, guessed_letters)
        draw_alphabet(screen, guessed_letters)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouseX, mouseY = pygame.mouse.get_pos()
                x, y = 50, 50
                for letter in ALPHABET:
                    if x <= mouseX <= x + 40 and y <= mouseY <= y + 40:
                        guessed_letters.add(letter)
                        if letter not in word:
                            mistakes += 1
                        break
                    x += 40
                    if x >= 750:
                        x = 50
                        y += 50

        if mistakes >= 6:
            display_message(screen, f"The word was {word}", RED)
        elif all(letter in guessed_letters for letter in word):
            display_message(screen, "You win!", GREEN)

        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()
