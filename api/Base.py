from fastapi import APIRouter, Request

from api.Login import login, index

#
ApiRouter = APIRouter(prefix='/v1', tags=["api路由"])


# router = ApiRouter()

@ApiRouter.get('/')
async def home(req: Request):
    return "fastApi"

ApiRouter.get("/index", tags=["api路由"], summary="register接口")(index)
ApiRouter.post("/login", tags=["api路由"], summary="login接口")(login)
