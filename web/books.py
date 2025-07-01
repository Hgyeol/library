from fastapi import APIRouter

import data
from model import BookCreate
from service import books as service

router = APIRouter(prefix="/books")

@router.get("")
def test():
    return service.get_all_books()

@router.post("")
def add_book(book: BookCreate):
    return service.add_book(book.title, book.author)

@router.delete("/{book_id}")
def delete_book(book_id: int):
    return service.delete_book(book_id)
