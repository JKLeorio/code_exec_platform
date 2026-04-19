from fastapi_users.authentication import (
    AuthenticationBackend, 
    BearerTransport,
    JWTStrategy
    )

from decouple import config

SECRET = config(
    "SECRET",
    default = "TEST SECRET"
    )

bearer_transport = BearerTransport(
    "auth/jwt/login"
)

def get_jwt_stategy() -> JWTStrategy:
    return JWTStrategy(secret=SECRET, lifetime_seconds=3600)

auth_backend = AuthenticationBackend(
    name="jwt",
    transport=bearer_transport,
    get_strategy=get_jwt_stategy
)