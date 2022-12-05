"""
@Time : 2022/4/23 11:46 AM
@Author: dd
@Des: views home
"""

from fastapi import Request, Form


async def home(request: Request, id: str):
    return request.app.state.views.TemplateResponse("index.html", {"request": request, "id": id})


async def read_item(request: Request, id: str):
    return request.app.state.views.TemplateResponse("index.html", {"request": request, "id": id})


async def reg_page(request: Request, username: str = Form(...), password: str = Form(...)):
    return request.app.state.views.TemplateResponse("index.html", {"request": request, "id": id})