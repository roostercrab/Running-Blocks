import pygame
import random

pygame.init()
pygame.display.set_caption("Running Blocks")
window = pygame.display.set_mode((500, 500))

player_x = 50
player_y = 400
player_width = 40
player_height = 60
jumping = False
jump_progress = []
jump_velocity = 20

tree_x = 490
tree_y = 420
tree_width = 10
tree_height = 40
tree_list = []
tree_speed = 5

#FUNCTIONS
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


run = True
while run:
  window.fill((0,0,0))
  pygame.draw.rect(window, (0,0,255), (player_x, player_y, player_width, player_height))
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      run = False

  if jump_progress == []:
    player_y = 400
    jump_velocity = 20
    jumping = False
  else:
    player_y = jump_progress[0]
    jump_velocity = jump_progress[1]

  # PLAYER BLOCK MOVEMENT
  keypress = pygame.key.get_pressed()

  if keypress[pygame.K_SPACE]:
    jumping = True

  if jumping == True:
      jump_progress = jump(player_y, jump_velocity)

  if len(tree_list) < 10:
    tree_chance = random.randint(1, 50)
    if tree_chance == 1:
      tree_list.append([tree_x, tree_y])

  for tree in tree_list:
    if tree[0] <= 0:
      tree_list.remove(tree)
    else:
      print(tree[0])
      tree[0] = tree[0] - tree_speed
      print(tree[0])

  for tree in tree_list:
    pygame.draw.rect(window, (0,255,0), (tree[0], tree_y, tree_width, tree_height))

  pygame.time.delay(10)
  pygame.display.update()

pygame.quit()
