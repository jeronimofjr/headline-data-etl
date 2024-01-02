from pymongo.mongo_client import MongoClient
from dotenv import dotenv_values
from logging import INFO, info, basicConfig, warning, exception

config = dotenv_values(".env")

basicConfig(format="%(asctime)s - %(message)s", datefmt="%d-%b-%y %H:%M:%S", level=INFO)

class DB:
    def __init__(self) -> None:
        self.uri = config["URI"]
        self.client = None
        self.db = None
        self.collection = None

    def connect(self):
        try:
            self.client = MongoClient(self.uri)
            self.db = self.client[config["DATABASE"]]
            self.collection = self.db[config["COLLECTION"]]
            info("Database conectado")
        except Exception as e:
            exception("Falha na conexão")

