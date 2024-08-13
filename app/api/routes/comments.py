from fastapi import APIRouter
from models.comments.comment import Comment
from services.comments.comment_service import comment_service

router = APIRouter()


@router.get("/comment/{comment_id}", response_model=Comment)
def get_comment(comment_id: int):
    return comment_service.get_comment(comment_id)
