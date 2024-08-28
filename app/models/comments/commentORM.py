from sqlalchemy import Column, Integer, String, Text, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class CommentORM(Base):
    __tablename__ = 'comment'
    comment_id = Column(Integer, primary_key=True, index=True)
    account_id = Column(Integer, index=True)
    comment_content = Column(String, nullable=False)
    like_count = Column(Integer, default=0)
    dislike_count = Column(Integer, default=0)
    created_on = Column(DateTime, nullable=False)
    updated_on = Column(DateTime, nullable=False)