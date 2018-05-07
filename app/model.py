# -*- coding = utf-8 -*-

from authlib.flask.oauth2.sqla import OAuth2ClientMixin, OAuth2TokenMixin
from sqlalchemy import Column, Integer, Sequence, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class User(Base):

    __tablename__ = "user"

    id = Column(Integer, Sequence("user_id_seq"), primary_key=True)

    username = Column(String, unique=True)
    password = Column(String)

    def get_user_id(self):
        return self.id


class Client(Base, OAuth2ClientMixin):

    __tablename__ = "client"

    id = Column(Integer, Sequence("client_id_seq"), primary_key=True)
    user_id = Column(
        Integer, ForeignKey('user.id', ondelete='CASCADE')
    )

    user = relationship('User')


class Token(Base, OAuth2TokenMixin):

    __tablename__ = "token"

    id = Column(Integer, Sequence("token_id_seq"), primary_key=True)
    user_id = Column(
        Integer, ForeignKey('user.id', ondelete='CASCADE')
    )

    user = relationship('User')

