from etl.extract import Ingestion
from etl.transform import Transform
from etl.load import load
from database.db import DB 


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

    bd = DB()
    bd.connection()
    
    load(bd, feednews)

if __name__ == '__main__':
    pipeline()