from fastapi import APIRouter, Depends
from sqlmodel import Session
from src.controllers.registration_controller import RegistrationController
from src.database.connection import get_session
from src.dto.registration_dto import RegistrationCreate, RegistrationUpdate

router = APIRouter(prefix="/registrations", tags=["Registrations"])

@router.get("/")
def get_registrations(db: Session = Depends(get_session)):
    return RegistrationController(db).get_all()

@router.get("/{id}")
def get_registration(id: int, db: Session = Depends(get_session)):
    return RegistrationController(db).get_by_id(id)

@router.post("/")
def create_registration(reg: RegistrationCreate, db: Session = Depends(get_session)):
    return RegistrationController(db).create(reg)

@router.put("/{id}")
def update_registration(id: int, reg: RegistrationUpdate, db: Session = Depends(get_session)):
    return RegistrationController(db).update(id, reg)

@router.delete("/{id}")
def delete_registration(id: int, db: Session = Depends(get_session)):
    return RegistrationController(db).delete(id)