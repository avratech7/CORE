import math

# use by the tf function
def max_term_in_d(d_terms_list):
    return max([d_terms_list.count(i) / len(d_terms_list) for i in d_terms_list])

def tf(term,d_terms_list):
    return 0.5 + 0.5 * ((d_terms_list.count(term)/ len(d_terms_list)) / max_term_in_d(d_terms_list))

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
    if idf(t,D):
        return tf(t,d) * idf(t,D)
    else: return 0



"""
if you get a list of docs of terms - this function return the average of tf-idf score of specific term in all labels docs 
"""
def calculate_tfidf_with_averege(docs_label,all_docs,label):
    score_shits = {}
    for doc in docs_label:
        for term in doc:
            # to insert score for one term only once for a document
            checked = []
            if term not in checked:
                if term not in score_shits.keys():
                    score_shits[term] = {'label': label, 'score': 0, 'counter': 0}
                score_shits[term]['score'] += tfidf(term, doc, all_docs)
                score_shits[term]['counter'] += 1
                checked.append(term)
    # calc the averege
    for term in score_shits:
        score_shits[term]['score'] /= score_shits[term]['counter']
    return score_shits

