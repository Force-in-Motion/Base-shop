from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, declared_attr



class Base(DeclarativeBase):
    __abstract__ = True

    @classmethod
    @declared_attr.directive
    def __tablename__(cls) -> str:
        return cls.__name__.title()

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)

