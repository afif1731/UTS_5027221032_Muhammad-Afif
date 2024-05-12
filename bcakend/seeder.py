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
                where={'email': user['email']},
                data={
                    'create': {
                        'id': user['account_id'],
                        'email': user['email'],
                        'name': user['name'],
                        'password': user_pass.decode('utf-8'),
                        'role': user['role'],
                        'GameUser': {
                            'create': {
                                'id': user['user_id'],
                                'game_elo': int(user['game_elo'])
                            }
                        }
                    },
                    'update': {
                        'id': user['account_id'],
                        'email': user['email'],
                        'name': user['name'],
                        'password': user_pass.decode('utf-8'),
                        'role': user['role'],
                        'GameUser': {
                            'create': {
                                'id': user['user_id'],
                                'game_elo': int(user['game_elo'])
                            }
                        }
                    }
                }
            )

async def main():
    await prisma.connect()
    await users()
    await prisma.disconnect()

if __name__ == '__main__':
    asyncio.run(main())