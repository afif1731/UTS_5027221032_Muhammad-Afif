from protobs import game_protoc_pb2, game_protoc_pb2_grpc
from dotenv import load_dotenv
from typing import Iterable

import asyncio
import time
import grpc
import os

load_dotenv()

SERVER_URI = os.getenv('SERVER_URI')

def iterating(input_string: str) -> Iterable[str]:
    token = input_string.split()
    return token

async def main_run():
    async with grpc.aio.insecure_channel(SERVER_URI) as channel:
        authStub = game_protoc_pb2_grpc.UserAuthStub(channel)
        gameUserStub = game_protoc_pb2_grpc.GameUserStub(channel)
        gameGameStub = game_protoc_pb2_grpc.GameGameStub(channel)
        print('1. Register')
        print('2. Login')
        print('3. Get Me')
        print('4. Update Password')
        print('5. Delete user')
        print('6. Get user Detail')
        print('7. Get Leaderboard')
        print('8. Get Game Detail')
        print('9. Create new game')
        print('10. Update Move')
        print('11. Get Bot Move')
        print('12. End Game')
        print('13. ???')
        rpc_call = input('Your Choose : ')

        if rpc_call == '1':
            reg_name = input('Input Name: ')
            reg_email = input('Input Email: ')
            reg_pass = input('Input Pass: ')
            request = game_protoc_pb2.RegisterRequest(name=reg_name, email=reg_email, password=reg_pass)
            response = await authStub.Register(request)
            print(response)
        elif rpc_call == '2':
            reg_email = input('Input Email: ')
            reg_pass = input('Input Pass: ')
            request = game_protoc_pb2.LoginRequest(email=reg_email, password=reg_pass)
            response = await authStub.Login(request)
            print(response)
        elif rpc_call == '3':
            reg_token = input('Input Token: ')
            request = game_protoc_pb2.MeRequest(token=reg_token)
            response = await authStub.Me(request)
            print(response)
        elif rpc_call == '4':
            reg_email = input('Input Email: ')
            reg_oldpass = input('Input Old Pass: ')
            reg_newpass = input('Input New Pass: ')
            request = game_protoc_pb2.UpdatePasswordRequest(email=reg_email, old_pass=reg_oldpass, new_pass=reg_newpass)
            response = await authStub.UpdatePassword(request)
            print(response)
        elif rpc_call == '5':
            reg_id = input('Input Id: ')
            reg_token = input('Input Token: ')
            request = game_protoc_pb2.DeleteUserRequest(user_id=reg_id, token=reg_token)
            response = await authStub.DeleteUser(request)
            print(response)
        elif rpc_call == '6':
            reg_id = input('Input Id: ')
            request = game_protoc_pb2.UserDetailRequest(user_id=reg_id)
            response = await gameUserStub.GetUserDetail(request)
            print(response)
        elif rpc_call == '7':
            reg_filter = input('Input filter: ')
            reg_sort = input('Input Sort: ')
            reg_lim = input('Input Limit: ')
            reg_page = input('Input Page: ')
            request = game_protoc_pb2.LeaderboardRequest(filter=reg_filter, sort=reg_sort, limit=reg_lim, page=reg_page)
            response = await gameUserStub.GetLeaderBoard(request)
            print(response)
        elif rpc_call == '8':
            reg_game = input('Input game id: ')
            request = game_protoc_pb2.GameDetailRequest(game_id=reg_game)
            response = await gameGameStub.GetgameDetail(request)
            print(response)
        elif rpc_call == '9':
            reg_p1 = input('Input player 1: ')
            reg_p2 = input('Input player 2: ')
            reg_gtype = input('Input game type: ')
            request = game_protoc_pb2.CreateGameRequest(player_1=reg_p1, player_2=reg_p2, game_type=reg_gtype)
            response = await gameGameStub.CreateGame(request)
            print(response)
        elif rpc_call == '10':
            reg_gameid = input('Input Game Id: ')
            reg_ptype = input('Input P Type: ')
            reg_move = input('Input Move: ')
            reg_board = input('Input Board: ')
            request = game_protoc_pb2.UpdateMoveRequest(game_id=reg_gameid, player_type=int(reg_ptype), move=reg_move, board=iterating(reg_board))
            response = await gameGameStub.UpdateMove(request)
            print(response)            
        elif rpc_call == '11':
            reg_gameid = input('Input Game Id: ')
            reg_board = input('Input Board: ')
            request = game_protoc_pb2.BotMoveRequest(game_id=reg_gameid, board=iterating(reg_board))
            response = await gameGameStub.GetBotMove(request)
            print(response)
        elif rpc_call == '12':
            reg_gameid = input('Input Game Id: ')
            reg_win = input('Input Winner: ')
            request = game_protoc_pb2.EndGameRequest(game_id=reg_gameid, winner=reg_win)
            response = await gameGameStub.EndGame(request)
            print(response)
        elif rpc_call == '13':
            print('not implemented')
        else:
            print('Unknown choose')

if __name__ == '__main__':
    asyncio.run(main_run())