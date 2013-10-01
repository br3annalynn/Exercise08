#!/usr/bin/env python
"""
make text:
text = random item (tuple) from dict
next_word = random.choice(d[(tuple)])
add next word to text
repeat and return string (text)

"""
import sys
import random

def make_chains(corpus):
    """Takes an input text as a string and returns a dictionary of
    markov chains."""
    markov_dict = {}
    
    for word in range(len(corpus) - 2):
        markov_dict.setdefault((corpus[word], corpus[word + 1]), [])
        markov_dict[(corpus[word], corpus[word + 1])].append((corpus[word + 2]))

    return markov_dict

def make_text(chains):
    """Takes a dictionary of markov chains and returns random text
    based off an original text."""
    #makes a like of all keys
    tuple_list = chains.keys()
    #randomly chooses the first tuple
    tuple_text = random.choice(tuple_list)
    #sets first two words in random_text to tuple words
    random_text = tuple_text[0] + " " + tuple_text[1]

    for item in range(0, 6):
        next_word = random.choice(chains[tuple_text])
        random_text = random_text + " " + next_word

        tuple_text = (tuple_text[1], next_word)
    
    print random_text
    #return tuple_text

def main():
    args = sys.argv
    script, file_name = args
    
    input_text = open(file_name).read().lower().replace(".", " ").replace(",", " ").replace("?", " ").split()

    chain_dict = make_chains(input_text)
    #random_text = make_text(chain_dict)
    make_text(chain_dict)
    #print random_text

if __name__ == "__main__":
    main()
