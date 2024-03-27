import pygame
import sys

# Initialize pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 300, 300
LINE_WIDTH = 5
WHITE = (255, 255, 255)
LINE_COLOR = (0, 0, 0)
RED_COLOR = (255, 0, 0)
BLUE_COLOR = (0, 0, 255)
BOARD_ROWS = 3
BOARD_COLS = 3
SQUARE_SIZE = WIDTH // BOARD_ROWS

# Functions
def draw_board():
    for row in range(1, BOARD_ROWS):
        pygame.draw.line(screen, LINE_COLOR, (0, row * SQUARE_SIZE), (WIDTH, row * SQUARE_SIZE), LINE_WIDTH)
    for col in range(1, BOARD_COLS):
        pygame.draw.line(screen, LINE_COLOR, (col * SQUARE_SIZE, 0), (col * SQUARE_SIZE, HEIGHT), LINE_WIDTH)

def draw_mark(row, col, mark):
    posX = col * SQUARE_SIZE + SQUARE_SIZE // 2
    posY = row * SQUARE_SIZE + SQUARE_SIZE // 2
    if mark == 'X':
        pygame.draw.line(screen, RED_COLOR, (posX - SQUARE_SIZE // 4, posY - SQUARE_SIZE // 4),
                         (posX + SQUARE_SIZE // 4, posY + SQUARE_SIZE // 4), LINE_WIDTH)
        pygame.draw.line(screen, RED_COLOR, (posX + SQUARE_SIZE // 4, posY - SQUARE_SIZE // 4),
                         (posX - SQUARE_SIZE // 4, posY + SQUARE_SIZE // 4), LINE_WIDTH)
    else:
        pygame.draw.circle(screen, BLUE_COLOR, (posX, posY), SQUARE_SIZE // 4, LINE_WIDTH)

def check_winner(board):
    for row in range(BOARD_ROWS):
        if board[row][0] == board[row][1] == board[row][2] != 0:
            return board[row][0]
    for col in range(BOARD_COLS):
        if board[0][col] == board[1][col] == board[2][col] != 0:
            return board[0][col]
    if board[0][0] == board[1][1] == board[2][2] != 0:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != 0:
        return board[0][2]
    return 0

# Initialize screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic Tac Toe")

# Initialize variables
board = [[0 for _ in range(BOARD_COLS)] for _ in range(BOARD_ROWS)]
current_player = 'X'
game_over = False
winner = None

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if not game_over and event.type == pygame.MOUSEBUTTONDOWN:
            mouseX = event.pos[0] // SQUARE_SIZE
            mouseY = event.pos[1] // SQUARE_SIZE
            if board[mouseY][mouseX] == 0:
                board[mouseY][mouseX] = current_player
                if (winner := check_winner(board)) != 0:
                    game_over = True
                current_player = 'O' if current_player == 'X' else 'X'

    screen.fill(WHITE)
    draw_board()
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] != 0:
                draw_mark(row, col, board[row][col])

    if winner:
        font = pygame.font.Font(None, 36)
        text = font.render(f"Player {winner} wins!", True, LINE_COLOR)
        text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        screen.blit(text, text_rect)
    elif game_over:
        font = pygame.font.Font(None, 36)
        text = font.render("It's a draw!", True, LINE_COLOR)
        text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        screen.blit(text, text_rect)

    pygame.display.flip()
