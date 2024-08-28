from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import sessionmaker
from models.comments.commentORM import CommentORM
from repositories.comments.comment_repo_interface import CommentRepositoryInterface
from models.comments.comment import Comment
from typing import Optional

class CommentRepository(CommentRepositoryInterface):
    def __init__(self, db_session: sessionmaker):
        self.db_session = db_session

    async def get_comment_by_id(self, comment_id: int) -> Optional[Comment]:
        async with self.db_session() as session:
            result = await session.execute(select(CommentORM).filter(CommentORM.comment_id == comment_id))
            comment_orm = result.scalars().first()
            if comment_orm:
                return Comment.from_orm(comment_orm)
            return None
    
