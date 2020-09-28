import pygame
import random
import sys
import speed
import collision

pygame.init()
clock = pygame.time.Clock()
myFont = pygame.font.SysFont("monospace", 35)

SCREEN_HEIGHT = 600
SCREEN_WIDTH = 800

GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BACKGROUND_COLOR = (0,0,0)
ENEMY_SPEED = 10

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

# INITIALIZE SCREEN
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# GAME LOOP
game_over = False
while not game_over:
  for event in pygame.event.get():
    print(event)
    if event.type == pygame.QUIT:
      sys.exit()

  # PLAYER BLOCK MOVEMENT
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_UP:
        player_y_coord -= player_size * 2
      # elif event.key == pygame.K_DOWN:
      #   player_size = player_size * .5

      player_pos[1] = player_y_coord
    
    if event.type == pygame.KEYUP:
      if event.key == pygame.K_UP:
        player_y_coord += player_size * 2
      # elif event.key == pygame.K_DOWN:
      #   player_size = player_size * 2

      player_pos[1] = player_y_coord

  # PAINT BACKGROUND
  screen.fill(BACKGROUND_COLOR)

  # ENEMY IMAGE DROP and DRAW
#   drop_enemies(enemy_list)

#   text = "Score: " + str(score)
#   label = myFont.render(text, 1, (255,255,0))
#   screen.blit(label, (SCREEN_WIDTH-200, SCREEN_HEIGHT-40))

#   score = update_enemy_positions(enemy_list, score)
#   print(score)

#   if collision.collision_check(enemy_list, player_pos, player_size, enemy_size):
#     game_over = True

#   draw_enemies(enemy_list)

  # PLAYER IMAGE DRAW
  pygame.draw.rect(screen, player_color, (player_x_coord, player_y_coord, player_size, player_size))

  # ENEMY IMAGE DRAW
  pygame.draw.rect(screen, enemy_color, (enemy_x_coord, enemy_y_coord, enemy_size, enemy_size))

  # UPDATE SCREEN
  clock.tick(30)
  pygame.display.update()