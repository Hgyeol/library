from pydantic import BaseModel


class BookCreate(BaseModel):
    title: str
    author: str

class BookDelete(BaseModel):
    book_id: int

class Borrow(BaseModel):
    borrower: str
    title: str