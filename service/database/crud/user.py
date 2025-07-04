from sqlalchemy import select
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.asyncio import AsyncSession
from service.database.models import User as User_model
from web.schemas import User as User_scheme



class UserAdapter:

    @classmethod
    async def get_users(cls, session: AsyncSession) -> list[User_model]:
        try:
            request = select(User_model).order_by(User_model.id)
            result = await session.execute(request)
            users = result.scalars().all()
            return list(users)

        except SQLAlchemyError as e:
            print('Ошибка при получении списка всех пользователей', e)
            return []


    @classmethod
    async def get_user_by_id(cls, session: AsyncSession, id: int) -> User_model | None:
        try:
            return await session.get(User_model, id)

        except SQLAlchemyError as e:
            print('Ошибка при получении пользователя по id', e)
            return None


    @classmethod
    async def add_user(cls, session: AsyncSession, user: User_scheme) -> bool:
        try:
            user_model = User_model(**user.model_dump())
            session.add(user_model)
            await session.commit()
            return True

        except SQLAlchemyError as e:
            print('Ошибка при добавлении пользователя', e)
            await session.rollback()
            return False


    @classmethod
    async def update_user(cls, session: AsyncSession, id: int, user: User_scheme) -> bool:
        try:
            model_user = session.get(User_model, id)
            if model_user is None:
                return False

            for key, value in user.model_dump().items():
                setattr(model_user, key, value)

            await session.commit()
            return True

        except SQLAlchemyError as e:
            print('Ошибка при обновлении пользователя', e)
            await session.rollback()
            return False


    @classmethod
    async def del_user(cls, session: AsyncSession, id: int) -> bool:
        try:
            user_model = await session.get(User_model, id)
            if user_model is None:
                return False

            await session.delete(user_model)
            await session.commit()
            return True

        except SQLAlchemyError as e:
            print('Ошибка при удалении пользователя', e)
            await session.rollback()
            return False
