import pygame

pygame.init()
pygame.display.set_caption("Running Blocks")
window = pygame.display.set_mode((500, 500))

player_x = 50
player_y = 400
player_width = 40
player_height = 60
velocity = 5

jumping = False
hangtime = 10

run = True
while run:


  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      run = False

    # PLAYER BLOCK MOVEMENT
    keypress = pygame.key.get_pressed()

    if not(jumping):
      if keypress[pygame.K_SPACE]:
        jumping = True
    else:
      if hangtime >= -10:
        gravity = 1
        if hangtime < 0:
          gravity = -1
        player_y -= int((hangtime ** 2) * 0.5 * gravity)
        hangtime -= 1
      else:
        jumping = False
        hangtime = 10


  window.fill((0,0,0))
  pygame.draw.rect(window, (0,0,255), (player_x, player_y, player_width, player_height))
  pygame.time.delay(30)
  pygame.display.update()

pygame.quit()
