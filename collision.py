def check(
    player_x, player_y, player_height, player_width, tree_list, tree_height, tree_width
):
    player_x_space = range(player_x, player_x + player_width)
    player_y_space = range(player_y, player_y + player_height)
    player_x_set = set(player_x_space)

    for tree in tree_list:
        tree_x = int(tree[0])
        tree_y = int(tree[1])

        tree_x_space = range(tree_x, tree_x + tree_width)
        tree_y_space = range(tree_y, tree_y + tree_height)
        tree_x_set = set(tree_x_space)

        x_set_result = player_x_set.intersection(tree_x_set)

        player_y_set = set(player_y_space)
        tree_y_set = set(tree_y_space)
        y_set_result = player_y_set.intersection(tree_y_set)

        if x_set_result and y_set_result != set():
            return True
        return False
