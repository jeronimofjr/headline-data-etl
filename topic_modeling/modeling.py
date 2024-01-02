from gensim import corpora
from gensim.models import LsiModel
import string
import nltk
from tqdm import tqdm

nltk.download('stopwords')
nltk.download('wordnet')  
nltk.download('omw-1.4')  

from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer


class TopicModeling:
    def __init__(self, corpus, num_topics=3) -> None:
        self.corpus = self.processing(corpus)
        self.stopwords = set(stopwords.words('english'))
        self.lemma = WordNetLemmatizer()
        self.num_topics = num_topics

    def to_doc_matrix(self):
        dictionary = corpora.Dictionary(self.corpus)
        doc_term_matrix = [dictionary.doc2bow(doc) for doc in self.corpus]

        return doc_term_matrix, dictionary

    def get_topics(self,  id2word_dict, term_matrix):
        lsa = LsiModel(term_matrix, num_topics=3, id2word = id2word_dict)

        return lsa.show_topics(num_topics=3, num_words=3)
    
    def clean(self, doc: str) -> str:
        stop_free = " ".join([i for i in doc.lower().split() if i not in self.stopwords])
        punc_free = "".join(ch for ch in stop_free if ch not in set(self.exclude))
        normalized = " ".join(self.lemma.lemmatizer(word) for word in punc_free.split())
        return normalized

    def processing(self, corpus: list) -> list:
        return [self.clean(doc).split() for doc in tqdm(corpus)]