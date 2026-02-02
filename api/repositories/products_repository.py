from api.models.models import Product
from sqlalchemy.orm import Session
from api.schemas.products import ProductCreate

def get_all_products(db:Session):
    return db.query(Product).all()

def create_product(db: Session, product: ProductCreate, admin_id: int):
    new_product = Product(
        name=product.name,
        price=product.price,
        description=product.description,
        quantity=product.quantity,
        admin_id=admin_id
    )
    db.add(new_product)
    db.commit()
    db.refresh(new_product)
    return new_product