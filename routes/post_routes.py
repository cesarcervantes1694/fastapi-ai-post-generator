from fastapi import APIRouter, HTTPException
from models.post_model import PostRequest
from business.post_service_blc import generate_post_stability, generate_post_replicate

router = APIRouter()

@router.get("/")
def generate():
    return {
        "message":"API ON!",
        "data":"new"
    }

@router.post("/generate-stability")
def generate_stability(req: PostRequest):
    try:
        return generate_post_stability(req)
    except Exception as ex:
        raise HTTPException(
            status_code=500,
            detail=str(ex)
        )
    

@router.post("/generate-replicate")
def generate_replicate(req: PostRequest):
    try:
        return generate_post_replicate(req)
    except Exception as ex:
        raise HTTPException(
            status_code=500,
            detail=str(ex)
        )
    