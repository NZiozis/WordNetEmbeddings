# Generating the Adjacency List

## Description
    
This program allows users to generate an undirected adjacency list composed of the hypernym and hyponym edges in the nltk WordNet 3.0 graph. The output format for a synset is as follows:

``` text
meet.v.05 718 717 797 12410 21109 21110 3943
```

The first column is the synset name. The second column is the node ID for the synset. All other numbers that follow are the node IDs that there exists an edge to. 

In order to use this in the DeepWalk algorithm, it is necessary to remove the synset name column. The name is there to facilitate the creation of the composite file and for debugging.

## Requirements
- Python 3
- nltk >= 3.5

It is recommended that you install this in a [virtual environment](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/) so that any varying versions of nltk on the machine won't conflict. This is not necessary on a clean machine.

After installing nltk it is necessary to download the data for WordNet. This can be achieved by running python in interpreter mode with the following command.

``` sh
$ python
```

In interpreter mode run the following two commands:

``` sh
>>> import nltk
>>> nltk.download()
```

After the second command, a window should appear. Navigate to the Corpora tab, select WordNet, and download it in the default location provided by ntlk.

## Usage 

Run the script using the following command:
``` sh
$ python adjList.py
```

The results will be printed to standard output, so it is necessary to redirect the output to a file if you want to use the output for anything besides debugging. A UNIX example for how this can be achieved is shown below: 

``` sh
$ python adjList.py > output.txt
```

The results will be stored in the file output.txt.
