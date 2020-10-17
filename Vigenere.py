import sys
if (sys.argv[0] == "encode"):
    bool = True
else:
    bool = False
plaintext = sys.argv[1]
key = sys.argv[2]

def shiftText(text, shift):
    letters = "abcdefghijklmnopqrstuvwxyz"
    decrypt = ""
    for i in text:
        if i in letters:
            index = letters.find(i)
            index = index - shift
            if index < 0:
                index = index + 26
            decrypt = decrypt + letters[index]
        else:
            decrypt = decrypt + i
    return decrypt


def frequency(text):
    total = 0
    letters = "abcdefghijklmnopqrstuvwxyz"
    freq = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for i in text:
        if i.isalpha():
            total = total + 1
    for i in range(26):
        count = 0
        for j in text:
            if (j == letters[i:i+1]):
                count = count + 1
        freq[i] = count * 1.0 / total
    return freq
