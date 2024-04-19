from sqlalchemy import Column, Integer, String, Text, BigInteger, BLOB, DateTime
import sqlalchemy.sql.expression as Exp
from db.session import get_db_session
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class News(Base):
    __tablename__ = "news"

    id = Column(BigInteger, primary_key=True)
    source = Column(String(255), nullable=True)
    title = Column(String(255), nullable=True)
    content = Column(BLOB, nullable=True)
    create_time = Column(DateTime, nullable=False, default=Exp.text("CURRENT_TIMESTAMP"))

    def __init__(self, source, title, content):
        self.source = source.encode('utf-8')  # 显式指定编码
        self.title = title.encode('utf-8')
        self.content = content.encode('utf-8')

    def __repr__(self):
        return f"news(source={self.source}, title={self.title}, content={self.content})"


session = get_db_session()
# Create a new user
new_user = News(source="new york times", title="this is a title", content="this is content")
session.add(new_user)
session.commit()

# Read all users
# users = session.query(User).all()
# for user in users:
#     print(user)
#
# # Update a user's email
# user = session.query(User).filter_by(id=1).first()
# user.email = "newemail@example.com"
# session.commit()
#
# # Delete a user
# user = session.query(User).filter_by(id=2).first()
# session.delete(user)
# session.commit()
