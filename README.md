# WordNet Embeddings

## Description

This program allows users to use [pre-generated vector embeddings](#how-the-vectors-are-generated) on the WordNet graph of hypernyms and hyponyms to conduct word sense disambiguation of words in sentence. In python_API.py, the user provides a WordNet synset they are interested in and the vector is returned.

## Usage

1. ### Interactive Version

   - First, run the _wn_embedding_interactive.py_ file.

     ```
     $ python wn_embedding_interactive.py
     ```

   - Second, enter **at least one** or more synset names **separated by white space**. If the input is empty, the program will report a warning message and exit.

   - Then, the program will process the input. If one of the synset names is invalid, the program will report an error message and **continue** processing the other synset names. Otherwise, it will return the word vector respectively for each synset name.

   - Finally, a summary message will be returned once the program finishes running. The summary message contains the information of the number of successful processed synset names and errors. After reading the summary message, you can always go back to check the detail for each synset name.

     _Demo for interactive version:_

     ![interactive demo](/images/interactive.gif)

   ***

2. ### Command Line Interface Version

   The API program has the following usage synopsis:

   ```
   $ python wn_embedding_cli.py [-h] [-v] synset_name [synset_name ...]
   ```

   where:

   - `synset_name` is the synset name to be processed. There should be at least one synset name as the input. If there are more than one synset names, they should be separated by white space.
   - `-h` or `--help` displays the help menu contains usage information and the description of the program.
   - `-v` returns the version of the WordNet.

   _Demo for command line interface version:_

   ![cli demo](/images/cli.gif)

## How the vectors are generated

The vectors are generated using the DeepWalk algorithm ([paper](https://dl.acm.org/doi/pdf/10.1145/2623330.2623732), [GitHub](https://github.com/phanein/deepwalk)). The WordNet graph is parsed using the nltk python library and an undirected adjacency list is created based on the hypernym and hyponym edges found in WordNet. This adjacency list is then provided to the DeepWalk algorithm, with the default parameters, which outputs the vector embeddings. View them at [WordNet_Hypernym_Hyponym.composite](./WordNet_Hypernym_Hyponym.composite).
