# AI Class Project: CSUF Portal Bot
# Peter Bergeon, Brian Edwards, Ryan Romero

# ----- Libraries -----
import json
import pickle
import numpy as np
import nltk
from nltk.stem import WordNetLemmatizer

# ----- Setup -----
# nltk_path = os.environ.get("NLTK_ROOT", '~/nltk_data/')
# nltk.data.path.append(nltk_path)
lemmatizer = WordNetLemmatizer()

with open("intents.json") as file:
    data = json.load(file)

words = pickle.load(open("words.pkl", "rb"))
topics = pickle.load(open("topics.pkl", "rb"))


# ----- Helper Functions -----

# clean_up_sentences:
#       lowercase and stems(root) user's string
def clean_up_sentences(userString):
    sentence = nltk.word_tokenize(userString)
    sentence = [lemmatizer.lemmatize(word.lower()) for word in sentence]
    return sentence

# bag_of_words:
#       convert user's string to a bag-of-words. A list of 0s and 1s that indiciate
#       if a word exist in the complete-list-of-words saved in training.py


def bag_of_words(userString):
    sentence = clean_up_sentences(userString)
    bag = [0] * len(words)
    for w in sentence:
        for i, word in enumerate(words):
            if word == w:
                bag[i] = 1

    return bag
    # return np.array(bag)

