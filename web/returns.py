from fastapi import APIRouter

from model import Borrow
from service import borrowings as service

router = APIRouter(prefix="/return")

@router.get("")
def test():
    return service.test()

@router.post("")
def borrow(borrow: Borrow):
    # print(borrow.borrower, borrow.title)
    return service.return_book(borrow.borrower, borrow.title)