from itertools import product
from fastapi import APIRouter, Depends
from api.auth.dependencies import get_current_admin, require_admin
from api.core.database import get_db
from api.models.models import User, Product
from api.repositories.products_repository import create_product, get_all_products
from api.schemas.products import ProductResponse, deleteProduct, productsOut, ProductCreate
from sqlalchemy.orm import Session

router = APIRouter(tags=["Products"])

@router.post("/")
def create_product(
    product: ProductCreate,
    db: Session = Depends(get_db),
    admin = Depends(get_current_admin),
):
    db_product = Product(
        name=product.name,
        price=product.price,
        description=product.description,
        quantity=product.quantity,
        admin_id=admin.id   
    )

    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product


@router.put("/", response_model=list[ProductCreate])
def update_product(db: Session = Depends(get_db), current_user=Depends(require_admin)):
    return

@router.delete("/", response_model=list[deleteProduct])
def delete_product(db: Session = Depends(get_db), current_user=Depends(require_admin)):
    return

@router.get("/", response_model=list[productsOut])
def view_products(db: Session = Depends(get_db),):
    return get_all_products(db)
