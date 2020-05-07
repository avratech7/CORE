import math

# use by the tf function
# def max_term_in_d(d_terms_list):
#     return max([d_terms_list.count(i) / len(d_terms_list) for i in d_terms_list])

# def tf(term,d_terms_list):
#     return 0.5 + 0.5 * ((d_terms_list.count(term)/ len(d_terms_list)) / max_term_in_d(d_terms_list))


def tf_temp (term,document):
    return document.count(term)/len(document)


def max_term_in_d(document):
    return  max(tf_temp(term,document)for term in document)

def tf(term,document):
    return  0.5 + 0.5 * tf_temp(term,document)/max_term_in_d(document)

# use by the idf function
def num_docs_has_the_term(term,list_of_document):
    count = 0
    for i in list_of_document:
        if term in i:
            count += 1
    return count

def idf(term,list_of_documents):
    if num_docs_has_the_term(term,list_of_documents):
        return math.log(len(list_of_documents) / num_docs_has_the_term(term,list_of_documents))

def tfidf(t,d,D):
        return tf(t,d) * idf(t,D)

docs = [
        ["yes","ball","no"],
        ["yes","yellow card","no","yes","ball","yellow card"],
        ["yellow card","no","yes","ball","ball","yellow card"],
        ["no","yellow card","yes"],
        ["yes","pain","pain","yes"],
        ["no","no","no","pain", "pain","yes","yes"],
        ["medical","medical","medical","medical","medical"]
        ]



for doc in docs:
    doc_terms_score = {}
    for term in doc:
        doc_terms_score[term] = {"label": "sport", "score": tfidf(term,doc,docs)}
    print(doc_terms_score)
