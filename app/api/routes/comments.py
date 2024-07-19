from fastapi import APIRouter
from models.comments import Comment
from services.comments import CommentService

router = APIRouter()
comment_service = CommentService()

@router.get("/comment/{comment_id}", response_model=[Comment])
def get_comment(comment_id: int):
    return comment_service.get_comment(comment_id)