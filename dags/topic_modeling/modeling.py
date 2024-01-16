from gensim import corpora
from gensim.models import LsiModel
from more_itertools import flatten
import string
import nltk
import re
from tqdm import tqdm
import pytz
from datetime import datetime


# nltk.download('stopwords')
# nltk.download('wordnet')  
# nltk.download('omw-1.4')  

from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer

file = {"BBC" : [{ "summary" : "Christian Marriott, 46, had been helping an unconscious woman when the car hit him and others." },
{  "summary" : "Maine's top election official has ruled Trump cannot run for president next year in the state." },
{ "summary" : "Israeli tanks reportedly reach the outskirts of Bureij refugee camp as the ground offensive expands." },
{ "summary" : "We asked three military analysts how they think events may unfold in the coming 12 months." },
{  "summary" : "Proposals put to the former PM included a detention camp on Mull, newly-released files from 2003 show." }],
"ONU" : [{ "summary" : "An increase in antisemitism and Islamophobia is reported by major UK police forces." },
{  "summary" : "Some properties in the north of Scotland will not be reconnected to the electricity grid until Friday." },
{ "summary" : "Footage from the cockpit shows the helicopter rocking side to side after being hit by winds of up to 80mph." },
{ "summary" : "A tree crashed into another woman's bathroom during the tornado near Manchester in Storm Gerrit." },
{ "summary" : "Emergency services were called to the River Esk in the North York Moors, police say." }]}

class TopicModeling:
    def __init__(self) -> None:
        # print(stopwords.words('english'))
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
        stop_free = " ".join([i for i in doc.lower().split() if i not in self.stopwords and i != 'un'])
        punc_free = "".join(ch for ch in stop_free if ch not in set(self.exclude))
        normalized = " ".join(self.lemma.lemmatize(word) for word in punc_free.split())
        return normalized

    def processing(self, corpus: list) -> None:
        self.corpus = [self.clean(doc).split() for doc in tqdm(corpus)]

    def make_topics(self, feednews: dict) -> dict:
        presses = feednews.keys()
        news_summary = []
        for press in presses:
           news_summary.extend([news["summary"] for news in feednews[press] if "summary" in news.keys()])

        self.processing(corpus=news_summary)
        topics_list = self.get_topics(news_summary)
        return {"topics" : topics_list, "date" : datetime.now(pytz.timezone('America/Sao_Paulo')).strftime("%d/%m/%Y %H:%M:%S")}