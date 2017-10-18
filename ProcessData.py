import string
import nltk
from nltk.corpus import stopwords
# We keep negation words in stop words
# stopwords = [var for var in stopwords.words('english') if var not in ['not', 'isn']]
# stopwords.append('a')
stopwords = [l.split('\n')[0] for l in open('smartStopwords.txt')]
# print stopwords
# Stemming
sno = nltk.stem.SnowballStemmer('english')
endSentence = ';!?,)('
translateEndSentence = '...   '
dictForOverspan = {}
for i in endSentence:
    dictForOverspan[i] = '.'
def PreprocessFile(fileName):
    doc_labels = [l.split('\t')[0] for l in open(fileName)]
    doc_sents  = [l.split('\t')[1].strip().translate(string.maketrans('\n',' ')) for l in open(fileName)]
    return doc_labels,doc_sents

def ProcessDoc(inputDoc):
    # inputDoc: String
    # return tokenized,stemmed list of list of words
    output = []
    # inputDoc = str(inputDoc).strip().translate(string.maketrans(',', ' '))
    inputDoc = str(inputDoc).strip().translate(string.maketrans(endSentence,translateEndSentence))
    inputDoc += '.'
    for sentence in inputDoc.split('.')[:-1]:
        output.append([sno.stem(i) for i in nltk.word_tokenize(str(sentence.lower())) if i not in stopwords])
    # print output
    return output