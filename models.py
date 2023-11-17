from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker, AsyncAttrs
from conf import DSN
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Column, Integer, String, Text

engine = create_async_engine(DSN)

Session = async_sessionmaker(bind=engine,
                             class_=AsyncSession,
                             expire_on_commit=False)


class Base(DeclarativeBase, AsyncAttrs):
    pass


# модель персонажей
class SwapiPeople(Base):
    __tablename__ = 'swapi_people'

    id = Column(Integer, primary_key=True, autoincrement=False)
    birth_year = Column(String)
    eye_color = Column(String)
    films = Column(Text)
    gender = Column(String)
    hair_color = Column(String)
    height = Column(String)
    homeworld = Column(String)
    mass = Column(String)
    name = Column(String)
    skin_color = Column(String)
    species = Column(Text)
    starships = Column(Text)
    vehicles = Column(Text)
