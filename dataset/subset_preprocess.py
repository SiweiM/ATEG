import pickle
import re
import nltk
import sys
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import CountVectorizer


data_path = 'amazon_'+sys.argv[1]

subj_words = ['i', 'me', 'my', 'mine', 'myself', 'we', 'us', 'our', 'ours', 'ourselves']
noun_taggers = ['NN', 'NNP', 'NNPS', 'NNS']
adj_taggers = ['JJ', 'JJR', 'JJS']

def get_sentences(string):
    string = re.sub('[:?!\n]', '.', string)
    sentences = [sent.strip() for sent in string.split('.') if sent.strip() != '']
    return sentences

def get_sentence_attr(string):
    subj_num = 0
    noun_num = 0
    adj_num = 0
    words = string.lower().split()
    w_t_list = nltk.pos_tag(words)
    for (w, t) in w_t_list:
        if w in subj_words:
            subj_num += 1
        if t in noun_taggers:
            noun_num += 1
        if t in adj_taggers:
            adj_num += 1
    return subj_num, noun_num, adj_num
	
def parseSentence(line):
    lmtzr = WordNetLemmatizer()
    stop = stopwords.words('english')
    text_token = CountVectorizer().build_tokenizer()(line.lower())
    text_rmstop = [i for i in text_token if i not in stop]
    text_stem = [lmtzr.lemmatize(w) for w in text_rmstop]
    return text_stem
	
for i in list(range(1,6)):
    file_name=data_path+'_subset'+str(i)
    subset=pickle.load(open(file_name+'.pickle','rb'))
    sentences=[]
    for idx,review in enumerate(subset):
        text=review['text']
        sents=get_sentences(text)
        for sent in sents:
            subj_n,noun_n,adj_n=get_sentence_attr(sent)
            if subj_n>0: #filter out subjective sentence
                continue
            if noun_n<1 or adj_n<1: #filter out no meaningful sentence
                continue

            tokens = parseSentence(sent)
            if len(tokens)>0:
                preprocessed_text=' '.join(tokens)
                sentence={
                    'subset':i,
                    'review_idx':idx,
                    'user': review['user'],
                    'item': review['item'],
                    'rating': review['rating'],
                    'verified': review['verified'],
                    'helpful':review['helpful'],
                    'sentence':sent,
                    'prepro_text':preprocessed_text
                }
                sentences.append(sentence)
    pickle.dump(sentences,open(file_name+'_preprocessed.pickle','wb'))