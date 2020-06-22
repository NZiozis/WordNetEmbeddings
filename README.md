# WordNet Embeddings

## Description

This program allows users to use [pre-generated vector embeddings](#how-the-vectors-are-generated) on the WordNet graph of hypernyms and hyponyms to conduct word sense disambiguation of words in sentence. In python_API.py, the user provides a WordNet synset they are interested in and the vector is returned.

## Usage

- ### Interactive Version

  - First, run the _wn_embedding_interactive.py_ file.  
    `$ python wn_embedding_interactive.py`

  - Second, enter at least one or more synset names separated by white space. If the input is empty, the program will report a warning message and exit.

  - Then, the program will process the input. If one of the synset names is invalid, the program will report an error message and **continue** processing the other synset names. Otherwise, it will return the word vector respectively for each synset name.

  - Finally, a summary message will be returned once the program finishes running. The summary message contains the information of the number of successful processed synset names and errors. After reading the summary message, you can always go back to check the detail for each synset name.

  The interactive

  _Demo for interactive version:_

  - Single synset name:

    ![interactive demo](/image/interactive.gif)

  - Multiple synset names:  
    Please separate synset names with white space.

    ![interactive_mul demo](/image/interactive_mul.gif)

## How the vectors are generated

The vectors are generated using the DeepWalk algorithm ([paper](https://dl.acm.org/doi/pdf/10.1145/2623330.2623732), [GitHub](https://github.com/phanein/deepwalk)). The WordNet graph is parsed using the nltk python library and an undirected adjacency list is created based on the hypernym and hyponym edges found in WordNet. This adjacency list is then provided to the DeepWalk algorithm, with the default parameters, which outputs the vector embeddings. View them at [WordNet_Hypernym_Hyponym.composite](./WordNet_Hypernym_Hyponym.composite).

