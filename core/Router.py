from api.Base import ApiRouter
from views.Base import viewsRouter
from fastapi import APIRouter

# 路由聚合
AllRouter = APIRouter()

# 视觉路由
AllRouter.include_router(viewsRouter)

# api路由
AllRouter.include_router(ApiRouter)

