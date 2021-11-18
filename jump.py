def up(player_y, jump_velocity):
    if jump_velocity < -20:
        jump_velocity = 20
        jump_progress = []
        return jump_progress
    else:
        player_y -= jump_velocity
        jump_velocity -= 1
        jump_progress = [player_y, jump_velocity]
        return jump_progress
