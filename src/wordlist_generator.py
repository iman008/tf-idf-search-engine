from tokenizer import tokenizer
from tqdm import tqdm
import numpy as np
from collections import defaultdict
import json
docsPath = "../data/"
numdocs = 50001

def generate_word_doc_dict():
    word_doc_dict = defaultdict(lambda: defaultdict(int))
    for i in tqdm(range(numdocs), desc="Generating word list"):
        filename = f"document_{i}.txt"
        list_words = tokenizer(docsPath + filename)
        for w in list_words:
            word_doc_dict[w][i] += 1
    with open("unique_words.txt",'w') as t:
        t.write(json.dumps(word_doc_dict)) 
    return word_doc_dict


    



generate_word_doc_dict()