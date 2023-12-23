import sys
import string
import re
import os
import math
from collections import Counter

stopwords_english = set(
    [
        "shouldn",
        "you'd",
        "their",
        "after",
        "up",
        "that'll",
        "herself",
        "won't",
        "wouldn",
        "why",
        "myself",
        "weren't",
        "do",
        "until",
        "needn't",
        "or",
        "will",
        "here",
        "there",
        "mightn't",
        "in",
        "me",
        "she's",
        "these",
        "was",
        "being",
        "couldn",
        "won",
        "not",
        "isn't",
        "by",
        "now",
        "you've",
        "hadn",
        "its",
        "been",
        "above",
        "few",
        "it",
        "then",
        "other",
        "didn",
        "during",
        "while",
        "shan't",
        "ll",
        "had",
        "it's",
        "about",
        "out",
        "from",
        "wasn",
        "did",
        "yourselves",
        "hasn",
        "hasn't",
        "again",
        "down",
        "doesn",
        "doesn't",
        "into",
        "what",
        "wasn't",
        "does",
        "some",
        "with",
        "where",
        "should",
        "shouldn't",
        "is",
        "to",
        "itself",
        "under",
        "has",
        "y",
        "we",
        "just",
        "same",
        "ourselves",
        "she",
        "don't",
        "yourself",
        "am",
        "further",
        "isn",
        "didn't",
        "haven't",
        "themselves",
        "aren't",
        "needn",
        "between",
        "o",
        "because",
        "more",
        "d",
        "an",
        "all",
        "be",
        "our",
        "hadn't",
        "theirs",
        "having",
        "haven",
        "wouldn't",
        "shan",
        "than",
        "of",
        "so",
        "most",
        "hers",
        "no",
        "mightn",
        "such",
        "t",
        "both",
        "are",
        "they",
        "which",
        "through",
        "over",
        "you'll",
        "those",
        "have",
        "i",
        "and",
        "for",
        "how",
        "nor",
        "but",
        "you",
        "the",
        "when",
        "each",
        "ve",
        "before",
        "ain",
        "ours",
        "aren",
        "that",
        "you're",
        "don",
        "at",
        "s",
        "your",
        "his",
        "once",
        "my",
        "any",
        "should've",
        "them",
        "if",
        "below",
        "m",
        "mustn",
        "very",
        "as",
        "this",
        "mustn't",
        "who",
        "weren",
        "can",
        "off",
        "him",
        "himself",
        "couldn't",
        "a",
        "own",
        "were",
        "whom",
        "ma",
        "yours",
        "only",
        "re",
        "on",
        "doing",
        "too",
        "against",
        "her",
        "he",
    ]
)

def custom_tokenizer(text):
    list_words = re.split(r"\W+", str(text))
    tokens = [
        word
        for word in list_words
        if (word.isalpha() or word.replace(".", "").isdigit())
        and len(word) > 1
        and word.lower() not in stopwords_english
    ]
    return tokens

def custom_tfidfvectorizer(documents):
    tokenized_documents = [custom_tokenizer(doc) for doc in documents]

    vocabulary = set(word for doc in tokenized_documents for word in doc)

    tf_documents = [{word: doc.count(word) / len(doc) for word in doc} for doc in tokenized_documents]

    document_frequency = Counter(word for doc in tokenized_documents for word in set(doc))
    idf = {word: math.log(len(documents) / (1 + document_frequency[word])) for word in vocabulary}

    tfidf_documents = [{word: tf * idf[word] for word, tf in tf_doc.items()} for tf_doc in tf_documents]

    return tfidf_documents, list(vocabulary)

def custom_cosine_similarity(vector1, vector2):
    dot_product = sum(vector1[word] * vector2[word] for word in vector1 if word in vector2)
    magnitude1 = math.sqrt(sum(value**2 for value in vector1.values()))
    magnitude2 = math.sqrt(sum(value**2 for value in vector2.values()))

    if magnitude1 == 0 or magnitude2 == 0:
        return 0

    return dot_product / (magnitude1 * magnitude2)

def find_best_match_paragraph(query, doc_text):
    paragraphs = doc_text.split("\n")
    paragraphs += [query]

    tfidf_documents, vocabulary = custom_tfidfvectorizer(paragraphs)

    query_vector = {word: query.count(word) / len(query) * idf for word, idf in zip(vocabulary, tfidf_documents[-1].values())}
    
    similarities = [custom_cosine_similarity(query_vector, doc_vector) for doc_vector in tfidf_documents[:-1]]
    best_match_index = similarities.index(max(similarities))

    return best_match_index

