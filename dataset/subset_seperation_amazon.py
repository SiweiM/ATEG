import pickle
import gzip
import sys
import random
from bs4 import BeautifulSoup

data = sys.argv[1]+"_5.json.gz"
reviews_data = 'amazon_'+sys.argv[1]
  
global false,null,true
false=False
null=None
true=True

reviews=[]
for line in gzip.open(data,'r'):
    review=eval(line)
    text=''
    if 'summary' in review:
        text+=review['summary']+'\n'
    if 'reviewText' in review:
        text+=review['reviewText']
    if '</' in text:  # wash the review with html contents
        text = BeautifulSoup(text,features='html.parser').get_text()
    if text=='':
        continue
    
    json_doc={
              'user':review['reviewerID'],
              'item': review['asin'],
              'rating': int(review['overall']),
              'text': text,
              'verified':review['verified'],
              }
    if 'vote' in review:
        json_doc['helpful']=review['vote']
    else:
        json_doc['helpful']=0
    reviews.append(json_doc)

random.shuffle(reviews)
pickle.dump(reviews,open(reviews_data+'.pickle','wb'))
i=len(reviews)//5
for j in range(5):
    subset=reviews[j*i:(j+1)*i]
    pickle.dump(subset,open(reviews_data+'_subset'+str(j+1)+'.pickle','wb'))