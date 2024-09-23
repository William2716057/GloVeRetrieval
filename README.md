# GloVe Twitter Word Vector Analyzer

This script demonstrates the usage of the GloVe Twitter-25 word embedding model for analyzing word vectors and their relationships. It allows users to compute the vector difference between two words and find word analogies using the GloVe model.

## Features
- Vector Difference Calculation: Input two words and compute the difference between their word vectors.
- Word Analogies: Find analogies using word relationships in the form word1 : word2 :: word3 :

## Requirements
- Python 3.x
- gensim library

## Installation
1. Clone the repository:
```
https://github.com/William2716057/GloVeRetrieval.git
```
2. Install dependencies:
```
pip install gensim
```

How to Use
1. Run the script:
```
python3 gloveTwittorVectors.py
```
2. Calculate Vector Difference:
- The script prompts you to enter two words.
- If both words are found in the GloVe Twitter-25 model, it will display their vectors and compute the difference between them.

3. Find word analogies
- After calculating the vector difference, the script automatically attempts to find an analogy where the input words serve as the basis of the relationship.
- For example, given king : queen :: man : ?, the script will find the word that best completes the analogy.

## Example
```
$ python gloveTwittorVectors.py
Enter the first word: king
Enter the second word: queen

Vector for 'king' = [ 0.24489   -0.19915   -0.16848    0.14739    0.19808   -0.12205   ...
Vector for 'queen' = [ 0.39054    0.12318    0.41921    0.32083    0.35607    0.52853   ...
Difference between 'king' and 'queen' = [-0.14565   -0.32233   -0.58769   -0.17344   -0.15799   -0.65058   ...

king is to queen, as man is to woman
```
