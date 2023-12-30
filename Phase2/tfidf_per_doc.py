from tokenizer import tokenizer
import math
import pickle
from tqdm import tqdm
import numpy as np
from collections import defaultdict
from scipy.sparse import lil_matrix
import gzip

docsPath = "../data/"
numdocs = 10000


def generate_word_doc_dict():
    word_doc_dict = defaultdict(lambda: defaultdict(int))
    for i in tqdm(range(numdocs), desc="Generating word list"):
        filename = f"document_{i}.txt"
        list_words = tokenizer(docsPath + filename)
        for w in list_words:
            word_doc_dict[w][i] += 1
    return word_doc_dict


def calculate_tfidf(word_doc_dict):
    tfidf_per_doc = {}
    for i in tqdm(range(numdocs), desc="Calculating TF-IDF"):
        tfidf_per_doc[i] = {}
        filepath = f"../data/document_{i}.txt"
        tokens = tokenizer(filepath)
        di = len(tokens)
        for x in tokens:
            if x in word_doc_dict:
                tf = word_doc_dict[x][i] / di
                idf = math.log10(numdocs / len(word_doc_dict[x]))
                tfidf_per_doc[i][x] = tf * idf

        s = tfidf_per_doc[i]
        tfidf_per_doc[i] = dict(sorted(s.items(), key=lambda t: t[1], reverse=True))

    return tfidf_per_doc


def create_sparse_matrix(tfidf_per_doc, all_unique_words):
    word_index_mapping = {word: index for index, word in enumerate(all_unique_words)}
    tfidf_matrices = lil_matrix((numdocs, len(all_unique_words)))

    for i, doc_name in enumerate(
        tqdm(tfidf_per_doc.keys(), desc="Processing documents")
    ):
        word_indices = [word_index_mapping[word] for word in tfidf_per_doc[doc_name]]
        tfidf_values = np.fromiter(tfidf_per_doc[doc_name].values(), dtype=float)

        tfidf_matrices[i, word_indices] = tfidf_values

    return tfidf_matrices


def save_tfidf_to_file(tfidf_matrices, filename):
    with gzip.open(filename, "wb") as file:
        pickle.dump(tfidf_matrices, file)


word_doc_dict = generate_word_doc_dict()
tfidf_per_doc = calculate_tfidf(word_doc_dict)
all_unique_words = sorted(set(word for doc in tfidf_per_doc.values() for word in doc))
tfidf_matrices = create_sparse_matrix(tfidf_per_doc, all_unique_words)
save_tfidf_to_file(tfidf_matrices, "tfidf_per_doc.pkl.gz")
