from Arabic_NLP import ArabicNLP
nlp = ArabicNLP("arabic")
text = "أنا بحب انام والعب"
import nltk

nltk.download('wordnet')
nltk.download('omw-1.4')
nltk.download('stopwords')

nltk.download('stopwords')
print(nlp.basic_clean(text,'LTR'))


print(nlp.tokenize(text,"RTL"))
print(nlp.tokenize(text,"LTR"))
print(nlp.remove_stopwords(text,"RTL"))
print(nlp.remove_stopwords(text,"LTR"))
print(nlp.stem(text,'RTL'))
print(nlp.stem(text,'LTR'))

# Display RTL
#print("RTL Output:", nlp.reshape_for_display(text))
print('Preprocessed text is',nlp.preprocess(text,"RTL"))
print('Preprocessed text is',nlp.preprocess(text,"LTR"))

from English_NLP import EnglishPreprocessor

processor = EnglishPreprocessor()

sentence = "Cats were running faster than dogs in 2023!"

cleaned = processor.preprocess(sentence)

print("Original:", sentence)
print("Cleaned:", cleaned)