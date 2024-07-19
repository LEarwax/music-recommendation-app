from fastapi import HTTPException
import comment_service_interface
from typing import Optional
from models.comments import Comment

class CommentService(comment_service_interface):
    def __init__(self, comment_repo):
        self.comment_repo = comment_repo

    def get_comment(self, comment_id: int) -> Optional[Comment]:
        comment = self.comment_repo.get_comment_by_id(comment_id)
        if not comment:
            raise HTTPException(status_code=404, detail="Comment not found")
        return comment