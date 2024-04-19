from db.connection import get_connection
from sqlalchemy.orm import sessionmaker


class DatabaseSession:
    # 静态对象
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            engine = get_connection()
            Session = sessionmaker(bind=engine)
            cls.session = Session()
        return cls._instance


def get_db_session():
    return DatabaseSession().session
