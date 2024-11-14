import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions and game constants
WIDTH, HEIGHT = 600, 400
PLAYER_WIDTH, PLAYER_HEIGHT = 40, 40
BALL_SIZE = 20
NET_WIDTH, NET_HEIGHT = 10, 80
PLAYER_SPEED = 10
BALL_SPEED_X, BALL_SPEED_Y = 5, 5
WINNING_SCORE = 5
MATCH_TIME = 60  # Total match time in seconds

# Color definitions
BLUE = (0, 0, 255)
GREEN = (0, 128, 0)
RED = (255, 0, 0)
LIGHT_BLUE = (173, 216, 230)
GRAY = (128, 128, 128)
BLACK = (0, 0, 0)

# Setup display, font, and initial positions
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Volleyball Game")
font = pygame.font.Font(None, 36)

# Player starting positions and scores
player1_x, player2_x = 20, WIDTH - PLAYER_WIDTH - 20
player1_y, player2_y = HEIGHT - PLAYER_HEIGHT, HEIGHT - PLAYER_HEIGHT
player1_score, player2_score = 0, 0

# Ball starting position and speed
ball_x, ball_y = WIDTH // 2 - BALL_SIZE // 2, HEIGHT // 2 - BALL_SIZE // 2
ball_speed_x, ball_speed_y = BALL_SPEED_X, BALL_SPEED_Y

# Game state variables
game_over = False
player1_jumping, player2_jumping = False, False  # Track if players are jumping
jump_height = 0
gravity = 1  # Gravity factor for jumping
match_time = MATCH_TIME

def reset_ball():
    """Reset the ball to the center and apply the current speed."""
    global ball_x, ball_y, ball_speed_x, ball_speed_y
    ball_x, ball_y = WIDTH // 2 - BALL_SIZE // 2, HEIGHT // 2 - BALL_SIZE // 2
    ball_speed_x = random.choice([-abs(ball_speed_x), abs(ball_speed_x)])
    ball_speed_y = abs(ball_speed_y)

