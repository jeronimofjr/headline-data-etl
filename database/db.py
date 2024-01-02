from pymongo.mongo_client import MongoClient
from dotenv import dotenv_values

config = dotenv_values(".env")


class DB:
    def __init__(self) -> None:
        self.uri = config["URI"]
        self.client = None
        self.connect = False
        self.db = None
        self.collection = None

    def connection(self):
        try:
            self.client = MongoClient(self.uri)
            self.connect = True
            self.db = self.client[config["DATABASE"]]
            self.collection = self.db[config["COLLECTION"]]
        except Exception as e:
            raise "Falha na conexão"
