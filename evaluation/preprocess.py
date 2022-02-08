import pandas as pd
import argparse
import os
import pickle

parser = argparse.ArgumentParser()
parser.add_argument('-f',"--fold", dest="fold", type=int, metavar='<int>', default=1,
                    help="Number of fold (default=1)")
parser.add_argument("-as", "--aspect-size", dest="aspect_size", type=int, metavar='<int>', default=10,
                    help="The number of aspects specified by users (default=10)")
parser.add_argument('-d',"--dataset", dest="dataset", type=str, metavar='<str>', default='amazon_All_Beauty_5',
                    help="Name of dataset (default=amazon_All_Beauty_5)")
args = parser.parse_args()

print('----------reading data-------------')
data_dir="../preprocessed_data/"+args.dataset+"/fold"+str(args.fold) #open train dataset
train=pickle.load(open(data_dir+'/train.pickle','rb'))

test=pickle.load(open('../dataset/'+args.dataset+'_subset'+str(args.fold)+".pickle",'rb'))

labels_dir="../output/"+args.dataset+"_"+str(args.aspect_size)+"/fold"+str(args.fold)
with open(labels_dir+'/labels.txt') as labels:
    count=0
    for aspect in labels.readlines():
        train[count]['aspect']=int(aspect)

print('----------saving data-------------')
output_dir="fold"+str(args.fold)+"/"
if not os.path.exists(output_dir):
    os.mkdir(output_dir)
pickle.dump(train,open(output_dir+"train_with_aspects.pickle",'wb'))
pickle.dump(test,open(output_dir+"test_set.pickle",'wb'))