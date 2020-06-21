# WordNet Embeddings

## Description

This program allows users to use [pre-generated vector embeddings](#how-the-vectors-are-generated) on the WordNet graph of hypernyms and hyponyms to conduct word sense disambiguation of words in sentence. In python_API.py, the user provides a WordNet synset they are interested in and the vector is returned.

## How the vectors are generated

The vectors are generated using the DeepWalk algorithm ([paper](https://dl.acm.org/doi/pdf/10.1145/2623330.2623732), [GitHub](https://github.com/phanein/deepwalk)). The WordNet graph is parsed using the nltk python library and an undirected adjacency list is created based on the hypernym and hyponym edges found in WordNet. This adjacency list is then provided to the DeepWalk algorithm, with the default parameters, which outputs the vector embeddings. View them at [WordNet_Hypernym_Hyponym.composite](./WordNet_Hypernym_Hyponym.composite).

## Usage

- **Interactive Verison**

  - First, run the _wn_embedding_interactive.py_ file.  
    `$ python wn_embedding_interactive.py`
  - Second, enter one or more synset names seperated by white space.
  - Finallly, the program will return respective word vector(s) for synset name(s)

  _Demo for interactive verison:_

  - single synset name:  
    ![interactive demo](/image/interactive.gif)

  - multiple synset names:  
    ![interactive_mul demo](/image/interactive_mul.gif)
