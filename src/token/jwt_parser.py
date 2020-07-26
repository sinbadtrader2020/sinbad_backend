import jwt

from src.token.config import Algorithm, AlgorithmList, Header, Type


def get_token(payload, secret, applicable_algo= None, header=None):
    response = None
    algorithm = None

    if None == applicable_algo:
        algorithm = AlgorithmList.get(Algorithm.HMAC_SHA_256)
    else:
        algorithm = AlgorithmList.get(applicable_algo)
        if algorithm == None:
            return response

    if None == header or not any(header):
        header = {
            Header.ALGORITHM: algorithm,
            Header.TYPE: Type.JWT,
        }

    if header.get(Header.ALGORITHM) != algorithm:
        print('return match algo')
        return response

    if header.get(Header.TYPE) != Type.JWT:
        return response

    try:
        response = jwt.encode(payload=payload, key=secret, algorithm=algorithm, headers=header)
    except jwt.InvalidTokenError:
        pass  # do something sensible here, e.g. return HTTP 403 status code

    return response


def parse_token(token, secret, audience=None, applicable_algo=None):
    response = None
    algorithm=None

    if None == applicable_algo:
        algorithm = AlgorithmList.get(Algorithm.HMAC_SHA_256)
    else:
        algorithm = AlgorithmList.get(applicable_algo)
        if algorithm == None:
            return response

    try:
        response = jwt.decode(token, key=secret, audience=audience, algorithms=[algorithm])
    except jwt.InvalidTokenError as err:
        print(format(err))
        pass

    return response

