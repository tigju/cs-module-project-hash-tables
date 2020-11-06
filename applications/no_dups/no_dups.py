def no_dups(s):
    # Your code here
    no_duplicates = []
    splited_s = s.split()
    for word in splited_s:
        if word not in no_duplicates:
            no_duplicates.append(word)
        else:
            continue
    no_dup_string = " ".join(no_duplicates)
    return no_dup_string



if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))
