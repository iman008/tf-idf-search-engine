import json
from tokenizer import tokenizer, tokenizer_from_string

word_doc_dict=dict(json.loads(open("unique_words.txt").read()))

query=""
query_tfidf={}
query_tfidf_norm=0

tokens=tokenizer_from_string (query)
di=len(tokens)
sum_squared=0

# TODO: tfidf calcualtion of query
