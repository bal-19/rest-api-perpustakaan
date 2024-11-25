from pydantic import BaseModel
from typing import Optional, List

from models.perpusnas import PerpusnasModel

class PerpusnasResponse(BaseModel):
    query: Optional[str] = None
    page: int
    limit: int
    total_data: int
    total_pages: int
    result: List[PerpusnasModel]