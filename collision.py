def collision_check(tree_list, player_pos, player_size, tree_size):
  player_x = player_pos[0]
  player_y = player_pos[1]
  player_x = int(player_x)
  player_y = int(player_y)
  for tree_pos in tree_list:
    tree_x = tree_pos[0]
    tree_y = tree_pos[1]
    tree_x = int(tree_x)
    tree_y = int(tree_y)

    if detect_collision(player_x, player_y, tree_x, tree_y, player_size, tree_size):
      return True
  return False

def detect_collision(player_x, player_y, tree_x, tree_y, player_size, tree_size):
  player_x = int(player_x)
  player_y = int(player_y)
  tree_x = int(tree_x)
  tree_y = int(tree_y)

  player_x_space = range(player_x, player_x + player_width)
  player_y_space = range(player_y, player_y + player_height)

  tree_x_space = range(tree_x, tree_x + tree_size)
  tree_y_space = range(tree_y, tree_y + tree_size)

  player_x_set = set(player_x_space)
  tree_x_set = set(tree_x_space)
  x_set_result = player_x_set.intersection(tree_x_set)

  player_y_set = set(player_y_space)
  tree_y_set = set(tree_y_space)
  y_set_result = player_y_set.intersection(tree_y_set)

  if x_set_result and y_set_result != set():
    print("GAME OVER")
    return True
  else:
    return False