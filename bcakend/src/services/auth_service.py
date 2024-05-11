import src.repositories.auth_repository as AuthRepository
from src.utils import hasing, jwt_utils

async def register(name, email, password):
    try:
        user = await AuthRepository.findAccountByEmail(email)

        if user is not None :
            raise Exception('email is already exist')
        
        hashedpass = await hasing.hash_pass(password)

        account = await AuthRepository.registerAccount(name, email, hashed_pass=hashedpass.decode('utf-8'))
        gameUser = await AuthRepository.createGameAccount(account_id=account.id, elo=100)

        payload = {
            'account_id': account.id,
            'user_id': gameUser.id,
            'email': account.email,
            'role': account.role
        }

        token = jwt_utils.jwt_encode(payload)

        return token
    except Exception as err:
        return err

async def login(email, password):
    try:
        user = await AuthRepository.findUserByEmail(email)

        if user is None:
            raise Exception('email not found')

        isPasswTrue = await hasing.compare(password, user.account.password)

        if not isPasswTrue:
            raise Exception('invalid credential')
        
        payload = {
            'account_id': user.account_id,
            'user_id': user.id,
            'email': user.account.email,
            'role': user.account.role
        }

        token = jwt_utils.jwt_encode(payload)

        return token
    except Exception as err:
        return err

async def me(token):
    try:
        data_decode = jwt_utils.jwt_verify(token)

        if data_decode is None:
            raise Exception('invalid token')
        
        user = await AuthRepository.findAccountByEmail(data_decode['data']['email'])

        if not user:
            raise Exception('user not found')
        
        return {
            'account_id': user.id,
            'user_id': data_decode['data']['user_id'],
            'name': user.name
        }
    except Exception as err:
        return err
        
async def updateUserPassword(email, old_pass, new_pass):
    try:
        user = await AuthRepository.findAccountByEmail(email)

        if user is None:
            raise Exception('email not found')
        
        isPasswTrue = await hasing.compare(old_pass, user.password)

        if not isPasswTrue:
            raise Exception('invalid credential')
        
        hashedpass = await hasing.hash_pass(new_pass)

        new_user = await AuthRepository.updateUserPassword(user.id, hashedpass.decode('utf-8'))

        if new_user is None:
            raise Exception('failed to update data')
        return True
    except Exception as err:
        return err

async def deleteAccount(account_id, token):
    try:
        user = await AuthRepository.findAccountById(account_id)

        if user is None:
            raise Exception('user not found')
        
        data_decode = jwt_utils.jwt_verify(token)

        if user.id != data_decode['data']['account_id']:
            raise Exception('you dont have permission to do this')
        
        isDeleted = await AuthRepository.deletegameUser(data_decode['data']['user_id'])
        isDeleted = await AuthRepository.deleteAccount(user.id)

        if isDeleted is None:
            raise Exception('failed to delete account')
        
        return True
    except Exception as err:
        return err
