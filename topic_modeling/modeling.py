from gensim import corpora
from gensim.models import LsiModel
import string
import nltk
import re
from tqdm import tqdm

nltk.download('stopwords')
nltk.download('wordnet')  
nltk.download('omw-1.4')  

from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer
# from t import file

class TopicModeling:
    def __init__(self) -> None:
        self.corpus = []
        self.stopwords = set(stopwords.words('english'))
        self.lemma = WordNetLemmatizer()
        self.term_matrix = []
        self.dictionary = None
        self.exclude = string.digits + string.punctuation
        self.num_topics = 5

    def to_doc_matrix(self) -> None:
        self.dictionary = corpora.Dictionary(self.corpus)
        self.term_matrix = [self.dictionary.doc2bow(doc) for doc in self.corpus]

    def get_topics(self, corpus: list) -> list:
        self.processing(corpus)
        self.to_doc_matrix()
        lsa = LsiModel(self.term_matrix, num_topics=self.num_topics, id2word=self.dictionary)

        topics = lsa.show_topics(num_topics=self.num_topics, num_words=1)
        return [re.search(r'"([\w]*)"' , topic[1]).group(1) for topic in topics]

    def clean(self, doc: str) -> str:
        stop_free = " ".join([i for i in doc.lower().split() if i not in self.stopwords])
        punc_free = "".join(ch for ch in stop_free if ch not in set(self.exclude))
        normalized = " ".join(self.lemma.lemmatize(word) for word in punc_free.split())
        return normalized

    def processing(self, corpus: list) -> None:
        self.corpus = [self.clean(doc).split() for doc in tqdm(corpus)]

