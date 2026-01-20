from passlib.context import CryptContext
import hashlib

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str) -> str:
    """
    Hash the password using SHA256 first, then bcrypt.
    Ensures bcrypt does not receive more than 72 bytes.
    """
    # Step 1: SHA256 hash (hex digest is 64 characters)
    sha256_hash = hashlib.sha256(password.encode('utf-8')).hexdigest()

    # Step 2: bcrypt hash
    return pwd_context.hash(sha256_hash)


def verify_password(password: str, hashed_password: str) -> bool:
    """
    Verify password by applying SHA256 and comparing with bcrypt hash.
    """
    sha256_hash = hashlib.sha256(password.encode('utf-8')).hexdigest()
    return pwd_context.verify(sha256_hash, hashed_password)
