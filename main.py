letters = list(input("Letters: ").upper())
points = {
    'A': 1,
    'E': 1,
    'I': 1,
    'O': 1,
    'U': 1,
    'L': 1,
    'N': 1,
    'S': 1,
    'T': 1,
    'R': 1,
    'D': 2,
    'G': 2,
    'B': 3,
    'C': 3,
    'M': 3,
    'P': 3,
    'F': 4,
    'H': 4,
    'V': 4,
    'W': 4,
    'Y': 4,
    'K': 5,
    'J': 8,
    'X': 8,
    'Q': 10,
    'Z': 10
}
words = []
with open('words.txt', 'r') as f:
    for word in f:
        copyLetters = letters.copy()
        word = word.strip()
        equal = True
        for letter in word:
            if letter in copyLetters:
                copyLetters.remove(letter)
            elif '?' in copyLetters:
                copyLetters.remove('?')
            else:
                equal = False
                break
        if equal:
            words.append(word)
wordValues = {}
value = 0
for word in words:
    value = 0
    copyLetters = letters.copy()
    for letter in word:
        if letter in copyLetters:
            value += points[letter]
            copyLetters.remove(letter)
    wordValues[word] = value
sortedWords = {k: v for k, v in sorted(wordValues.items(), key=lambda item: item[1])}
for key in sortedWords.keys():
    print(f'{key}: {sortedWords[key]}')
