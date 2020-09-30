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

game_over = False
while game_over != True:
  window.fill((0,0,0))
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      game_over = True

  # PLAYER
  pygame.draw.rect(window, (0,0,255), (player_x, player_y, player_width, player_height))

  pygame.time.delay(10)
  pygame.display.update()

pygame.quit()
