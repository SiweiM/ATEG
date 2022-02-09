import pickle
import os
import sys

data_name = sys.argv[1]

for i in list(range(1,6)):
    test_n=i
    train_n=[j for j in range(1,6)]
    train_n.remove(test_n)

    data_dir='../dataset/'+data_name
    if not os.path.exists(data_name):
        os.mkdir(data_name)
    out_dir=data_name+'/fold'+str(test_n)+'/'
    if not os.path.exists(out_dir):
        os.mkdir(out_dir)
    
    with open(data_dir+'_subset'+str(test_n)+'_preprocessed.pickle','rb') as f:
        pickle_test=pickle.load(f)
        pickle.dump(pickle_test,open(out_dir+'test.pickle','wb'))
        with open(out_dir+'test.txt','w') as out:
            for sentence in pickle_test:
                out.write(sentence['prepro_text']+'\n')

    train_pickles=[]
    for train in train_n:
        subset=pickle.load(open(data_dir+'_subset'+str(train)+'_preprocessed.pickle','rb'))
        train_pickles=train_pickles+subset
    pickle.dump(train_pickles,open(out_dir+'train.pickle','wb'))
    with open(out_dir+'train.txt','w') as out:
        for sentence in train_pickles:
            out.write(sentence['prepro_text']+'\n')
    
    print('Fold'+str(test_n))
    print('test length=',len(pickle_test))
    print('train length=',len(train_pickles))

