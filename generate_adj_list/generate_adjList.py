from nltk.corpus import wordnet as wn

count = 1
dic = {}

class SynsetData:
    name = ""
    number = -1
    edges = set()

    def __init__(self, name, number, edges):
        
        self.name = name
        self.number = number
        self.edges = edges

    def __str__(self):
        out = "Name: {}, Number: {}, Edges: {}".format(self.name, self.number, self.edges)
        return out

def add_synset_if_not_exist(syn_name):

    global count
    global dic

    if dic.get(syn_name) is None:

        syn_data = SynsetData(syn_name, count, set())
        count += 1

        dic[syn_name] = syn_data

        return syn_data

    else:
        return dic[syn_name]

def main():
    '''
    extract the graph of hypernyms and hyponyms (symmetric) from WordNet
    '''

    global count
    global dic

    for syn in wn.all_synsets():
        syn_name = syn.name()
        syn_data = add_synset_if_not_exist(syn_name)
        
        hypernyms = syn.hypernyms()
        for hyper in hypernyms:
            # add it to the dic if not there yet
            hyper_name = hyper.name()
            hyper_data = add_synset_if_not_exist(hyper_name)

            # add edges(bidirectional) to the current synset and the hypernym
            syn_data.edges.add(hyper_data.number)
            hyper_data.edges.add(syn_data.number)

        hyponyms = syn.hyponyms()
        for hypo in hyponyms:
            hypo_name = hypo.name()
            hypo_data = add_synset_if_not_exist(hypo_name)

            syn_data.edges.add(hypo_data.number)
            hypo_data.edges.add(syn_data.number)

    for syn_data in dic.values():
        print(syn_data.name, end=' ')
        print(syn_data.number, end=' ')
        print(' '.join(map(str, syn_data.edges))) 



main()
