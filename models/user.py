from uuid import UUID, uuid4
from pydantic import BaseModel

class DetailsOfBook(BaseModel):
    # id: UUID = uuid4()
    title: str
    author: str
    published_year: int
    genre: str
    is_available: bool

    