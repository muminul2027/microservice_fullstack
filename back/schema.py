#portfolio
#handle: _MUMINUL__ISLAM___

#CODE

from pydantic import BaseModel

class Product_Schema(BaseModel):
    product_id: int
    product_name: str
    product_model: str
    product_core: int

