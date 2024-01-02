import string
import nltk
from tqdm import tqdm

nltk.download('stopwords')
nltk.download('wordnet')  
nltk.download('omw-1.4')  

from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer


stop = set(stopwords.words('english'))
exclude = set(string.punctuation)
lemma = WordNetLemmatizer()

def clean(doc):
    stop_free = " ".join([i for i in doc.lower().split() if i not in stop])
    punc_free = "".join(ch for ch in stop_free if ch not in exclude)
    normalized = " ".join(lemma.lemmatize(word) for word in punc_free.split())
    return normalized

def processing(corpus):
    return [clean(doc).split() for doc in tqdm(corpus)]