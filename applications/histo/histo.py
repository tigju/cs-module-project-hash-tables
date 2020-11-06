# Your code here

hash_t = {}

def histogram(filename):
    # read the file text
    f = open(filename, "r")
    text = f.read()

    # remove punctuation and make words lower case
    no_punct = "".join(c.lower() for c in text if c not in ("?", ".", ";", ":", "!", ",", '"',
                                                 "-", "+", "=", "/", "\\", "|", "[", "]", "{", "}", "(", ")", "*", "^", "&"))
    
    # split by spaces
    arr = no_punct.split()

    # define dictionary
    word_count = {}

    # store word counts in dictionary
    for w in arr:
        if w in word_count:
            word_count[w] += 1
        else:
            word_count[w] = 1

    # sort by keys alphabetically
    sorted_dict_keys = {i: word_count[i] for i in sorted(word_count)}
    
    # sort values in descending order
    sorted_dict_values = {v: sorted_dict_keys[v] for v in sorted(
        sorted_dict_keys, key=sorted_dict_keys.get, reverse=True)}

    # find the longest key string
    max_key_length = len(max(sorted_dict_values, key=len))
    
    # define histogram string
    hist_str = ''

    # loop through the dict items 
    for key, value in sorted_dict_values.items():
        # create histogram bar based on value number
        bar = value*'#'

        # calculate the spaces after each word
        num_spaces = max_key_length - len(key)+1
        # spaces based on number
        spaces = num_spaces*' '
        # hash marks are left justified two spaces after the longest word
        line = spaces + bar
        # append histogram string
        hist_str += f'{key}: {line}\n'

    return hist_str



print(histogram("robin.txt"))
