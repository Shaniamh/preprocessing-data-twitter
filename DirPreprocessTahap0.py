import re
import pandas as pd
import nltk
import csv
import glob


#PREPOCESSING INI MELIPUTI : NUMBER REMOVAL, HASHTAG, MENTION, URL, EMOTICON

def getNumberRemoval(text):
    # PREPROCESS - NUMBER REMOVAL
    text = re.sub(r'\d+', '', text)
    # print("Number removal: {}".format(text))
    return text
def getMentionLinkHashtagRemoval(text):
    # PREPROCESS - MENTION REMOVAL , LINK, HASHTAG sign REMOVAL
    text = re.sub(r'@\w+ ?|http\S+|#', '', text)
    # print("Mention, Link, hashtag sign removal: {}".format(text))
    return text
def getNTConversion(text):
    # PREPROCESS - n't conversion
    # text  = re.sub('n''t+$', " not", text)
    text = re.sub("n't\s*|don$", " not ", text)
    # print(" n't conversion: {}".format(text))
    return text
def getFivePreprocess(text):
    text = getNumberRemoval(text)  # PREPROCESS - NUMBER REMOVAL
    # PREPROCESS - PUNCTUATION REMOVAL (have done at prev preprocess)
    # text = text.translate(string ("", ""), string.punctuation)
    text = getMentionLinkHashtagRemoval(text)  # PREPROCESS - MENTION REMOVAL , LINK, HASHTAG sign REMOVAL
    text = getNTConversion(text)  # PREPROCESS - n't conversion
    # PREPROCESS - OVERWRITE (data dari DB sudah recognize by wordnet and corrected by textblob)
    # text = ''.join(''.join(s)[:] for _, s in itertools.groupby(text))
    #print(" get five preprocess : {}".format(text))
    return text

regex_str = [
    # r'<[^>]+>',  # HTML tags
    r'(?:@[\w_]+)',  # @-mentions
    r"(?:\#+[\w_]+[\w\'_\-]*[\w_]+)",  # hash-tags
    r'http[s]?://(?:[a-z]|[0-9]|[$-_@.&amp;+]|[!*\(\),]|(?:%[0-9a-f][0-9a-f]))+',  # URLs
    # r'(?:(?:\d+,?)+(?:\.?\d+)?)',  # numbers
    r"(?:[a-z][a-z'\-_]+[a-z])",  # words with - and '
    r'(?:[\w_]+)',  # other words
    # r'(?:\S)'  # anything else
]
tokens_re = re.compile(r'('+'|'.join(regex_str)+')', re.VERBOSE | re.IGNORECASE)

def tokenize(s):
    return tokens_re.findall(s)
#======merubah ke huruf kecil semua
def preprocess(param, lowercase=False):
    tokens = tokenize(param)
    if lowercase:
        tokens = [token.lower() for token in tokens]
    return tokens

