import uvicorn

from fastapi import FastAPI

from auth import routers

app = FastAPI()

app.include_router(
    routers.login_router,
    prefix="/auth/jwt",
    tags=["auth"]
)
app.include_router(
    routers.register_router,
    prefix="/auth",
    tags=["auth"]
)
app.include_router(
    routers.password_reset_router,
    prefix="/auth",
    tags=["auth"]
)



if __name__ == "__main__":
    uvicorn.run(
        app=app,
        host='127.0.0.1',
        port=8000,
    )
