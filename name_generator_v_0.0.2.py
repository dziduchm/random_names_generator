import numpy as np
import os
import argparse

parser = argparse.ArgumentParser(description='Random names generator')
parser.add_argument('--num_names', default=10, type=int, help='number of names to generate i.e. 20')
parser.add_argument('--name_len', default=5, type=int, help='length of names')
parser.add_argument('--save_file', default='No', type=str, help='path to save names to a file')
args = parser.parse_args()

def alphabet():
    """
    Function to create aplphabet 
    with vowels and consonants
    """
    vowels = {1:'a', 2:'e', 3:'i', 4:'o', 5:'u', 6:'y'}
    consonants = {1:'b', 2:'c', 3:'d', 4:'f', 5:'g', 6:'h', 7:'j', 8:'k', 9:'l', 
                10:'m', 11:'n', 12:'p', 13:'q', 14:'r', 15:'s', 16:'t', 17:'v', 
                18:'w', 19:'x', 20:'y'}
    return vowels, consonants

# B, C, D, F, G, H, J, K, L, M, N, P, Q, R, S, T, V, W, X, Y
def v_or_c(name_len, vowels, consonants):
    """
    Let the game begin v or c
    Random name generator
    building name of v's or c's to specified length
    """
    generated_name = str()
    for i in range(1, name_len+1):
        v_c = np.random.randint(1,9)
        if v_c in (1,2,8): # there's no science here, just rough guess :) on how to select vowel
            v = np.random.randint(1,7)
            vow = vowels[v]
            generated_name += vow
        else:#
            c = np.random.randint(1, len(consonants)+1)
            con = consonants[c]
            generated_name += con
    return generated_name

def save_names(names_list, out_path):
    with open(out_path, 'w') as f:
        for n in names_list:
            f.write(f'{n}\n')

def main():
    num_names = args.num_names # number of names to generate
    name_len = args.name_len # how long should be the name
    save_file = args.save_file.lower() # Yes of no to save file
    vowels, consonants = alphabet() # call alphabet dictionaries
    names_storage = list() # create a list to store the names
    for name in range(1, num_names +1):
        np.random.seed(name*np.random.randint(2,10000)) # 'randomize' the process using different random seeds
        if save_file == 'no':
            print (v_or_c(name_len, vowels, consonants)) # option for printing names on the screen only
        else:
            names_storage.append(v_or_c(name_len, vowels, consonants)) # option for saving names to a file
    if save_file == 'yes':
        path = os.getcwd() # saving path in current working directory
        if not os.path.isdir('names_generated'):
            os.mkdir('names_generated')
        save_path = os.path.join(path, 'names_generated/names.txt')
        save_names(names_storage, save_path)
        print(f'Saving names to {save_path}') # print saving path to the screen
if __name__ == "__main__":
    main()