
def word_count(s):
    # Your code 
    no_punct = "".join(c for c in s if c not in ("?", ".", ";", ":", "!", ",", '"',
                                                 "-", "+", "=", "/", "\\", "|", "[", "]", "{", "}", "(", ")", "*", "^", "&"))
    arr = no_punct.lower().split()
    d = {}

    for word in arr:
        if word in d:
            d[word] += 1
        else:
            d[word] = 1
    return d


if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))
