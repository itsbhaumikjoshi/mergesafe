from datetime import datetime, timedelta
from jose import jwt, JWTError


class JWTService:
    def __init__(self, secret: str, expiry_minutes: int = 60*24*30, algorithm: str = "HS256"):
        self.secret = secret
        self.algorithm = algorithm
        self.expiry_minutes = expiry_minutes

    def sign(self, payload: dict) -> str:
        data = payload.copy()
        expire = datetime.utcnow() + timedelta(minutes=self.expiry_minutes)

        data.update({
            "exp": expire,
            "iat": datetime.utcnow()
        })

        token = jwt.encode(data, self.secret, algorithm=self.algorithm)
        return token

    def verify(self, token: str) -> dict:
        try:
            payload = jwt.decode(token, self.secret, algorithms=[self.algorithm])
            return payload

        except JWTError as e:
            raise Exception(f"Invalid token: {str(e)}")