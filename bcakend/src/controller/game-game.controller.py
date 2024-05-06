from protobs import game_protoc_pb2, game_protoc_pb2_grpc
from concurrent import futures
import asyncio
import time

class GameGameServicer(game_protoc_pb2_grpc.GameGameServicer):
    def GetgameDetail(self, request, context):
        return super().GetgameDetail(request, context)
    
    def CreateGame(self, request, context):
        return super().CreateGame(request, context)
    
    def UpdateMove(self, request, context):
        return super().UpdateMove(request, context)
    
    def EndGame(self, request, context):
        return super().EndGame(request, context)
 