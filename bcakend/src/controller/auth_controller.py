from protobs import game_protoc_pb2, game_protoc_pb2_grpc
from src.middleware.custom_error import CustomError
from src.middleware.custom_response import CustomResponse
import src.services.auth_service as AuthService

class UserAuthController(game_protoc_pb2_grpc.UserAuthServicer):
    async def Register(self, request, context):
        try:
            token = await AuthService.register(name=request.name, email=request.email, password=request.password)

            if isinstance(token, Exception):
                raise token

            data = {'token': token}
            result = CustomResponse(201, 'login success', data)
            response = game_protoc_pb2.RegisterResponse()

            return result.Parse(response)
        except Exception as err:
            error = CustomError(403, err)
            response = game_protoc_pb2.RegisterResponse()
            return error.Parse(response)
    
    async def Login(self, request, context):
        try:
            token = await AuthService.login(email=request.email, password=request.password)

            if isinstance(token, Exception):
                raise token
            
            data = {'token': token}
            result = CustomResponse(200, 'login success', data)
            response = game_protoc_pb2.Loginresponse()

            return result.Parse(response)
        except Exception as err:
            error = CustomError(403, err)
            response = game_protoc_pb2.Loginresponse()
            return error.Parse(response)

    
    async def Me(self, request, context):
        try:
            data = await AuthService.me(request.token)

            if isinstance(data, Exception):
                raise data
            
            result = CustomResponse(200, 'get me', data)
            response = game_protoc_pb2.MeResponse()

            return result.Parse(response)
        except Exception as err:
            error = CustomError(403, err)
            response = game_protoc_pb2.MeResponse()
            return error.Parse(response)
    
    async def UpdatePassword(self, request, context):
        try:
            isUpdated = await AuthService.updateUserPassword(email=request.email, old_pass=request.old_pass, new_pass=request.new_pass)

            if isinstance(isUpdated, Exception):
                raise isUpdated
            
            data = {'empty_data': ''}
            result = CustomResponse(200, 'password updated', data)
            response = game_protoc_pb2.UpdatePasswordResponse()
            return result.Parse(response)
        except Exception as err:
            error = CustomError(403, err)
            response = game_protoc_pb2.UpdatePasswordResponse()
            return error.Parse(response)
    
    async def DeleteUser(self, request, context):
        try:
            isDeleted = await AuthService.deleteAccount(request.user_id, request.token)

            if isinstance(isDeleted, Exception):
                raise isDeleted
            
            data = {'empty_data': ''}
            result = CustomResponse(200, 'user deleted', data)
            response = game_protoc_pb2.DeleteUserResponse()
            return result.Parse(response)
        except Exception as err:
            error = CustomError(403, err)
            response = game_protoc_pb2.DeleteUserResponse()
            return error.Parse(response)
