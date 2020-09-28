import pygame
import random
import sys
import speed
import collision


pygame.init()
clock = pygame.time.Clock()
myFont = pygame.font.SysFont("monospace", 35)

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

RED = (255, 0, 0)
BLUE = (0, 0, 255)
BACKGROUND_COLOR = (0,0,0)
ENEMY_SPEED = 10

# INITIALLY DEFINE PLAYER
player_size = 50
player_pos = [SCREEN_WIDTH/2, SCREEN_HEIGHT-2*player_size]
player_x_coord = player_pos[0]
player_y_coord = player_pos[1]
score = 0

# INITIALLY DEFINE ENEMY
enemy_size = 50
enemy_pos = [random.randint(0, SCREEN_WIDTH - enemy_size), 0]
enemy_x_coord = enemy_pos[0]
enemy_y_coord = enemy_pos[1]
enemy_list = [enemy_pos]

# DEFINE SCREEN
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# FUNCTIONS
def drop_enemies(enemy_list):
  delay = random.random()
  if len(enemy_list) < 10 and delay < 0.1:
    x_pos = random.randint(0, SCREEN_WIDTH - enemy_size)
    y_pos = 0
    enemy_list.append([x_pos, y_pos])

def draw_enemies(enemy_list):
  for enemy_pos in enemy_list:
      enemy_x_coord = enemy_pos[0]
      enemy_y_coord = enemy_pos[1]
      pygame.draw.rect(screen, BLUE, (enemy_x_coord, enemy_y_coord, enemy_size, enemy_size))

def update_enemy_positions(enemy_list, score):
  for idx, enemy_pos in enumerate(enemy_list):
    enemy_y_coord = enemy_pos[1]
    enemy_y_coord = int(enemy_y_coord)
    if enemy_y_coord >= 0 and enemy_y_coord < SCREEN_HEIGHT:
      enemy_pos[1] += ENEMY_SPEED
    else:
      enemy_list.pop(idx)
      score += 1
  return score


# GAME LOOP
game_over = False
while not game_over:
  for event in pygame.event.get():
    # print(event)
    if event.type == pygame.QUIT:
      sys.exit()

  # PLAYER BLOCK MOVEMENT
    if event.type == pygame.KEYDOWN:

      if event.key == pygame.K_LEFT:
        player_x_coord -= (player_size * .5)

      elif event.key == pygame.K_RIGHT:
        player_x_coord += (player_size * .5)

      player_pos[0] = player_x_coord

  # PAINT BACKGROUND
  screen.fill(BACKGROUND_COLOR)

  # ENEMY IMAGE DROP and DRAW
  drop_enemies(enemy_list)

  text = "Score: " + str(score)
  label = myFont.render(text, 1, (255,255,0))
  screen.blit(label, (SCREEN_WIDTH-200, SCREEN_HEIGHT-40))

  score = update_enemy_positions(enemy_list, score)
  print(score)

  if collision.collision_check(enemy_list, player_pos, player_size, enemy_size):
    game_over = True

  draw_enemies(enemy_list)

  # PLAYER IMAGE DRAW
  pygame.draw.rect(screen, RED, (player_x_coord, player_y_coord, player_size, player_size))

  # UPDATE SCREEN
  clock.tick(30)
  pygame.display.update()