from tokenizer import tokenizer
import json
import math



# consider i want to calculate tf-idf of document one
# i create a mapping between each token of that doc and map that token to its tf-idf number
# for each token the tf(token,doc) is word_doc_dict[token][id of that doc]/length of that doc;
# for each token the idf(token,D) is log(50000/len(word_doc_dict[token]))




word_doc_dict=dict(json.loads(open("unique_words.txt").read()))
tfidf_per_doc={}
tfidf_norm_per_doc={}
for i in range(0,50001):
    print(i)
    tfidf_per_doc[i]={}
    filepath="../data/document_"+str(i)+".txt"
    tokens=tokenizer(filepath)
    di=len(tokens)
    sum_squared=0
    for x in tokens:
        tf=word_doc_dict[x][str(i)]/di
        idf=math.log10(50001/len(word_doc_dict[x]))
        tfidf_per_doc[i][x]=tf*idf
        sum_squared+=(tf*idf)**2
    s=tfidf_per_doc[i]
    tfidf_per_doc[i]=dict(sorted(s.items(),key=lambda t:t[1],reverse=True) )
    tfidf_norm_per_doc[i]=math.sqrt(sum_squared)


open("tfidf_per_doc.txt","w").write(json.dumps(tfidf_per_doc))
open("tfidf_norm_per_doc.txt","w").write(json.dumps(tfidf_norm_per_doc))


