from fastapi import APIRouter
from models.comments.comment import Comment
from services.comments.comment_service import comment_service

router = APIRouter()

@router.get("/comment/{comment_id}", response_model=Comment)
async def get_comment(comment_id: int):
    comment = await comment_service.get_comment(comment_id)
    return comment

# add endpoint to create a comment
# research post method 
# figure out how to send a body with the POST request
# use chat gpt to help you write it in FastAPI

# @router.post("/comment/", response_model=Comment)
# async def create_comment(comment: Comment):
    
#     created_comment = await comment_service.create_comment(comment)
#     return created_comment
    
