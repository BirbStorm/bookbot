def num_of_words(input):
    return len(input.split())

def characterCount(input):
    book = input.lower()
    charCount = {}
    for c in list(book):
        if c not in charCount:
            charCount[c] = 1
        else:
            charCount[c] += 1
    return charCount

def sortOn(dict):
    return dict["num"]

def sortCharacters(chars):
    return sorted(chars.items(), key=lambda x:x[1], reverse=True)