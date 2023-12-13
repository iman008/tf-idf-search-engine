import string
import os
from tokenizer import tokenizer
import json 


docsPath="../data/"

word_doc_dict={}

for i in range(0,20000):
    filename="document_"+str(i)+".txt"
    list_words=tokenizer(docsPath+filename)
    for w in list_words:
        if word_doc_dict.get(w,0)==0:
            word_doc_dict[w]={}
            word_doc_dict[w][i]=1
        else:
            word_doc_dict[w][i]=word_doc_dict[w].get(i,0)
            word_doc_dict[w][i]+=1
    print(i)

with open("unique_words.txt",'w') as t:
    t.write(json.dumps(word_doc_dict)) 