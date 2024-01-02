from tqdm import tqdm

class Load:
    def load(db, feednews: dict):
        for press in tqdm(feednews.keys()):
            db.collection.insert_many(feednews[press])
