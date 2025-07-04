from fastapi import APIRouter, HTTPException, status, Depends

from sqlalchemy.ext.asyncio import AsyncSession

from web.schemas.user import User as User_scheme
from service.database.crud import UserAdapter as ua
from service.database import db_connector




router = APIRouter()


@router.get('/', response_model=list[User_scheme])
async def get_users(session: AsyncSession = Depends(db_connector.session_dependency)) -> list[User_scheme]:

    result = await ua.get_users(session)

    if not result:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='The database is empty')

    return result



@router.get('/{id}', response_model=User_scheme)
async def get_user_by_id(id: int, session: AsyncSession = Depends(db_connector.session_dependency)) -> User_scheme:

        result = await ua.get_user_by_id(session, id)

        if result is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='User with this id not found')

        return result



@router.post('/', response_model=dict)
async def add_user(user: User_scheme, session: AsyncSession = Depends(db_connector.session_dependency)) -> dict:

        result = await ua.add_user(session, user)

        if result:
            return {'status': 'ok', 'detail': 'User added'}

        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Error adding user')


@router.put('/{id}', response_model=dict)
async def update_user(id: int, user: User_scheme, session: AsyncSession = Depends(db_connector.session_dependency)) -> dict:

    result = await ua.update_user(session, id, user)

    if result:
        return {'status': 'ok', 'detail': 'User updated'}

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Error updating user')


@router.delete('/{id}', response_model=dict)
async def del_user_by_id(id: int, session: AsyncSession = Depends(db_connector.session_dependency)) -> dict:

    result = await ua.del_user(session, id)

    if result:
        return {'status': 'ok', 'detail': 'User deleted'}

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Error removing user')