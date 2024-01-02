from tqdm import tqdm
from logging import info


def load_data(db, feednews: dict):
    info("Inserção dos dados no database iniciada!!!")
    for press in tqdm(feednews.keys()):
        db.collection.insert_many(feednews[press])
