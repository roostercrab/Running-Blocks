import pygame
import sys
 

pygame.init()
clock = pygame.time.Clock()

# INITIALIZE SCREEN AND COLORS
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 800
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BACKGROUND_COLOR = (0,0,0)

#INITIALIZE SCORE
score = 0

# INITIALIZE PLAYER
player_size = 50
player_pos = [50, 525]
player_x_coord = player_pos[0]
player_y_coord = player_pos[1]
player_color = BLUE

# INITIALIZE ENEMY
enemy_size = 50
enemy_pos = [750, 525]
enemy_x_coord = enemy_pos[0]
enemy_y_coord = enemy_pos[1]
enemy_color = GREEN
enemy_list = [enemy_pos]

# GAME LOOP
game_over = False
while not game_over:
  for event in pygame.event.get():
    print(event)
    if event.type == pygame.QUIT:
      sys.exit()

  # PLAYER JUMP
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_SPACE:
        hangtime = 1
        while hangtime <= 50:
          player_y_coord -= hangtime
          hangtime = hangtime + hangtime
        player_pos[1] = player_y_coord
        pygame.draw.rect(screen, player_color, (player_x_coord, player_y_coord, player_size, player_size))

        hangtime = 50
        while hangtime >= 1:
          player_y_coord += hangtime
          hangtime = hangtime - hangtime
        player_pos[1] = player_y_coord
        pygame.draw.rect(screen, player_color, (player_x_coord, player_y_coord, player_size, player_size))


  # PAINT BACKGROUND
  screen.fill(BACKGROUND_COLOR)

  # PLAYER IMAGE DRAW
  pygame.draw.rect(screen, player_color, (player_x_coord, player_y_coord, player_size, player_size))

  # ENEMY IMAGE DRAW
  pygame.draw.rect(screen, enemy_color, (enemy_x_coord, enemy_y_coord, enemy_size, enemy_size))

  # UPDATE SCREEN
  clock.tick(30)
  pygame.display.update()