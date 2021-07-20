import sqlalchemy as sa

from .db_session import SqlAlchemyBase


class User(SqlAlchemyBase):
    __tablename__ = 'couples'
    id = sa.Column(sa.Integer,
                   primary_key=True, autoincrement=True)
    first = sa.Column(sa.Integer, nullable=True)
    second = sa.Column(sa.Integer, nullable=True)
    third = sa.Column(sa.Integer, nullable=True)
    fourth = sa.Column(sa.Integer, nullable=True)
    fifth = sa.Column(sa.Integer, nullable=True)
    sixth = sa.Column(sa.Integer, nullable=True)
