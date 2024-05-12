from src.config.prisma_config import prisma

async def findUserById(user_id):
    return await prisma.gameuser.find_first(
        where={
            'id': user_id
        },
        include={
            'account': True
        }
    )

async def getTopElo(query):
    return await prisma.gameuser.find_many(
        take=int(query['limit']),
        skip= (int(query['page']) - 1)*int(query['limit']),
        order={'game_elo': query['sort']},
        include={'account': True}
    )

async def countUser():
    return await prisma.gameuser.count(
        select={'id': True}
    )