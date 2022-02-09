# Aspect-based Textual Explanation Generation System
---
Part of codes refer the codes from [Ruidan's paper](https://github.com/ruidan/Unsupervised-Aspect-Extraction)
## Data preprocessing
Datasets are from [Amazon product data](https://nijianmo.github.io/amazon/index.html)
The datasets used in the experiment are in dataset folder.

For preprocessing, please run the codes respectively in dataset/.
```
python subset_seperation_amazon.py $dataset_name
python subset_preprocess.py $dataset_name
```
The preprocessed pickle files for each fold will be saved in the same folder.

After this, please run the code in preprocessed_data/.
```
python transform_txt.py $pickle_file_name_before_'_subset'
```
The txt files for each fold experiment will be saved in folders under preprocessed_data/$pickle_file_name/.

## Aspect extraction
Before aspect extraction, you need to generate the word embeddings first. Under code/, please run
```
python word2vec.py $pickle_file_name_before_'_subset'
```
The trained word embeddings are saved in preprocessed_data/fold(1-5).
After this, please type
```
python train.py --emb ../preprocessed_data/$pickle_file_name/fold$fold_number/w2v_embedding -f $fold_number -as $number_of_aspect -d $pickle_file_name
```

where *$fold_number* should between 1 to 5. Also please change *$output_dir*, *$number_of_aspect* and *$pickle_file_name* to what you want.

Then, please type
```
python evaluation.py --emb ../preprocessed_data/$pickle_file_name/fold$fold_number/w2v_embedding -f $fold_number -as $number_of_aspect -d $pickle_file_name
```
This will output the file *aspect.log* which contains the top representative words of each aspects, *labels.txt* which contains the labels that assign the sentences in train set to different aspects.

## Explanation generation & evaluation
To generate the explanation, please run the code under evaluation/:
```
python preprocess.py -f $fold_number -as $number_of_aspect -d $pickle_file_name
```
## The part after here is under implement, this part is not uploaded to github

```
python generation.py -f $fold_number
```
You may need to change the direct of *labels.txt* in *preprocess.py*.
After this, the generated explanations(including the explanations generated from random-based mehtod and popular-based method) will be saved in evaluation/fold_number/.

For evaluation, you can run the codes under evaluation/:
```
python wmdistance.py -f $fold_number 
python similarity.py -f $fold_number 
```
It will return the word mover's distance score and semantic textual similarity score of the experiment.

## Dependencies
Python 3.6
* keras <2.3
* tensorflow<1.10
* gensim<3.6
* numpy<1.16
* scikit-learn
* tqdm
* h5py
* nltk
* pandas
* gzip
* bs4
* pickle
* sklearn
