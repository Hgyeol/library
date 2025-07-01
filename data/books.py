from . import con, cur

def test():
    return "sqlite connect ok"

def add_book(title, author):
    try:
        sql = "INSERT INTO books (title, author) VALUES (?, ?)"
        cur.execute(sql, (title, author))
        con.commit()
        return True
    except :
        return False


def get_all():
    sql = "SELECT title, author, book_id FROM books"
    cur.execute(sql)
    rows = cur.fetchall()
    row_to_model = lambda row: {"title": row[0], "author": row[1], "book_id": row[2]}
    return [row_to_model(row) for row in rows]


def exist_book_id(book_id):
    sql = "SELECT title FROM books WHERE book_id = ?"
    cur.execute(sql, (book_id,))
    row = cur.fetchone()
    if row is not None:
        print("true1111")
        return True
    else:
        print("false111")
        return False


def delete_book(book_id):
    sql = "DELETE FROM books WHERE book_id = ?"
    cur.execute(sql, (book_id,))
    con.commit()
    return True


def get_book_id_by_title(title):
    sql = "SELECT book_id FROM books WHERE title = ?"
    cur.execute(sql, (title,))
    row = cur.fetchone()
    if row is not None:
        return row[0]
    else:
        return None


def update_available(book_id):
    sql = "UPDATE books SET available = ? WHERE book_id = ?"
    cur.execute(sql, (True, book_id))
    con.commit()

def update_disavailable(book_id):
    sql = "UPDATE books SET available = ? WHERE book_id = ?"
    cur.execute(sql, (False, book_id))
    con.commit()