from dags.etl.extract import Ingestion
from dags.etl.transform import Transform
from dags.topic_modeling.modeling import TopicModeling
from dags.database.database import Connection
from dags.etl.load import load_data, load_topics

def pipeline_data():
    print("Extração de dados")
    ingestion = Ingestion()
    feednews = ingestion.extract()

    print("\nTransformação dos dados")
    transform = Transform(feednews)
    feednews = transform.transform()
    
    print("\nCaptura dos tópicos")
    topic_modeling = TopicModeling()
    topics = topic_modeling.make_topics(feednews)
    
    print("\nInserção  dos dados\n")
    connection = Connection()
    connection.connect()
    load_data(connection, feednews)
    load_topics(connection, topics)