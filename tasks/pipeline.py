from tasks.etl.extract import Ingestion
from tasks.etl.transform import Transform
from tasks.topic_modeling.modeling import TopicModeling
from tasks.database.database import Connection
from tasks.etl.load import load_data, load_topics


def pipeline_data():
    print("Extração de dados")
    ingestion = Ingestion()
    feednews = ingestion.extract()
    print("")

    print("Transformação dos dados")

    transform = Transform(feednews)
    feednews = transform.transform()
    
    print("Captura dos tópicos")
    topics = transform.take_topics(TopicModeling)
    
    print("")
    print("Inserção  dos dados\n")

    connection = Connection()
    connection.connect()
    
    load_data(connection, feednews)
    load_topics(connection, topics)

# pipeline_data()