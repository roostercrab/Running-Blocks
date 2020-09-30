import pygame

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

  pygame.time.delay(10)
  pygame.display.update()

pygame.quit()
