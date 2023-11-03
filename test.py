import sqlite3
import pymongo

# 连接到 SQLite 数据库文件
sqlite_connection = sqlite3.connect("fe/data/book.db")
sqlite_cursor = sqlite_connection.cursor()

# 连接到 MongoDB 服务器
mongo_client = pymongo.MongoClient("mongodb://localhost:27017/")
db = mongo_client["bookstore"]

# 创建一个名为 "book" 的集合，用于存储图书详细信息
book_collection = db["book"]

# 从 SQLite 数据库中读取数据
sqlite_cursor.execute("SELECT * FROM book")
sqlite_data = sqlite_cursor.fetchall()

# 将数据插入到 MongoDB 集合中
for row in sqlite_data:
    book_doc = {
        "id": row[0],
        "title": row[1],
        "author": row[2],
        "publisher": row[3],
        "original_title": row[4],
        "translator": row[5],
        "pub_year": row[6],
        "pages": row[7],
        "price": row[8],
        "currency_unit": row[9],
        "binding": row[10],
        "isbn": row[11],
        "author_intro": row[12],
        "book_intro": row[13],
        "content": row[14],
        "tags": row[15],
        # 如果有图书封面图片字段，需要根据实际情况添加
    }
    book_collection.insert_one(book_doc)

# 关闭连接
sqlite_connection.close()
mongo_client.close()
