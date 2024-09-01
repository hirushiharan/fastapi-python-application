from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.schemas.user import UserCreate, UserRead, UserUpdate
from app.crud.user import get_user, create_user, update_user, delete_user
from app.api.deps import get_db, get_current_active_user

router = APIRouter()

@router.post("/", response_model=UserRead)
def create_new_user(user_in: UserCreate, db: Session = Depends(get_db)):
    user = create_user(db, user_in)
    return user

@router.get("/{user_id}", response_model=UserRead)
def read_user(user_id: int, db: Session = Depends(get_db)):
    user = get_user(db, user_id)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    return user

@router.put("/{user_id}", response_model=UserRead)
def update_existing_user(user_id: int, user_in: UserUpdate, db: Session = Depends(get_db)):
    user = update_user(db, user_id, user_in)
    return user

@router.delete("/{user_id}", response_model=UserRead)
def delete_existing_user(user_id: int, db: Session = Depends(get_db)):
    user = delete_user(db, user_id)
    return user
