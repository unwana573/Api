from api.models.models import Product
from sqlalchemy.orm import Session
from api.schemas.products import ProductCreate, deleteProduct, ProductUpdate
from api.models.models import User
from fastapi import HTTPException, Depends
from api.core.database import get_db

def get_all_products(db: Session):
    return db.query(Product).all()

def create_product(product: ProductCreate, admin_id: int, db: Session):
    db_product = Product(
        name=product.name,
        price=product.price,
        description=product.description,
        quantity=product.quantity,
        admin_id=admin_id
    )
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

def update_product(product_name: str, product: ProductUpdate, db: Session):
    db_product = db.query(Product).filter(Product.name == product_name).first()
    if not db_product:
        raise HTTPException(status_code=404, detail="Product not found")
    
    if product.name is not None:
        db_product.name = product.name
    if product.price is not None:
        db_product.price = product.price
    if product.description is not None:
        db_product.description = product.description
    if product.quantity is not None:
        db_product.quantity = product.quantity

    db.commit()
    db.refresh(db_product)
    return db_product

def delete_product(product_name: str, db: Session):
    product = db.query(Product).filter(Product.name == product_name).first()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    db.delete(product)
    db.commit()
    return {"message": "Product deleted successfully"}