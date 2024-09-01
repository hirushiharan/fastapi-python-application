from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.models.user import User
from app.core.security import verify_password
from app.core.auth import decode_token

# OAuth2 password flow scheme
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/v1/login/access-token")

# Dependency to get the current user based on JWT token
def get_current_user(db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)) -> User:
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    payload = decode_token(token)
    if payload is None:
        raise credentials_exception
    email: str = payload.get("sub")
    if email is None:
        raise credentials_exception
    user = db.query(User).filter(User.email == email).first()
    if user is None:
        raise credentials_exception
    return user


# Dependency to verify user credentials
def verify_user_credentials(email: str, password: str, db: Session = Depends(get_db)) -> User:
    user = db.query(User).filter(User.email == email).first()
    print(f'USER: {user}')
    if user and verify_password(password, user.hashed_password):
        return user
    else:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
