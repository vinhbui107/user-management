from fastapi import APIRouter

router = APIRouter()


@router.get("/")
def heath_check():
    return {"message": "Ok"}
