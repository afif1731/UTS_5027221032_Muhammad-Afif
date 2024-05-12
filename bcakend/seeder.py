from src.config.prisma_config import prisma
from src.utils.hasing import hash_pass
import asyncio
import csv

async def users():
    with open('./prisma/seed_data/users.csv', mode='r') as infile:
        reader = csv.DictReader(infile)
        mydict = [row for row in reader]
        for user in mydict:
            user_pass = await hash_pass(user['password'])

            await prisma.accounts.upsert(
                where={'id': user['account_id']},
                data={
                    'create': {
                        'id': user['account_id'],
                        'email': user['email'],
                        'name': user['name'],
                        'password': user_pass.decode('utf-8'),
                        'role': user['role'],
                    },
                    'update': {
                        'email': user['email'],
                        'name': user['name'],
                        'password': user_pass.decode('utf-8'),
                        'role': user['role'],
                    }
                }
            )

            await prisma.gameuser.upsert(
                where={'id': user['user_id']},
                data={
                    'create':{
                        'id': user['user_id'],
                        'account_id': user['account_id'],
                        'game_elo': int(user['game_elo'])
                    },
                    'update':{
                        'account_id': user['account_id'],
                        'game_elo': int(user['game_elo'])
                    }
                }
            )

async def gamelog():
    with open('./prisma/seed_data/gamelog.csv', mode='r') as infile:
        reader = csv.DictReader(infile)
        mydict = [row for row in reader]

        for glog in mydict:
            board = glog['board'].split()
            p1_move = glog['p1_move'].split()
            p2_move = glog['p2_move'].split()

            await prisma.gamedetail.upsert(
                where={'id': glog['detail_id']},
                data={
                    'create': {
                        'id': glog['detail_id'],
                        'board': board,
                        'p1_move': p1_move,
                        'p2_move': p2_move,
                        'move_count': int(glog['move_count'])
                    },
                    'update': {
                        'board': board,
                        'p1_move': p1_move,
                        'p2_move': p2_move,
                        'move_count': int(glog['move_count'])
                    }
                }
            )

            await prisma.gamelog.upsert(
                where={'id': glog['id']},
                data={
                    'create': {
                        'id': glog['id'],
                        'player_1': glog['player_1'],
                        'player_2': glog['player_2'],
                        'game_type': glog['game_type'],
                        'winner': glog['winner'],
                        'duration': int(glog['duration']),
                        'detail': glog['detail_id']
                    },
                    'update': {
                        'player_1': glog['player_1'],
                        'player_2': glog['player_2'],
                        'game_type': glog['game_type'],
                        'winner': glog['winner'],
                        'duration': int(glog['duration']),
                        'detail': glog['detail_id'],
                    }
                }
            )

async def main():
    await prisma.connect()
    await users()
    await gamelog()
    await prisma.disconnect()

if __name__ == '__main__':
    asyncio.run(main())