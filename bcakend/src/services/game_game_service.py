import src.repositories.game_game_repository as GameRepo

from bot_file.run_bot import runBot
from bot_file.win_check import isOnWin
from src.middleware.custom_error import CustomError
from src.utils.game_default import default_point
from itertools import zip_longest
from datetime import datetime

async def getGameDetail(game_id):
    try:
        detail = await GameRepo.getGameById(game_id)

        if detail is None:
            raise CustomError(400, 'invalid id')
        
        response = {
            'game_id': detail.id,
            'move_count': detail.game_detail.move_count,
            'p1_id': detail.player_1,
            'p2_id': detail.player_2,
            'winner': detail.winner,
            'p1_move': detail.game_detail.p1_move,
            'p2_move': detail.game_detail.p2_move,
            'all_move': [item for pair in zip_longest(detail.game_detail.p1_move, detail.game_detail.p2_move) for item in pair if item is not None],
            'board': detail.game_detail.board,
            'created_at': str(detail.created_at),
            'duration': str(detail.duration)
        }

        return response
    except CustomError as err:
        return err

async def createGame(player_1, player_2, game_type):
    try:
        player1Exist = await GameRepo.findPlayerById(player_1)

        if player1Exist is None:
            raise CustomError(400, 'invalid player')
        
        player2Exist = await GameRepo.findPlayerById(player_2)

        if player2Exist is None:
            raise CustomError(400, 'invalid player')
        
        newgame = await GameRepo.createNewGame(player_1, player_2, game_type)

        result = {
            'game_id': newgame.id,
            'game_type': newgame.game_type,
            'player1_id': newgame.player_1,
            'player1_name': player1Exist.account.name,
            'player2_id': newgame.player_2,
            'player2_name': player2Exist.account.name,
            'created_at': str(newgame.created_at)
        }

        return result
    except CustomError as err:
        return err

async def updateMove(game_id, player_type, move, board):
    try:
        if int(player_type) != 1:
            raise CustomError(400, 'invalid player type')
        
        gameExist = await GameRepo.getGameById(game_id)

        if gameExist is None:
            raise CustomError(400, 'invalid game id')
        
        if gameExist.winner != 'NOP':
            raise CustomError(418, 'ima teapot')

        p1_move = gameExist.game_detail.p1_move
        p2_move = gameExist.game_detail.p2_move
        move_count = gameExist.game_detail.move_count

        if int(player_type) == 1:
            p1_move += [move]
        elif int(player_type) == 2:
            p2_move += [move]
        else:
            raise CustomError(400, 'invalid player type')
        
        move_count += 1

        newdetail = await GameRepo.updateDetail(gameExist.game_detail.id, p1_move, p2_move, list(board), move_count)

        new_p1_move = newdetail.p1_move
        new_p2_move = newdetail.p2_move
        new_count = newdetail.move_count

        if len(new_p2_move) > len(new_p1_move):
            new_p2_move = new_p2_move.pop()
            new_count -= 1
        
        result = {
            'p1_move': new_p1_move,
            'p2_move': new_p2_move,
            'all_move': [item for pair in zip_longest(new_p1_move, new_p2_move) for item in pair if item is not None],
            'move_count': new_count,
            'board': newdetail.board
        }
        
        return result
    except CustomError as err:
        return err

async def updateBotMove(game_id, board):
    try:
        gameExist = await GameRepo.getGameById(game_id)
        
        if gameExist is None:
            raise CustomError(400, 'invalid game id')
        
        if gameExist.winner != 'NOP':
            raise CustomError(418, 'ima teapot')
        
        if list(board) != gameExist.game_detail.board:
            raise CustomError(400, 'invalid board')
        
        if gameExist.game_detail.move_count % 2 == 0:
            raise CustomError(403, 'not bot turn')
        
        modified_board = [gameExist.game_detail.board[i:i+3] for i in range(0, len(gameExist.game_detail.board), 3)]

        if isOnWin(modified_board) is True:
            raise CustomError(400, 'already win')

        data = runBot(modified_board)

        new_board = data['board']
        new_move = data['move']
        
        new_detail = await GameRepo.updateDetail(
            detail_id=gameExist.game_detail.id,
            p1_move=gameExist.game_detail.p1_move,
            p2_move=gameExist.game_detail.p2_move + [new_move],
            board=new_board,
            move_count=gameExist.game_detail.move_count + 1
        )

        result = {
            'p1_move': new_detail.p1_move,
            'p2_move': new_detail.p2_move,
            'all_move': [item for pair in zip_longest(new_detail.p1_move, new_detail.p2_move) for item in pair if item is not None],
            'move_count': new_detail.move_count,
            'board': new_detail.board
        }
        
        return result
    except CustomError as err:
        return err

async def endGame(game_id, winner):
    try:
        gameExist = await GameRepo.getGameById(game_id)
        
        if gameExist is None:
            raise CustomError(400, 'invalid game id')
        
        if gameExist.winner != 'NOP':
            raise CustomError(418, 'ima teapot')
        
        date_obj = datetime.strptime(str(gameExist.created_at), '%Y-%m-%d %H:%M:%S.%f%z')
        now = datetime.now(date_obj.tzinfo)
        duration = (now - date_obj).total_seconds()
        
        if winner == 'NOP':
            raise CustomError(400, 'winner required')

        point = default_point(gameExist.game_type)

        player_1 = await GameRepo.findPlayerById(gameExist.player_1)
        player_2 = await GameRepo.findPlayerById(gameExist.player_2)
        winner_id = ''

        if player_1 is None or player_2 is None:
            raise CustomError(404, 'player not found')
        
        if winner == 'P1':
            await GameRepo.updateUserElo(player_1.id, player_1.game_elo + point)
            await GameRepo.updateUserElo(player_2.id, player_2.game_elo - point)
            winner_id = player_1.id
        elif winner == 'P2':
            await GameRepo.updateUserElo(player_1.id, player_1.game_elo - point)
            await GameRepo.updateUserElo(player_2.id, player_2.game_elo + point)
            winner_id = player_2.id
        else:
            raise CustomError(400, 'invalid winner')

        end_game = await GameRepo.updateWinner(game_id, winner, int(duration))

        result = {
            'game_id': end_game.id,
            'winner': winner_id,
            'duration': str(end_game.duration),
            'point': point
        }
        return result
    except CustomError as err:
        return err