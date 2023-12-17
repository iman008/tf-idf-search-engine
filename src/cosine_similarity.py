# TODO
# gets the tf-idf dictionary of query and tf-idf of each document and then calculates the cosine similarity between them. for fast
# calculation the tf-idf of each doc is in tfidf_per_doc.txt and norm of tf-idf vector of each doc is stored in tfidf_norm_per_doc

def cosine_sim(query_dict,query_norm,doc_dict,doc_norm):
    numerator=0
    for x in query_dict:
        numerator+=query_dict[x]*doc_dict[x]
    denumerator = query_norm*doc_norm
    if denumerator==0:
        return 0
    return numerator/denumerator