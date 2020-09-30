import pygame
import random
import collision
import jump

# DEFINE PYGAME SETTINGS
pygame.init()
pygame.display.set_caption("Running Blocks")
window = pygame.display.set_mode((750, 500))
text_font = pygame.font.SysFont("monospace", 35)

# DEFINE PLAYER
player_x = 50
player_y = 400
player_width = 40
player_height = 60
jumping = False
jump_progress = []
jump_velocity = 20
player_life = 100
score = 0

# DEFINE TREE
tree_x = 740
tree_y = 420
tree_width = 10
tree_height = 40
tree_list = []
tree_speed = 5
tree_countdown = 0

# START THE GAME RUN LOOP
game_over = False
while game_over is False:
  window.fill((0,0,0))
  for event in pygame.event.get():
    #print(event)
    if event.type == pygame.QUIT:
      game_over = True

  # THE GAME IS OVER IF THE PLAYER'S LIFE GOES BELOW 0
  if player_life <= 0:
    game_over = True

  # PRINT SCORE TO SCREEN
  text = "Score: " + str(score)
  label = text_font.render(text, 1, (255,255,0))
  window.blit(label, (550, 460))

  # PRINT PLAYER LIFE TO SCREEN
  text = "Life: " + str(player_life)
  label = text_font.render(text, 1, (255,255,0))
  window.blit(label, (50, 460))

  # THIS CHECKS IF THE JUMP IS FINISHED SO THE PLAYER POSITION AND JUMP INFORMATION CAN BE RESET
  if jump_progress == []:
    player_y = 400
    jump_velocity = 20
    jumping = False
  # IF THE JUMP ISN'T FINISHED THEN THE JUMP PROGRESS FROM JUMP.UP FUNCTION CHANGES THE PLAYERS Y COORDINATE
  else:
    player_y = jump_progress[0]
    jump_velocity = jump_progress[1]

  # PLAYER BLOCK DRAWING
  pygame.draw.rect(window, (0,0,255), (player_x, player_y, player_width, player_height))

  # SHORTEN NAME FOR KEY PRESS DETECTION
  keypress = pygame.key.get_pressed()

  # IF SPACE IS PRESSED THEN JUMPING IS TRUE
  if keypress[pygame.K_SPACE]:
    jumping = True

  # IF JUMPING IS TRUE THEN RUN THE JUMP UP FUNCTION
  if jumping == True:
      jump_progress = jump.up(player_y, jump_velocity)

  # TREE COUNTDOWN IS SET TO 10 AFTER A TREE IS CREATED
  # TREES WILL ONLY APPEAR IF THERE ARE LESS THAN 5 ON THE SCREEN AND TREE COUNTDOWN IS EQUAL TO OR LESS THAN 0
  tree_countdown -= 1
  if len(tree_list) < 5 and tree_countdown <= 0:
    tree_chance = random.randint(1, 100)
    if tree_chance == 1:
      tree_list.append([tree_x, tree_y])
      tree_countdown = 10

  # CHECK EACH TREE IN THE TREE LIST AND SEE IF THEY HAVE GONE OFF SCREEN
  for tree in tree_list:
    if tree[0] <= 0:
      tree_list.remove(tree)
      score += 1
    # IF THEY HAVEN'T GONE OFF SCREEN THEN INCREASE THEIR X POSITION BY THE TREE SPEED
    else:
      tree[0] -= tree_speed

  # DRAW THE TREES AT THEIR NEW POSITION
  for tree in tree_list:
    pygame.draw.rect(window, (0,255,0), (tree[0], tree_y, tree_width, tree_height))

  hit = collision.check(player_x, player_y, player_height, player_width, tree_list, tree_height, tree_width)
  if hit == True:
    player_life -= 1

  pygame.time.delay(10)
  pygame.display.update()

pygame.quit()
