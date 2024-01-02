from gensim import corpora


def to_doc_matrix(corpus):
    dictionary = corpora.Dictionary(corpus)
    doc_term_matrix = [dictionary.doc2bow(doc) for doc in corpus]

    return doc_term_matrix, dictionary