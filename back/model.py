#portfolio
#handle: _MUMINUL__ISLAM___

#CODE
from sqlalchemy import Column,Integer,String
from sqlalchemy.orm import declarative_base

Base=declarative_base()

class Product_Model(Base):
    __tablename__="products"

    product_id=Column(Integer,primary_key=True)
    product_name=Column(String)
    product_model=Column(String)
    product_core=Column(Integer)