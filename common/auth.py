#!/root/.pyenv/shims/python
# -*- coding:utf-8 -*-

# serializer for JWT
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
# exceptions for JWT
from itsdangerous import SignatureExpired, BadSignature, BadData
import time
import logging
from logging.handlers import TimedRotatingFileHandler

"""
token is generated as the JWT protocol.
JSON Web Tokens(JWT) are an open, industry standard RFC 7519 method
"""

###### configure logging #####
logFilePath = "../log/auth/auth.log"
logger = logging.getLogger("Auth")
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s \
%(filename)s[line:%(lineno)d] %(levelname)s %(message)s',)
handler = TimedRotatingFileHandler(logFilePath,when="D",interval=1,backupCount=30)
handler.suffix = "%Y%m%d"
handler.setFormatter(formatter)
logger.addHandler(handler)

class auth:
    def __init__(self,user_id,role_id):
        self.user_id = user_id
        self.role_id = role_id
        self.secret_key = "yo"
        self.salt = "yoyo"

    def genTokenSeq(self,expires):
        s = Serializer(
            secret_key=self.secret_key,
            salt=self.salt,
            expires_in=expires)
        print("first Serializer: ", s)
        timestamp = time.time()
        return s.dumps(
            {'user_id': self.user_id,
                'user_role': self.role_id,
                'iat': timestamp})
        # The token contains userid, user role and the token generation time.
        # u can add sth more inside, if needed.
        # 'iat' means 'issued at'. claimed in JWT.

    def parsetoken(self,token):
        #token decoding
        s = Serializer(
            secret_key=self.secret_key,
            salt=self.salt
        )
        try:
            data = s.loads(token)
        # 过期token
        except SignatureExpired:
            msg = "token expired"
            logger.warning(msg)
            return [None,None,msg]
        except BadSignature as e:
            encoded_payload = e.encoded_payload
            if encoded_payload is not None:
                try:
                    s.load_payload(encoded_payload)
                except BadData:
                    # the token is tampered,token 被篡改
                    msg = "token tampered"
                    logger.warning(msg)
                    return [None,None,msg]
                msg = 'badSignature of token,token 损坏'
                logger.warning(msg)
                return [None,None,msg]
        except:
            msg = 'wrong token with unkown reason'
            logger.warning(msg)
            return [None,None,msg]
        if ('user_id' not in data) or ('user_role' not in data ):
            msg = "illegal payload inside"
            logger.warning(msg)
            return [None,None,msg]
        # msg = 'user(' + data["user_id"] + ') logged in token'
        msg = "user_id( " +str(data["user_id"]) + " )logged in token"
        userId = data['user_id']
        roleId = data['user_role']
        print ([userId,roleId,msg])

if __name__ == "__main__":
    a = auth(1,2)
    b = a.genTokenSeq(11)
    print(b,type(b))
    a.parsetoken(b)