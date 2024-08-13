from abc import ABC, abstractmethod
from typing import Optional
from models.comments.comment import Comment

class CommentRepositoryInterface(ABC):
    @abstractmethod
    async def get_comment_by_id(self, comment_id: int) -> Optional[Comment]:
        """
        Retrieve a comment by its ID.
        """
        pass