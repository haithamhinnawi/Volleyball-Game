# Volleyball Game

A simple 2-player volleyball game created using Pygame. The game features two players, a ball, and a net, with jumping mechanics and a match timer.

---

## Features
- **Two players**: Player 1 (Blue) and Player 2 (Green).
- **Interactive gameplay**: Players move horizontally and jump to hit the ball.
- **Real-time ball physics**: The ball bounces off walls, players, and the net.
- **Scoring system**: Points are awarded when the ball touches the ground on the opponent's side or hits the net.
- **Match timer**: Each match is limited to 60 seconds.
- **Winning condition**: The first player to reach 5 points wins, or the player with the highest score at the end of the timer.

---

## Controls
- **Player 1 (Blue)**
  - Move Left: `LEFT Arrow`
  - Move Right: `RIGHT Arrow`
  - Jump: `UP Arrow`
- **Player 2 (Green)**
  - Move Left: `A`
  - Move Right: `D`
  - Jump: `W`

---

## How to Play
1. Run the game.
2. Use the controls to move and jump, trying to hit the ball to the opponent's side.
3. Score points by:
   - Letting the ball hit the ground on the opponent's side.
   - Making the ball hit the net.
4. The player with the highest score when time runs out or the first to reach 5 points wins.

---

## Game Mechanics
- **Jumping**: Players can jump up to a height of 100 pixels.
- **Gravity**: Automatically brings players back down after jumping.
- **Ball physics**: 
  - Bounces off walls, net, and players.
  - Adjusts speed and direction on collision.
- **Net interaction**: Both players score a point if the ball hits the net.

---

## Installation
1. Ensure Python is installed on your system.
2. Install Pygame:
   ```bash
   pip install pygame
   ```
3. Run the game:
   ```bash
   python volleyball_game.py
   ```

---

## Resetting the Game
- After a game ends, press the `SPACE` key to restart.

---

## Future Improvements
- Add AI for single-player mode.
- Introduce power-ups or penalties.
- Customize match time and winning score.
