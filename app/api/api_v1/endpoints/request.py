from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.schemas.request import RequestCreate, RequestRead, RequestUpdate
from app.crud.request import get_request, create_request, update_request, delete_request
from app.api.deps import get_db

router = APIRouter()

@router.post("/", response_model=RequestRead)
def create_new_request(request_in: RequestCreate, db: Session = Depends(get_db)):
    request = create_request(db, request_in)
    return request

@router.get("/{req_id}", response_model=RequestRead)
def read_request(req_id: int, db: Session = Depends(get_db)):
    request = get_request(db, req_id)
    if not request:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Request not found")
    return request

@router.put("/{req_id}", response_model=RequestRead)
def update_existing_request(req_id: int, request_in: RequestUpdate, db: Session = Depends(get_db)):
    request = update_request(db, req_id, request_in)
    return request

@router.delete("/{req_id}", response_model=RequestRead)
def delete_existing_request(req_id: int, db: Session = Depends(get_db)):
    request = delete_request(db, req_id)
    return request
