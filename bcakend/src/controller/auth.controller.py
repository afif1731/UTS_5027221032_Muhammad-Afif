from protobs import game_protoc_pb2, game_protoc_pb2_grpc
from concurrent import futures
import asyncio
import time

class UserAuthServicer(game_protoc_pb2_grpc.UserAuthServicer):
    def Register(self, request, context):
        return super().Register(request, context)
    
    def Login(self, request, context):
        return super().Login(request, context)
    
    def Me(self, request, context):
        return super().Me(request, context)
    
    def UpdatePassword(self, request, context):
        return super().UpdatePassword(request, context)
    
    def DeleteUser(self, request, context):
        return super().DeleteUser(request, context)
 