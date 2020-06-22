dic = {}

class bcolors:
    HEADER = '\033[95m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m\033[100m\033[97m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'

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
    
    # process the input from the user
    print()
    required_synset_name = input(f"{bcolors.BOLD}Enter the synset name(s):{bcolors.ENDC} ({bcolors.WARNING}seperate multiple synset names with a white space {bcolors.ENDC}) \n").strip().split()
    
    # check if the input is empty
    num_required = len(required_synset_name)
    if num_required == 0:
        print(bcolors.UNDERLINE + "\tThere should be at least one synset name as the input." + bcolors.ENDC)
        exit()
    
    # build up the dictionary
    build_up_dic()

    error_num = 0
    for syn_name in required_synset_name:
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
            print(f"{bcolors.UNDERLINE}Summary{bcolors.ENDC}: " + bcolors.OKGREEN + "All " + str(len(required_synset_name)) + " synset names are processed successfully." + bcolors.ENDC)
        elif num_required == 2:
            print(f"{bcolors.UNDERLINE}Summary{bcolors.ENDC}: " + bcolors.OKGREEN + "Both synset names are processed successfully." + bcolors.ENDC)
        elif num_required == 1:
            print(f"{bcolors.UNDERLINE}Summary{bcolors.ENDC}: " + bcolors.OKGREEN + "The synset name is processed successfully." + bcolors.ENDC)
    else:
        if num_required != error_num:
            print(f"{bcolors.UNDERLINE}Summary{bcolors.ENDC}: " + bcolors.FAIL + "There is/are " + str(error_num) + " error(s)." + bcolors.ENDC + "The process of the other synset name(s) is successful.")
        else:
            print(f"{bcolors.UNDERLINE}Summary{bcolors.ENDC}: " + bcolors.FAIL + "There is/are " + str(error_num) + " error(s)." + bcolors.ENDC)



main()
