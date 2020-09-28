def collision_check(enemy_list, player_pos, player_size, enemy_size):
  player_x_coord = player_pos[0]
  player_y_coord = player_pos[1]
  player_x_coord = int(player_x_coord)
  player_y_coord = int(player_y_coord)
  for enemy_pos in enemy_list:
    enemy_x_coord = enemy_pos[0]
    enemy_y_coord = enemy_pos[1]
    enemy_x_coord = int(enemy_x_coord)
    enemy_y_coord = int(enemy_y_coord)

    if detect_collision(player_x_coord, player_y_coord, enemy_x_coord, enemy_y_coord, player_size, enemy_size):
      return True
  return False

def detect_collision(player_x_coord, player_y_coord, enemy_x_coord, enemy_y_coord, player_size, enemy_size):
  player_x_coord = int(player_x_coord)
  player_y_coord = int(player_y_coord)
  enemy_x_coord = int(enemy_x_coord)
  enemy_y_coord = int(enemy_y_coord)

  player_x_space = range(player_x_coord, player_x_coord + player_size)
  player_y_space = range(player_y_coord, player_y_coord + player_size)

  enemy_x_space = range(enemy_x_coord, enemy_x_coord + enemy_size)
  enemy_y_space = range(enemy_y_coord, enemy_y_coord + enemy_size)

  player_x_set = set(player_x_space)
  enemy_x_set = set(enemy_x_space)
  x_set_result = player_x_set.intersection(enemy_x_set)

  player_y_set = set(player_y_space)
  enemy_y_set = set(enemy_y_space)
  y_set_result = player_y_set.intersection(enemy_y_set)

  if x_set_result and y_set_result != set():
    print("GAME OVER")
    return True
  else:
    return False