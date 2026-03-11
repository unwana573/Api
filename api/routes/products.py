from itertools import product
from fastapi import APIRouter, Depends, HTTPException
from api.auth.dependencies import get_current_admin, require_admin
from api.core.database import get_db
from api.models.models import User, Product
from api.repositories.products_repository import create_product, get_all_products, delete_product, update_product
from api.schemas.products import ProductResponse, deleteProduct, productsOut, ProductCreate, ProductUpdate
from sqlalchemy.orm import Session

router = APIRouter(tags=["Products"])

@router.get("/", response_model=list[productsOut])
def view_products(db: Session = Depends(get_db),):
    return get_all_products(db)

@router.post("/")
def create_product_route(
    product: ProductCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_admin)
):
    return create_product(product, current_user.id, db)

@router.put("/{product_name}")
def update_product_route(
    product_name: str,
    product: ProductUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_admin)
):
    return update_product(product_name, product, db)

@router.delete("/{product_name}")
def delete_product_route(
    product_name: str,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_admin)
):
    return delete_product(product_name, db)
