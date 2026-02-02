from typing import Optional
from pydantic import BaseModel

class ProductCreate(BaseModel):
    name: str
    price: int
    description: Optional[str] = None   
    quantity: int

class deleteProduct(BaseModel):
    name: str

class productsOut(ProductCreate):
    class Config:
        from_attributes = True

class ProductResponse(ProductCreate):
    id: int
    admin_id: int

    class Config:
        from_attributes = True


