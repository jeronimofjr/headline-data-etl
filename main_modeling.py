from topic_modeling.pre_processing import processing
from topic_modeling.document_matrix import to_doc_matrix
from topic_modeling.topic import topic_modeling
from database.database import DB 
from tqdm import tqdm

bd = DB()

bd.connection()

corpus = []
for item in tqdm(bd.collection.find({}, {"summary" : 1})):
    try:
        corpus.append(item["summary"])
    except Exception as e:
       pass

# print(*corpus, sep="\n\n")

corpues_clean = processing(corpus)

doc_term_matrix, dictionary = to_doc_matrix(corpues_clean)

topics = topic_modeling(doc_term_matrix, dictionary)

print("TOPICS MODELS")

print(*topics, sep="\n\n")