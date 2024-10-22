# from fastapi import status
from pydantic import BaseModel, StringConstraints
from typing import Annotated, Literal
from enum import StrEnum

class Role(StrEnum):
    USER="USER"
    ADMIN="ADMIN"
    MAIN_ADMIN="MAIN_ADMIN"

class AccountSchema(BaseModel):
    id: int
    login: str
    name: str
    role: Role

PasswordStr = Annotated[str, StringConstraints(min_length=8,strip_whitespace=False,pattern=r'^(a-zA-Z0-9)+$')]

class AccountRegistrSchema(BaseModel):
    login: Annotated[str, StringConstraints(min_length=1,strip_whitespace=True)]
    password: PasswordStr
    name: Annotated[str,StringConstraints(strip_whitespace=False,min_length=1)]

class StatusResponse(BaseModel):
    status: Literal["ok"]
status = StatusResponse(status="ok")

