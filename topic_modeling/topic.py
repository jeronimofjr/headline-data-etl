from gensim.models import LsiModel

def topic_modeling(term_matrix, id2word_dict):
    lsa = LsiModel(term_matrix, num_topics=3, id2word = id2word_dict)

    return lsa.show_topics(num_topics=3, num_words=3)
