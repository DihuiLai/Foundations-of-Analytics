
import spacy
import pandas as pd
import nltk
nlp = spacy.load("en_core_web_sm")
nltk.download('averaged_perceptron_tagger')
mt=pd.read_csv("mtsamples.csv")
with open(filename, ) as file: # Use file to refer to the file object
   content_txt=file.read()

doc = nlp(mt["transcription"][0])
print(doc.text)
for token in doc:
    print(token.text, token.ent_type_, token.ent_iob_,)


from gensim.models import KeyedVectors
# Load vectors directly from the file
model = KeyedVectors.load_word2vec_format("wikipedia-pubmed-and-PMC-w2v.bin", binary=True)
# Access vectors for specific words with a keyed lookup:

model.word_vec("weeks")
model.similarity('osteochondrodysplasias', 'osteochondrodysplasia')
model["Hajdu-Cheney"]-model["Hajdu-Cheney"]

model.most_similar('osteochondrodysplasias')

model.similarity('dysplasia', 'Spondyloenchondrodysplasia')


text = nltk.word_tokenize(mt["transcription"][0])
nltk.pos_tag(text)


for token in doc:
    print(token.text)


doc=nlp("Non-Hodgkin lymphoma, unspecified, extranodal and solid organ sites")
print(doc.text)
for token in doc:
    print(token.text)


from fuzzywuzzy import fuzz

import difflib
print (fuzz.ratio("Poisoning by antineoplastic and immunosuppressive drugs, accidental (unintentional), initial encounter"))
difflib.SequenceMatcher(None, "this is a test", "www s t").ratio()


import numpy as np
def simiarity(word1, word2):
    return np.dot(word1, word2)/np.sqrt(np.dot(word1, word1))/np.sqrt(np.dot(word2, word2))



doc1=nlp("dysplasia")
doc2=nlp("diaphyseal")

print (simiarity(doc1[0].vector, doc2[0].vector))


import numpy as np
ICD_LIST=
SNOW_LIST=
Match_Matrix=map(lambda ICDcode, SNOWcode: np.multiply(x[ICDode], y[SNOWcode]), ICD_LIST, SNOW_LIST)


def addition(n):
    return n + n


# We double all numbers using map()
numbers = (1, 2, 3, 4)
result = map(lambda y: 2*y, numbers)
print(list(result))