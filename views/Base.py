"""
@Time : 2022/4/23 11:46 AM
@Author: dd
@Des: 视图路由
"""

from fastapi import APIRouter, Request
from starlette.responses import HTMLResponse

from views.home import read_item

viewsRouter = APIRouter()


viewsRouter.get("/items/{id}", response_class=HTMLResponse)(read_item)

