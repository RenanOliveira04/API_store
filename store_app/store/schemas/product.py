from pydantic import Field
from store.schemas.base import BaseSchemaMixin

class ProductIn(BaseSchemaMixin):
    name: str = Field (..., description="Product name")
    quantity: int = Field (..., description="Product quantity")
    price: float = Field (..., description="Product price")
    status: bool = Field (..., description="Product status")
    
class ProductOut(ProductIn):
    id: str = Field (..., description="Product id")
    
    class Config:
        orm_mode = True