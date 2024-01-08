from pymongo.mongo_client import MongoClient
from dotenv import dotenv_values
from logging import info, exception
import os
from dotenv import load_dotenv

load_dotenv()

config = {"URI" : os.environ.get("URI"),
          "DATABASE" : os.environ.get("DATABASE")
          }

class Connection:
    def __init__(self) -> None:
        self.uri = config["URI"]
        self.client = None
        self.db = None

    def connect(self) -> None:
        try:
            self.client = MongoClient(self.uri)
            self.db = self.client[config["DATABASE"]]
            info("Database conectado")
        except Exception as e:
            exception("Falha na conexão")