def unicodetoascii(text):
    TEXT = (text.
            replace('\\xF0\\x9F\\x98\\x81', "joying ").
            replace('\\xF0\\x9F\\x98\\x82', "joying ").
            replace('\\xF0\\x9F\\x98\\x83', "joying ").
            replace('\\xF0\\x9F\\x98\\x84', "joying ").
            replace('\\xF0\\x9F\\x98\\x85', "joying ").
            replace('\\xF0\\x9F\\x98\\x86', "joying ").
            replace('\\xF0\\x9F\\x98\\x89', "joying ").
            replace('\\xF0\\x9F\\x98\\x8A', "joying ").
            replace('\\xF0\\x9F\\x98\\x8B', "joying ").
            replace('\\xF0\\x9F\\x98\\x8C', "relieved ").
            replace('\\xF0\\x9F\\x98\\x8D', "loving ").
            replace('\\xF0\\x9F\\x98\\x8F', "smirking ").
            replace('\\xF0\\x9F\\x98\\x92', "bored ").
            replace('\\xF0\\x9F\\x98\\x93', "bored ").
            replace('\\xF0\\x9F\\x98\\x94', "sad ").
            replace('\\xF0\\x9F\\x98\\x96', "sad ").
            replace('\\xF0\\x9F\\x98\\x98', "loving ").
            replace('\\xF0\\x9F\\x98\\x9A', "loving ").
            replace('\\xF0\\x9F\\x98\\x9C', "funny ").
            replace('\\xF0\\x9F\\x98\\x9D', "funny ").
            replace('\\xF0\\x9F\\x98\\x9E', "sad ").
            replace('\\xF0\\x9F\\x98\\xA0', "angry ").
            replace('\\xF0\\x9F\\x98\\xA1', "angry ").
            replace('\\xF0\\x9F\\x98\\xA2', "sad ").
            replace('\\xF0\\x9F\\x98\\xA3', "sad ").
            replace('\\xF0\\x9F\\x98\\xA4', "angry ").
            replace('\\xF0\\x9F\\x98\\xA5', "sad ").
            replace('\\xF0\\x9F\\x98\\xA8', "sad ").
            replace('\\xF0\\x9F\\x98\\xA9', "sad ").
            replace('\\xF0\\x9F\\x98\\xAA', "tired ").
            replace('\\xF0\\x9F\\x98\\xAB', "tired ").
            replace('\\xF0\\x9F\\x98\\xAD', "sad ").
            replace('\\xF0\\x9F\\x98\\xB0', "sad ").
            replace('\\xF0\\x9F\\x98\\xB1', "surprised ").
            replace('\\xF0\\x9F\\x98\\xB2', "surprised ").
            replace('\\xF0\\x9F\\x98\\xB3', "surprised ").
            replace('\\xF0\\x9F\\x98\\xB4', "surprised ").
            replace('\\xF0\\x9F\\x98\\xB7', "sick ").
            replace('\\xF0\\x9F\\x98\\xB8', "joying ").
            replace('\\xF0\\x9F\\x98\\xB9', "joying ").
            replace('\\xF0\\x9F\\x98\\xBA', "joying ").
            replace('\\xF0\\x9F\\x98\\xBB', "joying ").
            replace('\\xF0\\x9F\\x98\\xBC', "sad ").
            replace('\\xF0\\x9F\\x98\\xBD', "joying ").
            replace('\\xF0\\x9F\\x98\\xBE', "angry ").
            replace('\\xF0\\x9F\\x98\\xBF', "sad ").
            replace('\\xF0\\x9F\\x99\\x80', "surprised ").
            replace('\\xF0\\x9F\\x99\\x85', "deny ").
            replace('\\xF0\\x9F\\x99\\x86', "joying ").
            replace('\\xF0\\x9F\\x99\\x8F', "sorry ").

            replace('\\xf0\\x9f\\x91\\x8f', "clapping ").
            replace('\\xF0\\x9F\\x91\\x8C', "agree ").
            replace('\\xF0\\x9F\\x91\\x8D', "agree ").

            replace('\\xF0\\x9F\\x91\\x8E', "disagree ").

    		replace('\\xe2\\x80\\x99', "'").
            replace('\\xc3\\xa9', 'e').
            replace('\\xe2\\x80\\x90', '-').
            replace('\\xe2\\x80\\x91', '-').
            replace('\\xe2\\x80\\x92', '-').
            replace('\\xe2\\x80\\x93', '-').
            replace('\\xe2\\x80\\x94', '-').
            replace('\\xe2\\x80\\x94', '-').
            replace('\\xe2\\x80\\x98', "'").
            replace('\\xe2\\x80\\x9b', "'").
            replace('\\xe2\\x80\\x9c', '"').
            replace('\\xe2\\x80\\x9c', '"').
            replace('\\xe2\\x80\\x9d', '"').
            replace('\\xe2\\x80\\x9e', '"').
            replace('\\xe2\\x80\\x9f', '"').
            replace('\\xe2\\x80\\xa6', '...').#
            replace('\\xe2\\x80\\xb2', "'").
            replace('\\xe2\\x80\\xb3', "'").
            replace('\\xe2\\x80\\xb4', "'").
            replace('\\xe2\\x80\\xb5', "'").
            replace('\\xe2\\x80\\xb6', "'").
            replace('\\xe2\\x80\\xb7', "'").
            replace('\\xe2\\x81\\xba', "+").
            replace('\\xe2\\x81\\xbb', "-").
            replace('\\xe2\\x81\\xbc', "=").
            replace('\\xe2\\x81\\xbd', "(").
            replace('\\xe2\\x81\\xbe', ")").
            replace("b'", "").
            replace('b"', "").
            replace('\\xf\\xf\\x\\xc\\xf\\xf\\x\\xc', "").
            replace('\\xf\\xf\\x\\xd\\xf\\xf\\x\\xc', "").
            replace('\\xf\\xf\\x\\x\\xf\\xf\\x\\x\\xf\\xf\\x\\xc', "").
            replace('\\xf\\xf\\x\\xc',"").
            replace('\\xf\\xf\\x\\xd',"").
            replace('\\xf\\xf\\x\\xd',"").
            replace('\\xe\\x\\xa',"").
            replace('\\xe\\x\\xc', "").
            replace('\\xe\\xad\\x\\xe\\xad\\x', "").
            replace('\\xf\\xf\\x\\x',"").
            replace('\\xf\\xf\\xe\\x\\xf\\xf\\xe\\x',"").
            replace('\\xe\\x\\xd',"").
            replace('\\xe\\x\\xt',"").
            replace('\\xe\\x\\xs', "").
            replace('\\xe\\x\\xm', "").
            replace('\\xf\\xf\\xe\\x', "").
            replace('\\xe\\x\\xt', "").
            replace('\\xf\\xf\\xc\\xb', "").
            replace('\\xf\\xf\\xa\\xa', "").
            replace('\\xe\\x\\xre', "").
            replace('rt',"").
            replace('\\xf\\xf\\xd\\x\\xe\\xb\\x',"")
            )
    return TEXT

