import pygame

pygame.init()
pygame.display.set_caption("Running Blocks")
window = pygame.display.set_mode((500, 500))

player_x = 50
player_y = 400
player_width = 40
player_height = 60
jumping = False
jump_velocity = 10

run = True
while run:
  window.fill((0,0,0))
  pygame.draw.rect(window, (0,0,255), (player_x, player_y, player_width, player_height))
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      run = False

    # PLAYER BLOCK MOVEMENT

    keypress = pygame.key.get_pressed()

    if keypress[pygame.K_SPACE]:
      jumping = True
      if jumping == True:
        player_y -= jump_velocity
        print(jump_velocity )
        jump_velocity -= 1
        if jump_velocity < -10:
          jump_velocity = 10
          jumping = False


  pygame.time.delay(1)
  pygame.display.update()

pygame.quit()
