from fastapi import APIRouter,status
from src.schemas import AccountRegistrSchema, AccountSchema, Role, StatusResponse
status_router = APIRouter(prefix="/status")
account_router = APIRouter(prefix="/account",tags=["Аккаунт"])

@status_router.get("",summary="получить статус сервера",tags=["Статус"])
def get_status() -> StatusResponse:
    return StatusResponse(status="ok")

@account_router.post("/registr",summary="Регистрация аккаунта",status_code=status.HTTP_201_CREATED)
def register_account(body: AccountRegistrSchema) -> AccountSchema:
    return AccountSchema(
        id=1,
        login=body.login,
        name=body.name,
        role=Role.USER,
    )
@account_router.get("/my",summary="Получение информации об аккаунте")
def get_my_account() -> AccountSchema:
    return AccountSchema (
        id=1,
        login="user1",
        name="Вася Пупкин",
        role=Role.USER,
    )


