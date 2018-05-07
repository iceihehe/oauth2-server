# -*- coding = utf-8 -*-


class Config:

    PROJECT_NAME = "oauth2-server"

    # 数据库连接
    SQLALCHEMY_DATABASE_URI = "postgresql://postgres:postgres@10.0.2.127:5432/oauth"
    SQLALCHEMY_POOL_RECYCLE = 3600
    SQLALCHEMY_POOL_SIZE = 30
    SQLALCHEMY_MAX_OVERFLOW = 10
