from jwt import encode, decode


def create_token(data) -> str:
    token: str = encode(payload=data, key="my_pwd", algorithm="HS256")

    return token


def validate_token(token: str) -> dict:
    token_decode: dict = decode(token, key="my_pwd", algorithms=["HS256"])

    return token_decode
