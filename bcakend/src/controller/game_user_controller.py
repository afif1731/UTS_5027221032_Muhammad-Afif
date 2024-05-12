from protobs import game_protoc_pb2, game_protoc_pb2_grpc
from src.middleware.custom_error import CustomError
from src.middleware.custom_response import CustomResponse
from google.protobuf.json_format import ParseDict

import src.services.game_user_service as GameUserService
import math

class GameUserController(game_protoc_pb2_grpc.GameUserServicer):
    async def GetUserDetail(self, request, context):
        try:
            user_data = await GameUserService.getUserDetail(request.user_id)

            if isinstance(user_data, CustomError):
                raise user_data
            
            result = CustomResponse(200, 'get user detail', user_data)
            response = game_protoc_pb2.UserDetailResponse()
            return result.Parse(response)
        except CustomError as err:
            response = game_protoc_pb2.UserDetailResponse()
            return err.Parse(response)
    
    async def GetLeaderBoard(self, request, context):
        try:
            lb_data = await GameUserService.getLeaderBoard(request.sort, request.limit, request.page)

            result = {
                'status': {
                    'status': True,
                    'code': 200,
                    'res_msg': 'get leaderboard'
                },
                'metadata': {
                    'filter': 'NONE',
                    'sort': request.sort,
                    'limit': int(request.limit),
                    'page': int(request.page),
                    'max_page': math.ceil(lb_data[0] / int(request.limit))
                },
                'data': lb_data[1]
            }

            response = game_protoc_pb2.LeaderboardResponse()
            return ParseDict(result, response)
        except CustomError as err:
            return err
    
    def GetRecentGame(self, request, context):
        return super().GetRecentGame(request, context)
