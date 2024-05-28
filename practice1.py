import pymongo
import math
import random
import datetime as dt
import json

def main():
    client = pymongo.MongoClient()
    print(client)

    for db in client.list_databases():
        print(db)

    db_conn = client.get_database("practice")
    print(db_conn)

    # 빈 딕셔너리 리스트
    user = []
    # user = list
    for i in range(1000000):
        user.append(
            {
                "id": i,
                "username": "user" + str(i),
                "age": math.floor(random.random() * 100),
                "created": dt.datetime.now()
            }
        )

    db_conn.get_collection("user").insert_many(user)
    #
    # for col in db_conn.list_collection_names():
    #     print(col)
    #
    # collection = db_conn.get_collection("students")
    # print(collection)
    #
    # result = collection.find()
    # ds = list(result)
    # print("Number of data: {}".format(len(ds)))
    #
    # for data in ds:
    #     print(data)

# ./data/movies.json을 읽어서 mongodb에 삽입한다.
def set_data():
    client = pymongo.MongoClient()
    db_conn = client.get_database("practice")
    # json을 읽는다.
    with open("./data/movies.json", "r") as f:
        # open_file = f.read()
        json_data = json.load(f)
        print(json.dumps(json_data, indent=4))





# main()
set_data()