def readFolderCSV(dir):
    csvDir = glob.glob(dir + '/*.csv');
    filenamecsv = []
    i = 0;
    for file in csvDir:
        i=i+1
        nameOfFile = file
        space = nameOfFile.find(" ")
        file = nameOfFile[54:]
        file = nameOfFile[61:]
        num = nameOfFile[54:space]
        nameCSV = nameOfFile[space+1:]
        name = nameCSV[:-11]
        # print("{} | {} || : {} | {} | {}" .format(i, file, num, nameCSV, name))
        filenamecsv.append(nameOfFile)
    print(i)
    # 2214 records
    return filenamecsv

def cleansingCSVTweet(filename):
    print("will process", filename)
    namedir = filename[0:54]
    nameonly = filename[54:]
    nameNewDir = namedir + "result\\" + nameonly

    # df = pd.read_csv(os.path.join(os.path.dirname(__file__), filename))
    df = pd.read_csv(filename, encoding='latin-1')

    for f in range(df.shape[0]):
        alltext = df['text'][f]
      #  fiveprocess = getFivePreprocess(alltext)
        ascii = unicodetoascii(alltext)
        cleanByRegex = preprocess(ascii, True)
        #print(cleanByRegex)
        #===============TOKEN DIJADIKAN 1===============
        joinCleanTweet = ' '.join(cleanByRegex)
        data = joinCleanTweet
        print(f)
        df['text'][f] = data
    print(filename)
    df.to_csv(filename)

if __name__ == '__main__':
    dir = "C:\\userDepClean\\b\\new"
    resultDir = "C:\\userdepression\\result"
    fileNameCSVs = []
    fileNameCSVs = readFolderCSV(dir)
    for file in fileNameCSVs:
        print(file)
        clean = cleansingCSVTweet(file)
        counter = 0
        i = 0
    for file in clean:
        i = i + 1
       # print(i)
        nameonly = file[45:]
        #print(nameonly)
        if (i > 880):
            print(file)
            df = pd.read_csv(file, encoding='latin-1')
            if not df['text'].empty:
                if df['text'][0][0:1] != 'b':
                    print(nameonly)
                    isCleaned = True
                    df.to_csv(resultDir + '/' + nameonly)
                    print("yey")
                    counter = counter + 1
                    print(counter)

#print("BERHASIL MENYIMPAN FILE CSV")
