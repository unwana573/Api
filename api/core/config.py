from dotenv import load_dotenv
import os

load_dotenv()


class Settings:
    POSTGRES_DB: str = os.getenv("POSTGRES_DB")
    POSTGRES_USER: str = os.getenv("POSTGRES_USER")
    POSTGRES_PASSWORD: str = os.getenv("POSTGRES_PASSWORD")
    POSTGRES_SERVER: str = os.getenv("POSTGRES_SERVER")
    POSTGRES_PORT: str = os.getenv("POSTGRES_PORT")

    DATABASE_URL: str = (
        f"postgresql+psycopg2://{POSTGRES_USER}:"
        f"{POSTGRES_PASSWORD}@{POSTGRES_SERVER}:"
        f"{POSTGRES_PORT}/{POSTGRES_DB}"
    )

    SECRET_KEY: str = os.getenv("SECRET_KEY", "dev-secret")
    REFRESH_SECRET_KEY: str = os.getenv("REFRESH_SECRET_KEY", "dev-refresh-secret")
    ALGORITHM: str = os.getenv("ALGORITHM", "HS256")

    ACCESS_TOKEN_EXPIRE_MINUTES: int = int(
        os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", 15)
    )
    REFRESH_TOKEN_EXPIRE_DAYS: int = int(
        os.getenv("REFRESH_TOKEN_EXPIRE_DAYS", 7)
    )


settings = Settings()
