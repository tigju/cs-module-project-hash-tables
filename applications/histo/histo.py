# Your code here

hash_t = {}

def histogram(filename):
    f = open(filename, "r")

    text = f.read()

    no_punct = "".join(c.lower() for c in text if c not in ("?", ".", ";", ":", "!", ",", '"',
                                                 "-", "+", "=", "/", "\\", "|", "[", "]", "{", "}", "(", ")", "*", "^", "&"))
    
    arr = no_punct.split()
    word_count = {}

    for w in arr:
        if w in word_count:
            word_count[w] += 1
        else:
            word_count[w] = 1

    sorted_dict_keys = {i: word_count[i] for i in sorted(word_count)}
      
    sorted_dict_values = {v: sorted_dict_keys[v] for v in sorted(
        sorted_dict_keys, key=sorted_dict_keys.get, reverse=True)}

    
    max_key_length = len(max(sorted_dict_values, key=len))
    
    hist_str = ''
    for key, value in sorted_dict_values.items():
        bar = value*'#'
        num_spaces = max_key_length - len(key)+1
        spaces = num_spaces*' '
        line = spaces + bar
        hist_str += f'{key}: {line}\n'

    return hist_str



print(histogram("robin.txt"))
