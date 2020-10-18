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
            index = index + shift
            if index < 0:
                index = index + 26
            if index > 25:
                index = index - 26
            decrypt = decrypt + letters[index]
        else:
            decrypt = decrypt + i
    return decrypt


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
            shift = letters.find(fullKey[i]) * -1
        ans = ans + shiftText(text[i], shift)
    return ans


ans = vigenereCipher(plaintext, key, bool)
print(ans)
