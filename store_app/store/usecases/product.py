from uuid import UUID
from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorDatabase
from store.db.mongo import db_client
from store.schemas.product import ProductIn, ProductOut
import store.core.exeptions as BaseException

class ProductUseCase:
    def __init__(self) -> None:
        breakpoint()
        self.client: AsyncIOMotorClient = db_client.get()
        self.database: AsyncIOMotorDatabase = self.client.get_database()
        self.collection = self.database["products"]
    
    async def create(self, body: ProductIn) -> ProductOut:
        product = ProductOut(**body.model_dump())
        await self.collection.insert_one(body.model_dump())
        
        return product
    
    async def get(self, id: UUID) -> ProductOut:
        result = await self.collection.find_one({"id": id})
        
        if not result:
            raise BaseException
        
        return ProductOut(**result)  
      
usecase = ProductUseCase()