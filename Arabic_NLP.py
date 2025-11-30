import re
from camel_tools.utils.normalize import normalize_alef_maksura_ar, normalize_teh_marbuta_ar
import arabic_reshaper
from bidi.algorithm import get_display
from nltk.stem.isri import ISRIStemmer


class ArabicNLP:
    def __init__(self, language):
        self.language = language

        # Stopwords
        self.stopwords = set([
            "في","من","على","و","عن","إلى","ما","لم","لن","إن","أن",
            "كان","كانت","هذا","هذه","ذلك","هناك","هنا","هو","هي","هم","هن"
        ])

        # Stemmer
        self.stemmer = ISRIStemmer()

    # reshape ONLY for display
    def reshape_for_display(self, text):
        reshaped = arabic_reshaper.reshape(text)
        rtl_text = get_display(reshaped)
        return rtl_text

    # Step 1 — Basic cleaning
    def basic_clean(self, text,case):
        text = re.sub(r'[\u064B-\u0652]', '', text)
        text = re.sub('[إأآا]', 'ا', text)
        text = re.sub(r'[^ء-ي ]', ' ', text)
        text = re.sub(r'\s+', ' ', text).strip()
        if case=="LTR":
            
          return text  # مهم 
    
        elif case=="RTL":
            return self.reshape_for_display(text)

    # Step 2 — Normalize
    def normalize(self, text,case):
        text = normalize_alef_maksura_ar(text)
        text = normalize_teh_marbuta_ar(text)
        if case=="LTR":
            
          return text  # مهم 
    
        elif case=="RTL":
            return self.reshape_for_display(text)

    
    

    # Step 3 — Tokenize
    def tokenize(self, text,case):
        
        if case=="LTR":
            
          return text.split() # مهم 
    
        elif case=="RTL":
            return self.reshape_for_display(text).split()

        

    # Step 4 — Remove stopwords
    def remove_stopwords(self,text,case):
        
        
        tokens=self.tokenize(text,'LTR')
        pure_tokens =[t for t in tokens if t not in self.stopwords] 
        if case=="LTR":
          
          
          return (' '.join(pure_tokens))  # مهم 
    
        elif case=="RTL":
          return self.reshape_for_display(' '.join(pure_tokens))
        
        

    # Step 5 — Stemming
    def stem(self, text,case):
        stemmed_tokens= [self.stemmer.stem(t) for t in text.split()]
        if case =="RTL":
          return self.reshape_for_display(' '.join(stemmed_tokens))
        elif case =="LTR":
           return ' '.join(stemmed_tokens)


    # FINAL PIPELINE
    def preprocess(self, text,case):
        text = self.basic_clean(text,"LTR")
        text = self.normalize(text,"LTR")
        text = self.remove_stopwords(text,"LTR")
        text = self.stem(text,"LTR")
        if case =="LTR":
           return text
        elif case=="RTL":
           return(self.reshape_for_display(text))


# ---------------- Test ----------------
nlp = ArabicNLP("arabic")
text = "أنا بحب و البرمجة"

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