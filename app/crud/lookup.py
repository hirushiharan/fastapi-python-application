from sqlalchemy.orm import Session
from app.models.lookup import Lookup
from app.schemas.lookup import LookupCreate, LookupUpdate

def create_lookup(db: Session, lookup: LookupCreate) -> Lookup:
    db_lookup = Lookup(**lookup.model_dump())
    db.add(db_lookup)
    db.commit()
    db.refresh(db_lookup)
    return db_lookup

def get_lookup(db: Session, lookup_id: int) -> Lookup:
    return db.query(Lookup).filter(Lookup.lookup_id == lookup_id).first()

def get_lookups(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Lookup).offset(skip).limit(limit).all()

def update_lookup(db: Session, lookup_id: int, lookup: LookupUpdate) -> Lookup:
    db_lookup = db.query(Lookup).filter(Lookup.lookup_id == lookup_id).first()
    if db_lookup:
        for key, value in lookup.model_dump(exclude_unset=True).items():
            setattr(db_lookup, key, value)
        db.commit()
        db.refresh(db_lookup)
    return db_lookup

def delete_lookup(db: Session, lookup_id: int):
    db_lookup = db.query(Lookup).filter(Lookup.lookup_id == lookup_id).first()
    if db_lookup:
        db.delete(db_lookup)
        db.commit()
    return db_lookup
