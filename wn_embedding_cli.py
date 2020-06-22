import argparse
import sys

dic = {}

class bcolors:
    HEADER = '\033[95m'
    BOLD = '\033[1m'
    SUMMARY = '\033[100m\033[97m'
    UNDERLINE = '\033[4m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'

class N:
    pass 


def build_up_dic():
    '''
    Read from the composite file and store info into a dictionary 
    with synset name as the key and word vector as the value.
    '''
    global dic

    with open("WordNet_Hypernym_Hyponym.composite", 'r') as fl:
        for line in fl:
            line_list = line.strip().split(', ')
            synset_name = line_list[0]
            dic[synset_name] = line_list[1:]


def main():
    '''
    Get synset name(s) provided by the user and
    print out its/their word vector(s) respectively
    '''
    global dic

    # use ns to access the namespace
    ns = N()

    # process the input from the user
    parser = argparse.ArgumentParser(description='Process one or more synset names seperated by white space and return their respective word vectors.')
    parser.add_argument('synset_name', nargs='+', help="The name of the synset to process.")
    parser.add_argument('-v','--version', action='version', version='WordNet 3.0')
    parser.parse_args(sys.argv[1:], namespace=ns)

    # build up the dictionary
    build_up_dic()
    
    error_num = 0
    num_required = len(ns.synset_name)
    for syn_name in ns.synset_name:
        print()
        if syn_name in dic:
            print(f"{bcolors.HEADER}Synset name: {bcolors.ENDC}"+bcolors.OKGREEN+ syn_name + bcolors.ENDC +'\n' +', '.join(dic[syn_name]))
        else:
            error_num += 1
            print(f"{bcolors.FAIL}Error: {bcolors.ENDC}The synset name "+"\"" + bcolors.BOLD + syn_name + bcolors.ENDC + "\" is invalid.")

    # summary message:
    print()
    if error_num == 0:
        if num_required > 2:
            print(f"{bcolors.SUMMARY}Summary{bcolors.ENDC}: " + bcolors.OKGREEN + "All " + str(num_required) + " synset names are processed successfully." + bcolors.ENDC)
        elif num_required == 2:
            print(f"{bcolors.SUMMARY}Summary{bcolors.ENDC}: " + bcolors.OKGREEN + "Both synset names are processed successfully." + bcolors.ENDC)
        elif num_required == 1:
            print(f"{bcolors.SUMMARY}Summary{bcolors.ENDC}: " + bcolors.OKGREEN + "The synset name is processed successfully." + bcolors.ENDC)
    else:
        if num_required != error_num:
            print(f"{bcolors.SUMMARY}Summary{bcolors.ENDC}: " + bcolors.FAIL + "There is/are " + str(error_num) + " error(s)." + bcolors.ENDC + "The process of the other synset name(s) is successful.")
        else:
            print(f"{bcolors.SUMMARY}Summary{bcolors.ENDC}: " + bcolors.FAIL + "There is/are " + str(error_num) + " error(s)." + bcolors.ENDC)



    
main()
