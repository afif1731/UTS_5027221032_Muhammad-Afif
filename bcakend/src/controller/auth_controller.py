from protobs import game_protoc_pb2, game_protoc_pb2_grpc
from src.middleware.custom_error import CustomError
from src.middleware.custom_response import CustomResponse

import src.services.auth_service as AuthService

class UserAuthController(game_protoc_pb2_grpc.UserAuthServicer):
    async def Register(self, request, context):
        try:
            token = await AuthService.register(name=request.name, email=request.email, password=request.password)

            if isinstance(token, CustomError):
                raise token

            data = {'token': token}
            result = CustomResponse(201, 'login success', data)
            response = game_protoc_pb2.RegisterResponse()

            return result.Parse(response)
        except CustomError as err:
            response = game_protoc_pb2.RegisterResponse()
            return err.Parse(response)
    
    async def Login(self, request, context):
        try:
            token = await AuthService.login(email=request.email, password=request.password)

            if isinstance(token, CustomError):
                raise token
            
            data = {'token': token}
            result = CustomResponse(200, 'login success', data)
            response = game_protoc_pb2.Loginresponse()

            return result.Parse(response)
        except CustomError as err:
            response = game_protoc_pb2.Loginresponse()
            return err.Parse(response)

    
    async def Me(self, request, context):
        try:
            data = await AuthService.me(request.token)

            if isinstance(data, CustomError):
                raise data
            
            result = CustomResponse(200, 'get me', data)
            response = game_protoc_pb2.MeResponse()

            return result.Parse(response)
        except CustomError as err:
            response = game_protoc_pb2.MeResponse()
            return err.Parse(response)
    
    async def UpdatePassword(self, request, context):
        try:
            isUpdated = await AuthService.updateUserPassword(email=request.email, old_pass=request.old_pass, new_pass=request.new_pass)

            if isinstance(isUpdated, CustomError):
                raise isUpdated
            
            data = {'empty_data': ''}
            result = CustomResponse(200, 'password updated', data)
            response = game_protoc_pb2.UpdatePasswordResponse()
            return result.Parse(response)
        except CustomError as err:
            response = game_protoc_pb2.UpdatePasswordResponse()
            return err.Parse(response)
    
    async def DeleteUser(self, request, context):
        try:
            isDeleted = await AuthService.deleteAccount(request.user_id, request.token)

            if isinstance(isDeleted, CustomError):
                raise isDeleted
            
            data = {'empty_data': ''}
            result = CustomResponse(200, 'user deleted', data)
            response = game_protoc_pb2.DeleteUserResponse()
            return result.Parse(response)
        except CustomError as err:
            response = game_protoc_pb2.DeleteUserResponse()
            return err.Parse(response)
