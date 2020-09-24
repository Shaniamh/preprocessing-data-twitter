import pandas as pd
import nltk
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import WordPunctTokenizer
from nltk.corpus import wordnet
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords
stop_words =set(stopwords.words('english'))
from spacy.tokens import Doc
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.stem.wordnet import WordNetLemmatizer
from nltk import word_tokenize, pos_tag
from nltk.corpus import wordnet
from collections import defaultdict
from nltk.corpus import stopwords
from textblob import TextBlob

sent_analyzer = SentimentIntensityAnalyzer()
tag_map = defaultdict(lambda : wordnet.NOUN)
tag_map['J'] = wordnet.ADJ
tag_map['V'] = wordnet.VERB
tag_map['R'] = wordnet.ADV
wn_lemmater = WordNetLemmatizer()
stop_words =set(stopwords.words('english'))

#===================KEBUTUHAN STOPWORD==============
self_words = ['my', 'myself', 'i', "i'", 'self', 'am', 'me', 'id', "i'd", "'d", "ain", "ain't",
              "i'll", 'im', "i'm", "ive","i've",
              "mine", "own", 'myselves', 'ourselves', "'ve"]
negation_words = ['no', 'not', 'mustn', "wouldn't", "aren't", "hasn't", 'wasn', 'don',
                      "isn't", 'won', "won't", "didn't", "couldn't", "weren't", 'nor', 'neither', "'t"]

def updateStopWords(stop_words):
    to_extend = ['x', 'y', 'r', 'e', 's', 'm', 'hi', 'yet', 'may', 'oh', 'due', 'to',
                 'day', 'days', 'weeks', 'week','b', 'c', 'f', 'n', 'xde', 'co', 'xad',
                 'being', 'months', 'way', 'wa', 'xe', 'xa', 'xb', 'xef', 'xf', 'xd', 'xba', 'xbb', 'xbc', 'xef', 'xc', 'xll','rt']
    stop_words = stop_words.union(to_extend)

    #print(stop_words)
    to_remove = ['instead']
    stop_words = stop_words.difference(to_remove)
    stop_words = stop_words.difference(self_words)
    stop_words = stop_words.difference(negation_words)
    #print("STOP WORD BARU : {}".format(stop_words))
    return  stop_words
def tokenize(text):
    text = nltk.word_tokenize(text)
    return text

if __name__ == '__main__':
    #==========Baca file csv===================
    df = pd.read_csv(r'userNormal/2177 TheRealPuce_tweets.csv', encoding='latin-1')
    #PRINT DATA
    #print(df)
    only_recognized_words = []
    for f in range(df.shape[0]):
        alltext = df['text'][f]
        #=========Tokenizing============
        tokens = tokenize(alltext)
        #print(tokens)
        lemma2 = []
        token_2 = []
        for token, tag in pos_tag(tokens):
            lemma = wn_lemmater.lemmatize(token, tag_map[tag[0]])
            token_2.append(token)
            lemma2.append(lemma)
        filtered_sentence = []
        sentence = []
        stopword = []
        sw = updateStopWords(stop_words)
        stopword.append(sw)
        for l in lemma2:
            for s in stopword:
                if l not in s:
                    filtered_sentence.append(l)

        #text = ' '.join(filtered_sentence)
        print(filtered_sentence)
        #df['text'][f] = filtered_sentence
        join = ' '.join(filtered_sentence)
        df['text'][f] = join

    print("BERHASIL MENYIMPAN FILE CSV")
    df.to_csv(r'E:\1 DATA KULIAH\D4 IT B SEMESTER 7\TUGAS AKHIR\DATA PROCESSING SHANIA\USER\2177 TheRealPuce_tweets.csv',
              index=None, header=True)
    #stop = updateStopWords(stop_words)
    #print(stopword)

