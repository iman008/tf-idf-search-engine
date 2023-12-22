# import required module
import sys
import string
import re
import os


from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer

import string

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


def custom_tokenizer(filename):
    f = open(filename, encoding="UTF8")
    text = f.read()
    list_words = re.split(r"\W+", str(text))
    f.close()
    tokens = [
        word
        for word in list_words
        if (word.isalpha() or w.replace(".", "").isdigit())
        and len(word) > 1
        and word.lower() not in stopwords_english
    ]
    return tokens


def compute_tfidf(documents):
    vectorizer = TfidfVectorizer(tokenizer=custom_tokenizer)

    tfidf_matrix = vectorizer.fit_transform(documents)

    return tfidf_matrix, vectorizer


def match_document(tfidf_matrix, query, vectorizer):
    query_vector = vectorizer.transform([query])

    similarities = cosine_similarity(tfidf_matrix, query_vector)

    best_match_index = similarities.argmax()

    return best_match_index


# send form iman and find it
documents = []

# from server
query = ""

tfidf_matrix, vectorizer = compute_tfidf(documents)
best_match_index = match_document(tfidf_matrix, query, vectorizer)

print(f"match paragraph: {documents[best_match_index]}")
