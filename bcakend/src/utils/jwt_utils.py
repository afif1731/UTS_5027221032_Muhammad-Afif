from src.config.jwt_config import JWT
import time
import jwt

def jwt_encode(payload):
    new_payload = {
        'exp': time.time() + (24 * 60 * 60),
        'data': payload
    }
    return jwt.encode(payload=new_payload, key=JWT['secret'], algorithm=JWT['method'])

def jwt_verify(token):
    return jwt.decode(jwt=token, key=JWT['secret'], algorithms=JWT['method'], options={'verify_exp': True}, verify=True)