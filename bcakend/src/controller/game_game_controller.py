from protobs import game_protoc_pb2, game_protoc_pb2_grpc
from src.middleware.custom_response import CustomResponse
from src.middleware.custom_error import CustomError

import src.services.game_game_service as GameGameService

class GameGameController(game_protoc_pb2_grpc.GameGameServicer):
    async def GetgameDetail(self, request, context):
        try:
            detail = await GameGameService.getGameDetail(request.game_id)

            if isinstance(detail, CustomError):
                raise detail
            
            result = CustomResponse(200, 'get game detail', detail)
            response = game_protoc_pb2.GameDetailResponse()

            return result.Parse(response)
        except CustomError as err:
            response = game_protoc_pb2.GameDetailResponse()
            return err.Parse(response)
    
    async def CreateGame(self, request, context):
        try:
            data = await GameGameService.createGame(request.player_1, request.player_2, request.game_type)

            if isinstance(data, CustomError):
                raise data
            
            result = CustomResponse(201, 'game created', data)
            response = game_protoc_pb2.CreateGameResponse()

            return result.Parse(response)
        except CustomError as err:
            response = game_protoc_pb2.CreateGameResponse()
            return err.Parse(response)
    
    async def UpdateMove(self, request, context):
        try:
            new_detail = await GameGameService.updateMove(request.game_id, request.player_type, request.move, request.board)

            if isinstance(new_detail, CustomError):
                raise new_detail
            
            result = CustomResponse(200, 'move updated', new_detail)
            response = game_protoc_pb2.UpdateMoveResponse()

            return result.Parse(response)
        except CustomError as err:
            response = game_protoc_pb2.UpdateMoveResponse()
            return err.Parse(response)
    
    async def EndGame(self, request, context):
        try:
            end_detail = await GameGameService.endGame(request.game_id, request.winner)

            if isinstance(end_detail, CustomError):
                raise end_detail
            
            result = CustomResponse(200, 'game finished', end_detail)
            response = game_protoc_pb2.EndGameResponse()

            return result.Parse(response)
        except CustomError as err:
            response = game_protoc_pb2.EndGameResponse()
            return err.Parse(response)
    
    async def GetBotMove(self, request, context):
        try:
            new_detail = await GameGameService.updateBotMove(request.game_id, request.board)

            if isinstance(new_detail, CustomError):
                raise new_detail
            
            result = CustomResponse(200, 'bot move updated', new_detail)
            response = game_protoc_pb2.BotMoveResponse()

            return result.Parse(response)
        except CustomError as err:
            response = game_protoc_pb2.BotMoveResponse()
            return err.Parse(response)
