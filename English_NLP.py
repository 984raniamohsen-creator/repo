# preprocessor.py
import re
import string
import nltk

# Downloads
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('averaged_perceptron_tagger')
nltk.download('wordnet')

from nltk import pos_tag, word_tokenize
from nltk.corpus import stopwords, wordnet
from nltk.stem import WordNetLemmatizer


class EnglishPreprocessor:
    def __init__(self):
        self.stopwords = set(stopwords.words("english"))
        self.lemmatizer = WordNetLemmatizer()

    # 1 — Lowercase
    def to_lower(self, text):
        return text.lower()

    # 2 — Remove punctuation
    def remove_punctuation(self, text):
        return text.translate(str.maketrans("", "", string.punctuation))

    # 3 — Remove numbers
    def remove_numbers(self, text):
        return re.sub(r"\d+", "", text)

    # 4 — Remove stopwords
    def remove_stopwords(self, text):
        tokens = text.split()
        tokens = [t for t in tokens if t not in self.stopwords]
        return " ".join(tokens)

    # 5 — Map POS tag to WordNet tag
    def get_wordnet_pos(self, tag):
        if tag.startswith('J'):
            return wordnet.ADJ
        elif tag.startswith('V'):
            return wordnet.VERB
        elif tag.startswith('N'):
            return wordnet.NOUN
        elif tag.startswith('R'):
            return wordnet.ADV
        else:
            return wordnet.NOUN

    # 6 — Lemmatization
    def lemmatize_sentence(self, sentence):
        tokens = nltk.word_tokenize(sentence)
        pos_tags = nltk.pos_tag(tokens)

        lemmas = [
            self.lemmatizer.lemmatize(word, self.get_wordnet_pos(pos))
            for word, pos in pos_tags
        ]
        return " ".join(lemmas)

    # 7 — Full preprocessing pipeline
    def preprocess(self, text):
        text = self.to_lower(text)
        text = self.remove_punctuation(text)
        text = self.remove_numbers(text)
        text = self.remove_stopwords(text)
        text = self.lemmatize_sentence(text)
        return text
