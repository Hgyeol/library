from data import books as data
from cache import borrower as cache

def test():
    db_test = data.test()
    redis_test = cache.test()
    return {"sqlite": db_test, "redis": redis_test}

def add_book(title, author):
    return data.add_book(title, author)


def get_all_books():
    return data.get_all()


def delete_book(book_id):
    if data.exist_book_id(book_id):
        return data.delete_book(book_id)
    else:
        return False