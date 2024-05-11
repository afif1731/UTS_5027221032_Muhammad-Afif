from google.protobuf.json_format import ParseDict

class CustomResponse:
    def __init__(self, code, message, data):
        self.code = code
        self.message = message
        self.data = data
    
    def Parse(self, response):
        result = {
            'status': {
                'status': True,
                'code': self.code,
                'res_msg': self.message
            },
            'data': self.data
        }

        ParseDict(result, response)

        return response