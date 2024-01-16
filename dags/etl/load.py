from tqdm import tqdm
from logging import info


def load_data(connection, feednews: dict):
    info("Inserção dos dados no database iniciada!!!")
    for press in tqdm(feednews.keys()):
        connection.db['headlines'].insert_many(feednews[press])

def load_topics(connection, topics: dict):
    info("Inserção dos tópicos do dia no database iniciada!!!")
    connection.db["topics"].insert_one(topics)
