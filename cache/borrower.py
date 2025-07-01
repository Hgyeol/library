from . import redis_client

def test():
    return "redis connect ok"
def borrow(borrower, title):
    borrow_key = f"borrower:{borrower}:books"
    redis_client.sadd(borrow_key, title)
def return_book(borrower, title):
    borrow_key = f"borrower:{borrower}:books"
    redis_client.srem(borrow_key, title)
    print("레디스 성공")