from sqlalchemy.orm import Session
from app.models.request import Request
from app.schemas.request import RequestCreate, RequestUpdate

def create_request(db: Session, request: RequestCreate) -> Request:
    db_request = Request(**request.model_dump())
    db.add(db_request)
    db.commit()
    db.refresh(db_request)
    return db_request

def get_request(db: Session, req_id: int) -> Request:
    return db.query(Request).filter(Request.req_id == req_id).first()

def get_requests(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Request).offset(skip).limit(limit).all()

def update_request(db: Session, req_id: int, request: RequestUpdate) -> Request:
    db_request = db.query(Request).filter(Request.req_id == req_id).first()
    if db_request:
        for key, value in request.model_dump(exclude_unset=True).items():
            setattr(db_request, key, value)
        db.commit()
        db.refresh(db_request)
    return db_request

def delete_request(db: Session, req_id: int):
    db_request = db.query(Request).filter(Request.req_id == req_id).first()
    if db_request:
        db.delete(db_request)
        db.commit()
    return db_request
