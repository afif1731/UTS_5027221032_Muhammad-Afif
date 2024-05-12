from src.utils.game_default import bot_difficulty, p2, pdef
from bot_file.tapatan_bot import findBestMove, make_move

rrow = ['1', '2', '3']
ccol = ['A', 'B', 'C']

def moveCodeDecode(row, col, code):
    match int(code):
        case -1:
            col -= 1
        case 1:
            col += 1
        case -2:
            row -= 1
        case 2:
            row += 1
        case -3:
            row -= 1
            col -= 1
        case 3:
            row += 1
            col += 1
        case -4:
            row -= 1
            col += 1
        case 4:
            row += 1
            col += 1
    
    return (row, col)

def runBot(b):
    best_move = findBestMove(board=b, max_depth=bot_difficulty)

    new_b = make_move(board=b, prow=best_move[0], pcol=best_move[1], move_code=best_move[2], piece=p2, pdefault=pdef)

    from_p = ccol[best_move[1]] + rrow[best_move[0]]
    move_to = moveCodeDecode(best_move[0], best_move[1], best_move[2])
    to_p = ccol[move_to[1]] + rrow[move_to[0]]
    new_move = from_p + to_p


    flat_b = [elemen for sublist in new_b for elemen in sublist]
    return {
        'board': flat_b,
        'move': new_move
    }
