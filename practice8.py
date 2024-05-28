from sqlite3 import Date

import pymongo
import math
import random
import datetime as dt

def main():
    client = pymongo.MongoClient()
    print(client)

    # for db in client.list_databases():
    #     print(db)

    db_conn = client.get_database("practice")
    # print(db_conn)

    # 빈 딕셔너리 리스트

    # db.users.find({"username": "user01"})
    rs = db_conn.get_collection("user").find({"username": "user100"}).explain()
    print(rs.keys())
    print(rs.serverInfo)

main()