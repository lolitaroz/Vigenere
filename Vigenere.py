import sys
if (sys.argv[1] == "encode"):
    bool = True
else:
    bool = False
plaintext = sys.argv[2]
key = sys.argv[3]

def shiftText(text, shift):
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
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
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
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

def vigenereCipher(text, key, bool):
    x = 0
    ans = ""
    fullKey = ""
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    while x != len(text):
        fullKey = fullKey + key[x % len(key)]
        x = x + 1
    for i in range(len(text)):
        shift = letters.find(fullKey[i])
    if (not bool):
        shift *= -1
        ans = ans + shiftText(text[i], shift)
    return ans


ans = vigenereCipher(plaintext, key, bool)
print(ans)
