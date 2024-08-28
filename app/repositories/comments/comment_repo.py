from typing import Optional
from models.comments.comment import Comment
from db.db import SessionLocal
from repositories.comments.comment_repo_interface import CommentRepositoryInterface
from models.comments.commentORM import CommentORM

from sqlalchemy.future import select
from sqlalchemy import select, Table

db = SessionLocal()

class CommentRepository(CommentRepositoryInterface):
    async def get_comment_by_id(self, comment_id: int) -> Optional[Comment]:
        """
        Retrieve a comment by its ID.
        """
        query = select(CommentORM).where(CommentORM.comment_id == comment_id)
        result = db.execute(query)
        return result.scalar_one_or_none()