from src.config.prisma_config import prisma
from src.utils.game_default import default_board

async def findPlayerById(user_id):
    return await prisma.gameuser.find_first(
        where={
            'id': user_id
        },
        include={
            'account': True
        }
    )

async def getGameById(game_id):
    return await prisma.gamelog.find_first(
        where={
            'id': game_id
        },
        include={
            'game_detail': True
        }
    )

async def createNewGame(p1_id, p2_id, game_type):
    detail = await prisma.gamedetail.create(
        data={
            'board': default_board
        }
    )

    return await prisma.gamelog.create(
        data={
            'player_1': p1_id,
            'player_2': p2_id,
            'game_type': game_type,
            'detail': detail.id
        }
    )

async def updateDetail(detail_id, p1_move, p2_move, board, move_count):
    return await prisma.gamedetail.update(
        where={
            'id': detail_id
        },
        data={
            'p1_move': p1_move,
            'p2_move': p2_move,
            'board': board,
            'move_count': move_count
        }
    )

async def updateUserElo(user_id, elo):
    return await prisma.gameuser.update(
        where={
            'id': user_id
        },
        data={
            'game_elo': elo
        }
    )

async def updateWinner(game_id, winner, duration):
    return await prisma.gamelog.update(
        where={
            'id': game_id
        },
        data={
            'winner': winner,
            'duration': duration
        }
    )