from passlib.context import CryptContext
import random
import string

# Create a password context with hashing algorithms
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str) -> str:
    """
    Hash a password using bcrypt.
    """
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    """
    Verify a password against a hashed password.
    """
    return pwd_context.verify(plain_password, hashed_password)

def temp_password(length=12):
    characters = string.ascii_letters + string.digits + "!@#$%^&*()"
    password = hash_password
    return ''.join(random.choice(characters) for i in range(length))
