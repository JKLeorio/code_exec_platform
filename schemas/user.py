from fastapi_users import schemas


class UserBase(schemas.BaseUser[int]):
    pass



class UserCreate(schemas.BaseUserCreate):
    pass



class UserUpdate(schemas.BaseUserUpdate):
    pass

