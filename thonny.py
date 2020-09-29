player_x = 50
player_y = 400
player_width = 40
player_height = 60
jumping = False
jump_progress = []
jump_velocity = 10

#FUNCTIONS
def jump(player_y, jump_velocity):
    if jump_velocity < -10:
      jump_velocity = 10
      jump_progress = []
      return jump_progress
    else:
      player_y -= jump_velocity
      jump_velocity -= 1
      jump_progress = [player_y, jump_velocity]
      return jump_progress


run = True
while run:

  if jump_progress == []:
    jumping = False
  else:
    player_y = jump_progress[0]
    jump_velocity = jump_progress[1]

  # PLAYER BLOCK MOVEMENT
  keypress = True

  if keypress == True:
    jumping = True

  if jumping == True:
      jump_progress = jump(player_y, jump_velocity)