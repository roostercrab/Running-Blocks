import pygame
import random

# DEFINE PYGAME SETTINGS
pygame.init()
pygame.display.set_caption("Running Blocks")
window = pygame.display.set_mode((750, 500))

# DEFINE PLAYER
player_x = 50
player_y = 400
player_width = 40
player_height = 60
jumping = False
jump_progress = []
jump_velocity = 20

# DEFINE TREE
tree_x = 740
tree_y = 420
tree_width = 10
tree_height = 40
tree_list = []

# FUNCTIONS
def jump(player_y, jump_velocity):
    if jump_velocity < -20:
      jump_velocity = 20
      jump_progress = []
      return jump_progress
    else:
      player_y -= jump_velocity
      jump_velocity -= 1
      jump_progress = [player_y, jump_velocity]
      return jump_progress

# START THE GAME RUN LOOP
game_over = False
while game_over is False:
  # WINDOW.FILL IS HOW OUR BACKGROUND GETS PAINTED
  window.fill((0,0,0))
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      game_over = True

# THE GAME LOGIC WILL GO MOSTLY HERE

  # PLAYER BLOCK DRAWING
  pygame.draw.rect(window, (0,0,255), (player_x, player_y, player_width, player_height))

  # SHORTEN NAME FOR KEY PRESS DETECTION
  keypress = pygame.key.get_pressed()

  # IF SPACE IS PRESSED THEN JUMPING IS TRUE
  if keypress[pygame.K_SPACE]:
    jumping = True

  # IF JUMPING IS TRUE THEN RUN THE JUMP FUNCTION
  if jumping == True:
      jump_progress = jump(player_y, jump_velocity)

  # THIS CHECKS IF THE JUMP IS FINISHED SO THE PLAYER POSITION AND JUMP INFORMATION CAN BE RESET
  if jump_progress == []:
    player_y = 400
    jump_velocity = 20
    jumping = False

  # IF THE JUMP ISN'T FINISHED THEN JUMP_PROGRESS FROM JUMP FUNCTION CHANGES THE PLAYERS Y COORDINATE
  else:
    player_y = jump_progress[0]
    jump_velocity = jump_progress[1]

  # CREATE TREES AT RANDOM AND ADD THEM TO THE LIST (ALSO PRINT THE LIST FOR NOW TO VERIFY IT WORKS)
  tree_chance = random.randint(1, 100)
  if tree_chance == 1:
    tree_list.append([tree_x, tree_y])
    print(tree_list)

  # SUBTRACT THE TREE_SPEED FROM THE X COORDINATE OF EACH TREE IN THE LIST SO THAT THEY MOVE TOWARDS US
  for tree in tree_list:
      tree[0] -= tree_speed

  # DRAW EACH TREE FROM THE TREE_LIST ON THE EDGE OF THE SCREEN
  for tree in tree_list:
    pygame.draw.rect(window, (0,255,0), (tree[0], tree_y, tree_width, tree_height))

  pygame.time.delay(10)
  pygame.display.update()

pygame.quit()