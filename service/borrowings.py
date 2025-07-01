from data import borrowings as data
from data import books as book_data
from cache import borrower as cache

def test():
    db_test = data.test()
    redis_test = cache.test()
    return {"sqlite": db_test, "redis": redis_test}


def borrow(borrower, title):
    book_id = book_data.get_book_id_by_title(title)
    if book_id is None:
        return False
    # print(book_id)
    try:
        book_data.update_disavailable(book_id)
        data.update_book_id(book_id, borrower)
        cache.borrow(borrower, title)
        return True
    except:
        return False
def return_book(borrower, title):
    book_id = book_data.get_book_id_by_title(title)
    if book_id is None:
        return False
    try:
        book_data.update_available(book_id)
        # data.delete(borrower, book_id)
        data.return_book_id(book_id, borrower)
        cache.return_book(borrower, title)
        return True
    except:
        print("에러")
        return False