from typing import Optional
from models.comments.comment import Comment
from db.db import SessionLocal
from repositories.comments.comment_repo_interface import CommentRepositoryInterface

db = SessionLocal()

class CommentRepository(CommentRepositoryInterface):
    async def get_comment_by_id(self, comment_id: int) -> Optional[Comment]:
        """
        Retrieve a comment by its ID.
        """
        query = "SELECT * FROM comments WHERE comment_id = :comment_id"
        return await db.fetch_one(query=query, values={"comment_id": comment_id})