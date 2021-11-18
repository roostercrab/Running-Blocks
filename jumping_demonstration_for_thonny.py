# DEFINE PLAYER
player_x = 50
player_y = 400
player_width = 40
player_height = 60
jumping = True
jump_progress = []
jump_velocity = 20


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


while True == True:
    # IF JUMPING IS TRUE THEN RUN THE JUMP FUNCTION
    jumping = True

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