def draw_game():
    """Render all game elements on the screen."""
    screen.fill(LIGHT_BLUE)
    # Draw players
    pygame.draw.rect(screen, BLUE, (player1_x, player1_y, PLAYER_WIDTH, PLAYER_HEIGHT))
    pygame.draw.rect(screen, GREEN, (player2_x, player2_y, PLAYER_WIDTH, PLAYER_HEIGHT))
    # Draw ball and net
    pygame.draw.ellipse(screen, RED, (ball_x, ball_y, BALL_SIZE, BALL_SIZE))
    pygame.draw.rect(screen, GRAY, (WIDTH // 2 - NET_WIDTH // 2, HEIGHT - NET_HEIGHT, NET_WIDTH, NET_HEIGHT))
    # Display scores and time remaining
    score_text1 = font.render(f"Player 1: {player1_score}", True, BLACK)
    score_text2 = font.render(f"Player 2: {player2_score}", True, BLACK)
    screen.blit(score_text1, (10, 10))
    screen.blit(score_text2, (WIDTH - score_text2.get_width() - 10, 10))
    time_text = font.render(f"Time: {int(match_time)}", True, BLACK)
    screen.blit(time_text, (WIDTH // 2 - time_text.get_width() // 2, 10))
    pygame.display.flip()

def update_score(winner):
    """Increase the score for the winner."""
    global player1_score, player2_score, game_over, ball_speed_x, ball_speed_y
    if winner == "player1":
        player1_score += 1
    elif winner == "player2":
        player2_score += 1
    elif winner == "net":
        player1_score += 1
        player2_score += 1
    reset_ball()
    # End game if a player reaches winning score
    if player1_score == WINNING_SCORE or player2_score == WINNING_SCORE:
        game_over = True

def game_loop():
    """Main game loop for managing events, updating positions, and checking for collisions."""
    global player1_x, player2_x, player1_y, player2_y, ball_x, ball_y, ball_speed_x, ball_speed_y
    global game_over, player1_jumping, player2_jumping, jump_height, match_time

    clock = pygame.time.Clock()  # Initialize clock for frame rate control
    while not game_over and match_time > 0:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # Exit game
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                # Start jumping if UP (Player 1) or W (Player 2) is pressed
                if event.key == pygame.K_UP and not player1_jumping:
                    player1_jumping = True
                    jump_height = 0
                if event.key == pygame.K_w and not player2_jumping:
                    player2_jumping = True
                    jump_height = 0

        keys = pygame.key.get_pressed()
        # Move Player 1 horizontally within left boundary and center net
        if keys[pygame.K_LEFT] and player1_x > 0:
            player1_x -= PLAYER_SPEED
        if keys[pygame.K_RIGHT] and player1_x + PLAYER_WIDTH < WIDTH // 2 - NET_WIDTH // 2:
            player1_x += PLAYER_SPEED
        # Move Player 2 horizontally within net and right boundary
        if keys[pygame.K_a] and player2_x > WIDTH // 2 + NET_WIDTH // 2:
            player2_x -= PLAYER_SPEED
        if keys[pygame.K_d] and player2_x + PLAYER_WIDTH < WIDTH:
            player2_x += PLAYER_SPEED

        # Handle Player 1 jumping and gravity
        if player1_jumping:
            player1_y -= 10  # Move up while jumping
            jump_height += 10
            if jump_height >= 100:  # Limit jump height
                player1_jumping = False
        else:
            # Apply gravity to bring player down
            if player1_y < HEIGHT - PLAYER_HEIGHT:
                player1_y += gravity * 10
            else:
                player1_y = HEIGHT - PLAYER_HEIGHT

        # Handle Player 2 jumping and gravity
        if player2_jumping:
            player2_y -= 10
            jump_height += 10
            if jump_height >= 100:
                player2_jumping = False
        else:
            if player2_y < HEIGHT - PLAYER_HEIGHT:
                player2_y += gravity * 10
            else:
                player2_y = HEIGHT - PLAYER_HEIGHT

        # Move ball and handle boundary collisions
        ball_x += ball_speed_x
        ball_y += ball_speed_y
        # Bounce ball off left or right walls
        if ball_x <= 0 or ball_x + BALL_SIZE >= WIDTH:
            ball_speed_x *= -1
        # Bounce ball off top wall
        if ball_y <= 0:
            ball_speed_y *= -1

        # Ball collision with Player 1
        if player1_x < ball_x + BALL_SIZE < player1_x + PLAYER_WIDTH and player1_y < ball_y + BALL_SIZE < player1_y + PLAYER_HEIGHT:
            ball_speed_y = -abs(ball_speed_y)

        # Ball collision with Player 2
        if player2_x < ball_x + BALL_SIZE < player2_x + PLAYER_WIDTH and player2_y < ball_y + BALL_SIZE < player2_y + PLAYER_HEIGHT:
            ball_speed_y = -abs(ball_speed_y)

        # Ball collision with net
        if WIDTH // 2 - NET_WIDTH // 2 < ball_x < WIDTH // 2 + NET_WIDTH // 2 and HEIGHT - NET_HEIGHT < ball_y + BALL_SIZE < HEIGHT:
            ball_speed_x *= -1
            update_score("net")

        # Ball falls out of bounds; score point for other player
        if ball_y + BALL_SIZE >= HEIGHT:
            if ball_x < WIDTH / 2:
                update_score("player2")
            else:
                update_score("player1")

        match_time -= 1 / 60  # Decrease match time
        draw_game()
        clock.tick(60)  # Maintain 60 FPS

    # Determine and display winner after match ends
    if match_time <= 0:
        if player1_score > player2_score:
            winner = "Player 1"
        elif player2_score > player1_score:
            winner = "Player 2"
        else:
            winner = "Tie"
    else:
        winner = "Player 1" if player1_score == WINNING_SCORE else "Player 2"
    display_winner(winner)

def display_winner(winner):
    """Display the winner and offer option to restart."""
    screen.fill(LIGHT_BLUE)
    # Show winner message
    win_text = font.render(f"{winner} wins!", True, BLACK)
    screen.blit(win_text, (WIDTH // 2 - win_text.get_width() // 2, HEIGHT // 2))
    # Prompt for restarting the game
    restart_text = font.render("Press Space to restart", True, BLACK)
    screen.blit(restart_text, (WIDTH // 2 - restart_text.get_width() // 2, HEIGHT // 2 + 50))
    pygame.display.flip()
    # Wait for Space key to restart
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    waiting = False
    # Reset game variables
    global player1_score, player2_score, game_over, match_time, ball_speed_x, ball_speed_y
    player1_score, player2_score = 0, 0
    game_over = False
    match_time = MATCH_TIME
    ball_speed_x, ball_speed_y = BALL_SPEED_X, BALL_SPEED_Y
    game_loop()

# Start the game loop
game_loop()