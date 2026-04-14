from fastapi import APIRouter, Depends
from sqlmodel import Session
from src.controllers.registration_controller import RegistrationController
from src.database.connection import get_session
from src.dto.registration_dto import RegistrationCreate, RegistrationUpdate
from src.middleware.auth_middleware import get_current_account, require_role

router = APIRouter(prefix="/registrations", tags=["Registrations"])


# GET /registrations/ — hanya admin & superadmin
@router.get("/", dependencies=[Depends(require_role("admin", "superadmin"))])
def get_registrations(db: Session = Depends(get_session)):
    return RegistrationController(db).get_all()


# GET /registrations/{id} — hanya admin & superadmin
@router.get("/{id}", dependencies=[Depends(require_role("admin", "superadmin"))])
def get_registration(id: int, db: Session = Depends(get_session)):
    return RegistrationController(db).get_by_id(id)


# POST /registrations/ — user, admin, superadmin (semua yang login)
@router.post("/")
def create_registration(
    reg: RegistrationCreate,
    db: Session = Depends(get_session),
    current_user: dict = Depends(get_current_account),
):
    return RegistrationController(db).create(reg)


# PUT /registrations/{id} — hanya admin & superadmin
@router.put("/{id}", dependencies=[Depends(require_role("admin", "superadmin"))])
def update_registration(id: int, reg: RegistrationUpdate, db: Session = Depends(get_session)):
    return RegistrationController(db).update(id, reg)


# DELETE /registrations/{id} — hanya admin & superadmin
@router.delete("/{id}", dependencies=[Depends(require_role("admin", "superadmin"))])
def delete_registration(id: int, db: Session = Depends(get_session)):
    return RegistrationController(db).delete(id)