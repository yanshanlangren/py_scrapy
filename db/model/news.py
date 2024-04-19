from sqlalchemy import Column, String, BigInteger, Text, DateTime
import sqlalchemy.sql.expression as Exp
from db.session import get_db_session
from sqlalchemy.orm import declarative_base
import json

Base = declarative_base()


class News(Base):
    __tablename__ = "news"

    id = Column(BigInteger, primary_key=True)
    source = Column(String(255), nullable=True)
    title = Column(String(255), nullable=True)
    content = Column(Text, nullable=True)
    create_time = Column(DateTime, nullable=False, default=Exp.text("CURRENT_TIMESTAMP"))
    additional_data = Column(String(255), nullable=True)
    authors = Column(String(255), nullable=True)
    images = Column(String(255), nullable=True)
    keywords = Column(String(255), nullable=True)
    meta_description = Column(String(255), nullable=True)
    tags = Column(String(255), nullable=True)
    canonical_link = Column(String(255), nullable=True)
    publish_date = Column(DateTime, nullable=True)

    def __init__(self, source, title, content, additional_data, authors, images, keywords, meta_description,
                 publish_date, tags, canonical_link):
        self.source = source.encode('utf-8')  # 显式指定编码
        self.title = title.encode('utf-8')
        self.content = content.encode('utf-8')

        self.additional_data = json.dumps(additional_data).encode('utf-8')
        self.authors = ','.join(authors).encode('utf-8')
        self.images = ','.join(images).encode('utf-8')
        self.keywords = ','.join(keywords).encode('utf-8')
        self.meta_description = meta_description.encode('utf-8'),
        self.publish_date = publish_date
        self.tags = ','.join(tags).encode('utf-8')
        self.canonical_link = canonical_link.encode('utf-8')

    def __repr__(self):
        return f"news(source={self.source}, title={self.title}, content={self.content})"


def insert(source, title, content, additional_data, authors, images, keywords, meta_description,
           publish_date, tags, canonical_link):
    session = get_db_session()
    new_user = News(source=source, title=title, content=content, additional_data=additional_data, authors=authors,
                    images=images, keywords=keywords, meta_description=meta_description,
                    publish_date=publish_date, tags=tags, canonical_link=canonical_link)
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
