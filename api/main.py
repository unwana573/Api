from fastapi import FastAPI
from api.routes.users import router as user_router
from api.database import Base, engine

app = FastAPI()

# create tables
Base.metadata.create_all(bind=engine)

# include routers
app.include_router(user_router, prefix="/users", tags=["users"])
