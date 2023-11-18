from textblob import TextBlob, Word
from nltk.util import ngrams
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
stop = set(stopwords.words('english'))


def remove_stopwords(tokens):
    # sourcery skip: inline-immediately-returned-variable, list-comprehension
    filtered = []
    for word in tokens:
        if word not in stop:
            filtered.append(word)
    return filtered


def lemmatizer(sent_list):
    lemmatized_tokens = []
    for sent in sent_list:
        lemma_tokens = [Word(word).lemmatize() for word in sent]
        lemmatized_tokens.append(lemma_tokens)
    return lemmatized_tokens


def unigram_tokenizer(sent_list):
    unigram_tokens = []
    for sent in sent_list:
        line = word_tokenize(sent)
        new_line = remove_stopwords(line)
        unigram_tokens.append(new_line)
    return lemmatizer(unigram_tokens)


def bigram_tokenizer(sent_list):
    # sourcery skip: for-append-to-extend, identity-comprehension, inline-immediately-returned-variable, list-comprehension, simplify-generator
    bigram_tokens = []
    tokenized_data = unigram_tokenizer(sent_list)
    for item in tokenized_data:
        bigrams = list(ngrams(item, 2))
        new_item = [" ".join(token) for token in bigrams]
        bigram_tokens.append(new_item)
    return bigram_tokens