from fastapi import APIRouter, Depends
from sqlmodel import Session
from src.controllers.event_controller import EventController
from src.database.connection import get_session
from src.dto.event_dto import EventCreate, EventUpdate

router = APIRouter(prefix="/events", tags=["Events"])


@router.get("/")
def get_events(db: Session = Depends(get_session)):
    return EventController().get_all(db)


@router.get("/{id}")
def get_event(id: int, db: Session = Depends(get_session)):
    return EventController().get_by_id(id, db)


@router.post("/")
def create_event(event: EventCreate, db: Session = Depends(get_session)):
    return EventController().create(event, db)


@router.put("/{id}")
def update_event(id: int, event: EventUpdate, db: Session = Depends(get_session)):
    return EventController().update(id, event, db)


@router.delete("/{id}")
def delete_event(id: int, db: Session = Depends(get_session)):
    return EventController().delete(id, db)