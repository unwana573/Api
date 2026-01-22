from fastapi import FastAPI
from api.routes import auth, users
from api.core.database import Base, engine

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(auth.router, prefix="/auth", tags=["Auth"])
app.include_router(users.router, prefix="/users", tags=["Users"])


# uvicorn api.main:app --reload