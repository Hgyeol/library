from datetime import datetime

from . import con, cur

def test():
    return "sqlite connect ok"


# def update_book_id(book_id, borrower):
#     sql = "UPDATE borrowings SET book_id = ? WHERE borrower = ?"
#     cur.execute(sql, (book_id, borrower))
#     con.commit()
now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
def update_book_id(book_id, borrower):
    sql = 'update borrowings set book_id=?, borrowed_at=? where borrower=?'
    # sql = "UPDATE borrowings SET book_id = %s WHERE borrower = %s"
    cur.execute(sql, (book_id, now, borrower))
    # cur.execute(sql, (book_id, borrower))
    con.commit()

def update_return(borrower):
    sql = 'update borrowings set returned_at=? where borrower=?'
    cur.execute(sql, (now, borrower))
    con.commit()


def delete(borrower, book_id):
    sql = 'delete from borrowings where borrower=? and book_id=?'
    cur.execute(sql, (borrower, book_id))

    con.commit()
    print("성공")


def return_book_id(book_id, borrower):
    sql = 'update borrowings set returned_at=? where borrower=?'
    # sql = "UPDATE borrowings SET book_id = %s WHERE borrower = %s"
    cur.execute(sql, (now, borrower))
    # cur.execute(sql, (book_id, borrower))
    con.commit()