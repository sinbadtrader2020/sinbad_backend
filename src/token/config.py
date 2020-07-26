
###################################
# Supported Algorithms
# https://www.jsonwebtoken.io/
###################################


class Algorithm:
    HMAC_SHA_256            = 'HMACSHA256'
    HMAC_SHA_384            = 'HMACSHA384'
    HMAC_SHA_512            = 'HMACSHA512'
    RSASSA_SHA_256          = 'RSASSASHA256'
    RSASSA_SHA_384          = 'RSASSASHA384'
    RSASSA_SHA_512          = 'RSASSASHA512'
    ECDSA_P256_N_SHA_256    = 'ECDSASHA256'
    ECDSA_P384_N_SHA_384    = 'ECDSASHA384'
    ECDSA_P512_N_SHA_512    = 'ECDSASHA512'


AlgorithmList = {
    Algorithm.HMAC_SHA_256          : 'HS256',
    Algorithm.HMAC_SHA_384          : 'HS384',
    Algorithm.HMAC_SHA_512          : 'HS512',
    Algorithm.RSASSA_SHA_256        : 'RS256',
    Algorithm.RSASSA_SHA_384        : 'RS384',
    Algorithm.RSASSA_SHA_512        : 'RS512',
    Algorithm.ECDSA_P256_N_SHA_256  : 'ES256',
    Algorithm.ECDSA_P384_N_SHA_384  : 'ES384',
    Algorithm.ECDSA_P512_N_SHA_512  : 'ES512'
}


class Type:
    JWT         = 'JWT'


class Header:
    TYPE        = 'typ'
    ALGORITHM   = 'alg'
    KID         = 'kid'


class Payload:
    ISSUER          = 'iss'
    EXPIRATION      = 'exp'
    SUBJECT         = 'sub'
    AUDIENCE        = 'aud'
    CONTEXT         = 'context'
    ROOM            = 'room'


# {
#   "context": {
#     "user": {
#       "avatar": "https:/gravatar.com/avatar/abc123",
#       "name": "John Doe",
#       "email": "jdoe@example.com",
#       "id": "abcd:a1b2c3-d4e5f6-0abc1-23de-abcdef01fedcba"
#     },
#     "group": "a123-123-456-789"
#   },
#   "aud": "jitsi",
#   "iss": "my_client",
#   "sub": "meet.jit.si",
#   "room": "*",
#   "exp": 1500006923
# }