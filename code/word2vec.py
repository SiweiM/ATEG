#!/usr/bin/env python
#  -*- coding: utf-8  -*-

import gensim
import codecs
import sys

class Sentences(object):
    def __init__(self, filename):
        self.filename = filename

    def __iter__(self):
        for line in codecs.open(self.filename, 'r', 'utf-8'):
            yield line.split()


def main(n):
    dataset=sys.argv[1]
    source = '../preprocessed_data/'+dataset+'/fold'+str(n)+'/train.txt'
    model_file = '../preprocessed_data/'+dataset+'/fold'+str(n)+'/w2v_embedding'
    sentences = Sentences(source)
    model = gensim.models.Word2Vec(sentences, size=200, window=5, min_count=10, workers=4, sg=1, iter=2)
    model.save(model_file)

if __name__ == "__main__":
    for n in list(range(1,6)):
        print('Pre-training word embeddings for fold '+str(n))
        main(n)
