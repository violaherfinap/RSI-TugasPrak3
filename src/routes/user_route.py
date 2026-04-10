from fastapi import APIRouter, Depends
from sqlmodel import Session
from src.controllers.user_controller import UserController
from src.dto.user_dto import UserCreate, UserUpdate
from src.database.connection import get_session

router = APIRouter(prefix="/users", tags=["Users"])
controller = UserController()


@router.get("/")
def get_users(session: Session = Depends(get_session)):
    return controller.get_all(session)


@router.get("/{user_id}")
def get_user(user_id: int, session: Session = Depends(get_session)):
    return controller.get_by_id(user_id, session)


@router.post("/")
def create_user(user: UserCreate, session: Session = Depends(get_session)):
    try:
        print("🔥 MASUK:", user.dict())
        return controller.create(user, session)
    except Exception as e:
        import traceback
        traceback.print_exc()   # 🔥 ini yang penting
        return {"error": str(e)}


@router.put("/{user_id}")
def update_user(user_id: int, user: UserUpdate, session: Session = Depends(get_session)):
    return controller.update(user_id, user, session)


@router.delete("/{user_id}")
def delete_user(user_id: int, session: Session = Depends(get_session)):
    return controller.delete(user_id, session)