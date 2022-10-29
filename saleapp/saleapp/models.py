from sqlalchemy import Column, Integer, String, Text, Float, ForeignKey, BOOLEAN
from saleapp import db, app
from sqlalchemy.orm import relationship

class BaseModel(db.Model):
    __abstract__ = True
    id = Column(Integer, primary_key=True, autoincrement=True)

class Category(BaseModel):
    __tablename__ = "category"
    name = Column(String(50), nullable=True)
    Products = relationship('Product', backref = 'category', lazy=True)

class Product(BaseModel):
    name = Column(String(50), nullable=True)
    description = Column(Text)
    price = Column(Float, default=0)
    image = Column(String(200))
    active = Column(BOOLEAN, default=True)
    category_id = Column(Integer, ForeignKey(Category.id), nullable=False)

if __name__ == "__main__":
    with app.app_context():
        # c1 = Category(name="Điện thoại")
        # c2 = Category(name="Máy tính bảng")
        # c3 = Category(name="Phụ kiện")
        # db.session.add_all([c1, c2, c3])
        # db.session.commit()
        p1 = Product(name='Galaxy S22 Pro', description='Samsung, 128GB', price=25000000,
                     image='https://res.cloudinary.com/dxxwcby8l/image/upload/v1646729569/fi9v6vdljyfmiltegh7k.jpg',
                     category_id=1)
        p2 = Product(name='Galaxy Fold 4', description='Samsung, 128GB', price=38000000,
                     image='https://res.cloudinary.com/dxxwcby8l/image/upload/v1647248722/r8sjly3st7estapvj19u.jpg',
                     category_id=1)
        p3 = Product(name='Apple Watch S5', description='Apple, 32GB', price=18000000,
                     image='https://res.cloudinary.com/dxxwcby8l/image/upload/v1646729569/fi9v6vdljyfmiltegh7k.jpg',
                     category_id=3)
        p4 = Product(name='Galaxy Tab S8', description='Samsung, 128GB', price=22000000,
                     image='https://res.cloudinary.com/dxxwcby8l/image/upload/v1646729569/fi9v6vdljyfmiltegh7k.jpg',
                     category_id=2)
        db.session.add_all([p1, p2, p3,p4])
        db.session.commit()
        # db.create_all()