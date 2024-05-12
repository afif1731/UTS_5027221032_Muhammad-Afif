import src.repositories.game_user_repository as GameUserRepo

from src.middleware.custom_error import CustomError

async def getUserDetail(user_id):
    try:
        user = await GameUserRepo.findUserById(user_id)

        if user is None:
            raise CustomError(400, 'user not found')
        
        return {
            'user_id': user.id,
            'user_name': user.account.name,
            'user_email': user.account.email,
            'elo': user.game_elo,
            'created_at': str(user.created_at)
        }
    except CustomError as err:
        return err
    
async def getLeaderBoard(sort, limit, page):
    try:
        query = {
            'sort': sort,
            'limit': limit,
            'page': page
        }

        users = await GameUserRepo.getTopElo(query)

        mapped_users = [
            {
                'user_id': user.id,
                'user_name': user.account.name,
                'user_email': user.account.email,
                'elo': user.game_elo,
                'created_at': str(user.created_at)
            } for user in users
        ]

        user_count = await GameUserRepo.countUser()

        return (user_count['id'], mapped_users)
    except CustomError as err:
        return err