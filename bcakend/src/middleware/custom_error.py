from google.protobuf.json_format import ParseDict

class CustomError:
    def __init__(self, err_code, err_message):
        self.code = err_code
        self.message = str(err_message.args[0])

    def Parse(self, response):
        result = {
            'status': {
                'status': False,
                'code': self.code,
                'res_msg': self.message,
            },
            'data': {}
        }

        ParseDict(result, response)

        return response
