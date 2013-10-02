#!/usr/bin/env python

import sys
import random
import twitter

def make_chains(corpus):
    """Takes an input text as a string and returns a dictionary of
    markov chains."""
    markov_dict = {}
    
    for word in range(len(corpus) - 2):
        our_tuple = (corpus[word], corpus[word + 1])
        markov_dict.setdefault(our_tuple, [])
        markov_dict[our_tuple].append((corpus[word + 2]))

    return markov_dict

def make_text(chains):
    """Takes a dictionary of markov chains and returns random text
    based off an original text."""
    #makes a like of all keys
    tuple_list = chains.keys()
    
    
    while True:
        #randomly chooses the first tuple
        random_tuple_text = random.choice(tuple_list)
        
        first_letter = random_tuple_text[0][0]
        #Check that first char is cap, if not, rechoose
        if ord(first_letter) >= ord('A') and ord(first_letter) <= ord('Z'):
            tuple_text = random_tuple_text
            break
        
    #sets first two words in random_text to tuple words
    random_text = " ".join(tuple_text)
    
    while True:
        next_word = random.choice(chains[tuple_text])
        random_text = " ".join((random_text, next_word))       
        tuple_text = (tuple_text[1], next_word)

        if random_text[-1] == "." or random_text[-1] == "?":
            return random_text
        elif len(random_text) >= 120:
            random_text = random_text + "?"
            return random_text

def main():
    args = sys.argv
    script, file_name1, file_name2 = args
    
    input_text1 = open(file_name1).read().replace(")", " ").replace("(", " ").split()
    input_text2 = open(file_name2).read().split()
    input_text = input_text1 + input_text2

    chain_dict = make_chains(input_text)
    random_text = make_text(chain_dict)
    
    make_text(chain_dict)
    
    # print random_text

    api = twitter.Api(
        consumer_key=' ',
        consumer_secret=' ', 
        access_token_key=' ', 
        access_token_secret=' '
        )

    api.PostUpdate(random_text)

    print random_text

if __name__ == "__main__":
    main()