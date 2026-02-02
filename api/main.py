from fastapi import FastAPI
from api.routes import auth, products, users
from api.core.database import Base, engine

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(auth.router, prefix="/auth", tags=["Auth"])
app.include_router(users.router, prefix="/users", tags=["Users"])
app.include_router(products.router, prefix="/products", tags=["Products"])


# uvicorn api.main:app --reload