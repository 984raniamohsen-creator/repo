NLP Preprocessing for Arabic & English

Python library for text preprocessing in English and Arabic, including cleaning, normalization, tokenization, stopword removal, lemmatization, and stemming.

Features

English (preprocessor.py)

Lowercasing, punctuation & number removal

Stopwords removal

Lemmatization (NLTK WordNet)

Full preprocessing pipeline

Arabic (arabic_nlp.py)

Cleaning & normalization (Alef, Teh Marbuta)

Tokenization

Stopwords removal

Stemming (ISRI Stemmer)

Right-to-Left (RTL) reshaping

Full preprocessing pipeline

Installation
git clone https://github.com/YOUR_USERNAME/YOUR_REPO.git
cd YOUR_REPO
pip install nltk camel-tools arabic-reshaper python-bidi


Download NLTK resources:

import nltk
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('averaged_perceptron_tagger')
nltk.download('wordnet')

Usage

English

from preprocessor import EnglishPreprocessor

text = "The cats are running on the 3 streets!"
preprocessor = EnglishPreprocessor()
print(preprocessor.preprocess(text))


Arabic

from arabic_nlp import ArabicNLP

text = "أنا بحب و البرمجة"
nlp = ArabicNLP("arabic")
print(nlp.preprocess(text, "LTR"))  # Left-to-right
print(nlp.preprocess(text, "RTL"))  # Right-to-left
