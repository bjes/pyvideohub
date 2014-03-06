from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy import Column, Integer, SmallInteger, String, Text
from contextlib import contextmanager

ScopedSession = scoped_session(sessionmaker())
Base = declarative_base()

@contextmanager
def DBSession():
    try:
        yield ScopedSession()
    finally:
        ScopedSession.remove()

class Video(Base):
    __tablename__ = 'videos'

    id = Column(Integer, primary_key=True)
    title = Column(String(50), nullable=False)
    description = Column(Text, nullable=True)
    status = Column(SmallInteger, default=0, nullable=False)
