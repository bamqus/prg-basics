# Create a function f(word) that, for a given word word, returns a string of characters in which the successive
# letters of the word create a so-called Mexican wave. Initially, the first letter of the word is uppercase and the
# remaining letters are lowercase. Then the second letter of the word is uppercase and the remaining letters are
# lowercase, etc. Separate the words with a minus sign (-). Example:
# f("water") returns "Water-wAter-waTer-watEr-wateR"
# f("a") returns "A"
# f("") returns "" 


def f(word):
    wave = []
    for i in range(len(word)):
        wave_word = word[:i].lower() + word[i].upper() + word[i+1:].lower()
        wave.append(wave_word)
    return "-".join(wave)



print(f(""))

