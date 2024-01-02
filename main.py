from etl.extract import Ingestion
from etl.transform import Transform
from etl.load import load
from database.database import Connection
from logging import INFO, info

def pipeline():
    print("Extração de dados")
    ingestion = Ingestion()
    feednews = ingestion.extract()
    print("")

    print("Transformação dos dados")

    transform = Transform(feednews)
    feednews = transform.transformation()
    print("")
    print("Inserção  dos dados\n")

    bd = Connection()
    bd.connect()
    
    load(bd, feednews)

if __name__ == '__main__':
    pipeline()