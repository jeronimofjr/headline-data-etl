from tqdm import tqdm


def load(db, feednews: dict):
    for agencia in tqdm(feednews.keys()):
        db.collection.insert_many(feednews[agencia])
