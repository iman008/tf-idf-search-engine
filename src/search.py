import json
import math
from tokenizer import tokenizer_from_string
from cosine_similarity import cosine_sim
from time import time

word_doc_dict = dict(json.loads(open("unique_words.txt").read()))

tfidf_per_doc = dict(json.loads(open("tfidf_per_doc.txt").read()))
tfidf_norm_per_doc = dict(json.loads(open("tfidf_norm_per_doc.txt").read()))

def calculate_tfidf_for_query(query,doc_id):
    tokens = tokenizer_from_string(query)

    # Filter out tokens that are not in current doc
    tokens = [token for token in tokens if token in tfidf_per_doc[str(doc_id)]]
    query_tfidf = {}
    sum_squared = 0

    for token in tokens:
        tf = tokens.count(token) / len(tokens) if len(tokens) > 0 else 0

        idf = math.log10(50001 / len(word_doc_dict[token]))

        tfidf = tf * idf
        query_tfidf[token] = tfidf

        sum_squared += tfidf**2

    query_tfidf = dict(sorted(query_tfidf.items(), key=lambda t: t[1], reverse=True))

    query_norm = math.sqrt(sum_squared)

    return query_tfidf, query_norm


def search(query_text,doclist):
    res=[]
    start_time=time()
    for x in doclist:
        query_tfidf,query_norm=calculate_tfidf_for_query(query_text,x)
        res.append((x,cosine_sim(query_tfidf,query_norm,tfidf_per_doc[str(x)],tfidf_norm_per_doc[str(x)])))
    res.sort(key=lambda x:x[1],reverse=True)
    end_time=time()
    duration_ms = (end_time - start_time) * 1000
    print(f"Time took to search: {duration_ms:.2f} ms")
    return res


