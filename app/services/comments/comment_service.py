from fastapi import HTTPException
from .comment_service_interface import CommentServiceInterface
from typing import Optional
from repositories.comments.comment_repo import CommentRepository

from datetime import date

from models.comments.comment import Comment

class CommentService(CommentServiceInterface):
    def __init__(self, comment_repo):
        self.comment_repo = comment_repo

    def get_comment(self, comment_id: int) -> Optional[Comment]:
        # comment = self.comment_repo.get_comment_by_id(comment_id)
        comment = Comment(comment_id=1, account_id=1, comment_content="Hello, here is a comment", like_count=2, dislike_count=4, created_on=date(2024, 8, 12), updated_on=date(2024, 8, 12))
        if not comment:
            raise HTTPException(status_code=404, detail="Comment not found")
        return comment

comment_repo = CommentRepository()
comment_service = CommentService(comment_repo)