from etl.extract import Ingestion
from etl.transform import Transform
from etl.load import load_data

from database.database import Connection
from logging import INFO, info, WARNING, warning

def pipeline_data():
    # print("Extração de dados")
    ingestion = Ingestion()
    feednews = ingestion.extract()
    # print("")

    # print("Transformação dos dados")

    transform = Transform(feednews)
    feednews = transform.transform()
    # print("")
    # print("Inserção  dos dados\n")

    bd = Connection()
    bd.connect()
    
    load_data(bd, feednews)

# if __name__ == '__main__':
#     try:
#         pipeline_data()
#     except Exception as e:
#         print(e)