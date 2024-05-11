from protobs import game_protoc_pb2_grpc
from concurrent import futures
from dotenv import load_dotenv

from src.config.prisma_config import prisma
from src.controller.auth_controller import UserAuthController
from src.controller.game_user_controller import GameUserController
from src.controller.game_game_controller import GameGameController

import asyncio
import grpc
import os

load_dotenv()

SERVER_URI = os.getenv('SERVER_URI')
PORT = os.getenv('PORT')

async def serve():
    server = grpc.aio.server(futures.ThreadPoolExecutor(max_workers=100))
    game_protoc_pb2_grpc.add_UserAuthServicer_to_server(UserAuthController(), server)
    game_protoc_pb2_grpc.add_GameUserServicer_to_server(GameUserController(), server)
    game_protoc_pb2_grpc.add_GameGameServicer_to_server(GameGameController(), server)
    server.add_insecure_port(SERVER_URI)
    await server.start()
    await prisma.connect()
    print('Running in Port ' + PORT)
    await server.wait_for_termination()
    await prisma.disconnect()

if __name__ == '__main__':
    asyncio.run(serve())