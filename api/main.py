from fastapi import FastAPI
import uvicorn
from api.routes.users import router as user_router
from api.database import Base, engine

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(user_router, prefix="/users", tags=["Users"])

if __name__ == '__main__':
    uvicorn.run('main:app', port=8000, reload=True)  