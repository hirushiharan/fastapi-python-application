from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.schemas.lookup import LookupCreate, LookupRead, LookupUpdate
from app.crud.lookup import get_lookup, create_lookup, update_lookup, delete_lookup
from app.api.deps import get_db, get_current_active_user

router = APIRouter()

@router.post("/", response_model=LookupRead)
def create_new_lookup(lookup_in: LookupCreate, db: Session = Depends(get_db)):
    lookup = create_lookup(db, lookup_in)
    return lookup

@router.get("/{lookup_id}", response_model=LookupRead)
def read_lookup(lookup_id: int, db: Session = Depends(get_db)):
    lookup = get_lookup(db, lookup_id)
    if not lookup:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Lookup not found")
    return lookup

@router.put("/{lookup_id}", response_model=LookupRead)
def update_existing_lookup(lookup_id: int, lookup_in: LookupUpdate, db: Session = Depends(get_db)):
    lookup = update_lookup(db, lookup_id, lookup_in)
    return lookup

@router.delete("/{lookup_id}", response_model=LookupRead)
def delete_existing_lookup(lookup_id: int, db: Session = Depends(get_db)):
    lookup = delete_lookup(db, lookup_id)
    return lookup
