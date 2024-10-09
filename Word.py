def match_words(words):
    ctr = 0
    lst = []
    for word in words:
        if len(word) > 1 and word[0] == word[-1]:
            ctr = +1
            lst.append(word)
    print("Lists of words with first and last character same\n", lst)
    return ctr
count = match_words(['abc', 'xyz', 'tuv', '1221'])
print("Numbers of words have first and last character", count)
