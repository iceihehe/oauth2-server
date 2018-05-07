# -*- coding = utf-8 -*-

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session

from app import Config

engine = create_engine(
    Config.SQLALCHEMY_DATABASE_URI,
    max_overflow=Config.SQLALCHEMY_MAX_OVERFLOW,
    pool_recycle=Config.SQLALCHEMY_POOL_RECYCLE,
    pool_size=Config.SQLALCHEMY_POOL_SIZE,
    echo=True
)

Session = sessionmaker(bind=engine)
session = scoped_session(Session)
