from typing import Optional
from models.comments import Comment
from db.db import SessionLocal
from repositories.comments import CommentRepositoryInterface

db = SessionLocal()

class CommentRepository(CommentRepositoryInterface):
    async def get_comment_by_id(self, comment_id: int) -> Optional[Comment]:
        """
        Retrieve a comment by its ID.
        """
        query = "SELECT * FROM comments WHERE comment_id = :comment_id"
        return await db.fetch_one(query=query, values={"comment_id": comment_id})