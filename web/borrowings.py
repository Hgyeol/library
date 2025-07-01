from fastapi import APIRouter

from model import Borrow
from service import borrowings as service

router = APIRouter(prefix="/borrows")

@router.get("")
def test():
    return service.test()

@router.post("")
def borrow(b: Borrow):
    # print(borrow.borrower, borrow.title)
    return service.borrow(b.borrower, b.title)

@router.get("/borrowers/{borrower}/books")
def get_borrowers(borrower: str):
    return service.get_borrow(borrower)