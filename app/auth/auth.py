from app.db.session import SessionLocal
from app.models.user import User
from app.auth.hashing import verify_password
from sqlalchemy.orm import Session

def authenticate_user(db: Session, username: str, password: str):
    user = db.query(User).filter(User.username == username).first()
    if not user:
        return False
    if not verify_password(password, user.hashed_password):
        return False
    return user
