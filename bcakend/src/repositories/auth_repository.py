from src.config.prisma_config import prisma

async def findAccountByEmail(email):
    return await prisma.accounts.find_first(
        where= {
            'email': {
                'contains': email
            }
        }
    )

async def findAccountById(acc_id):
    return await prisma.accounts.find_first(
        where={
            'id': acc_id
        }
    )

async def registerAccount(name, email, hashed_pass):
    return await prisma.accounts.create({
        'name': name,
        'email': email,
        'password': hashed_pass
    })

async def createGameAccount(account_id, elo):
    return await prisma.gameuser.create({
        'account_id': account_id,
        'game_elo': elo
    })

async def findUserByEmail(email):
    return await prisma.gameuser.find_first(
        where= {
            'account': {
                'is': {
                    'email': email
                }
            }
        },
        include={
            'account': True
        }
    )

async def updateUserPassword(account_id, new_pass):
    return await prisma.accounts.update(
        where={
            'id': account_id
        },
        data={
            'password': new_pass
        }
    )

async def deleteAccount(account_id):
    return await prisma.accounts.delete(
        where={'id': account_id}
    )

async def deletegameUser(user_id):
    return await prisma.gameuser.delete(
        where={'id': user_id}
    )