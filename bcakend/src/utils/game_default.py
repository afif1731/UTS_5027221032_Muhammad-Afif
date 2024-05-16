default_board = ['O', 'X', 'O', '_', '_', '_', 'X', 'O', 'X']
p1 = 'O'
p2 = 'X'
pdef = '_'
bot_difficulty = 8

def default_point(game_type):
    if game_type == 'PVB':
        return 5
    elif game_type == 'OPVP':
        return 0
    elif game_type == 'LPVP':
        return 5
    
    return 0