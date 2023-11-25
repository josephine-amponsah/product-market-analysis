from textblob import TextBlob, Word
from nltk.util import ngrams
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
stop = set(stopwords.words('english'))
import re


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
        words = re.sub(r'[^a-zA-Z0-9\s]', '', str(sent))
        words = words.lower()
        line = word_tokenize(words)
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

def ngram_tokenizer(sent):
    # output = []
    unigrams = []
    words = re.sub(r'[^a-zA-Z0-9\s]', '', str(sent))
    words = words.lower()
    line = word_tokenize(words)
    new_line = remove_stopwords(line)
    unigrams.append(new_line)
    # output.extend(unigrams)
    bigrams = []
    tokens = words.split()
    bigram= list(ngrams(tokens, 2))
    new_item = [" ".join(token) for token in bigram]
    bigrams.append(new_item)
    # output.extend(bigrams)
    output = unigrams + bigrams
    return output
map_dict = {"Fitness": ["workout", "weight loss", "lose weight", "exercise", "exercising", "gym", "fitness", "pedometer", "step counter", "fit", "walking",
                        "running", "daily step", "cardio", "pilate", "boxing", "bodybuiling", "hiit", "stretch", "trainer", "trackerstep",
                        "workouts", "steps", "active","hiking","step", "sports","hikes"],
            "Nutrition":["diet", "calorie","intermittent fasting", "recipe", "nutrition", "calorie counter", "food", "meal plan", "menu planner", "water","vegan",
                         "water tracker"],
            "Wellness" : ["stress", "selfcare", "meditation", "calm", "yoga", "mindfulness", "anxiety", "menstrual", "ovulation", "anxiety", "relax",
                          "relaxation", "smoking", "wellbeing", "sleep", "music", "depression", "motivation", "therapy", "therapist", "smokefree",
                          "routine", "couple", "menstruations", "mood", "companion","period","friend","habits","moods","positive","personal care",
                          "addiction","wellness","pregnancy","therapists"],
            "Health Monitoring": ["blood pressure", "heart rate", "pulse", "blood sugar", "diabetes", "bmi", "health","glucose","data","prescription",
                                  "doctor"]
            }
def tokenize_summary(text):
    singles = ngram_tokenizer(text)
    multigrams = [item for sublist in singles for item in sublist]
    return multigrams

def assign_subgenre(text):
    tokens = tokenize_summary(text)
    for subgenre, keywords in map_dict.items():
        if any(keyword in tokens for keyword in keywords):
            return subgenre
    return None