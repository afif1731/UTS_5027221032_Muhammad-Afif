from protobs import game_protoc_pb2, game_protoc_pb2_grpc
from concurrent import futures
import asyncio
import time

class GameUserServicer(game_protoc_pb2_grpc.GameUserServicer):
    def GetUserDetail(self, request, context):
        return super().GetUserDetail(request, context)
    
    def GetLeaderBoard(self, request, context):
        return super().GetLeaderBoard(request, context)
    
    def GetRecentGame(self, request, context):
        return super().GetRecentGame(request, context)
