from fastapi import FastAPI
from api.core.database import Base, engine
from api.routes import users, auth

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(users.router, prefix="/users", tags=["Users"])
app.include_router(auth.router, prefix="/auth", tags=["Auth"])
