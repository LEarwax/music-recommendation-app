from abc import ABC, abstractmethod
from typing import Optional
from models.comments import Comment

class CommentServiceInterface(ABC):
    @abstractmethod
    def get_comment(self, comment_id: int) -> Optional[Comment]:
        pass