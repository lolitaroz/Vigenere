import sys
f = open(sys.argv[1], "r")
text = f.read()

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

def freqCheck(text):
    standardFreq = [0.0834, 0.0154, 0.0273, 0.0414, 0.126, 0.0203, 0.0192, 0.0611,
    0.0671, 0.0023, 0.0087, 0.0424, 0.0253, 0.068, 0.077, 0.0166, 0.0009, 0.0568,
    0.0611, 0.0937, 0.0285, 0.0106, 0.0234, 0.002, 0.0204, 0.0006]
    # found on https://www.sttmedia.com/characterfrequency-english
    shift = 0
    min = 100000
    for i in range(26):
        close = 0
        check = shiftText(text.lower(), i)
        checkFreq = frequency(check)
        for j in range(len(standardFreq)):
            if checkFreq[j] > 0:
                close = close + abs(standardFreq[j] - checkFreq[j])
        if (min > close):
            min = close
            shift = i
    print(shift)

def main(text):
    pile1 = ""
    pile2 = ""
    pile3 = ""
    pile4 = ""
    for i in range(len(text)):
        if (i % 4 == 0):
            pile1 = pile1 + text[i:i+1]
        if (i % 4 == 1):
            pile2 = pile2 + text[i:i+1]
        if (i % 4 == 2):
            pile3 = pile3 + text[i:i+1]
        if (i % 4 == 3):
            pile4 = pile4 + text[i:i+1]
    freqCheck(pile1)
    freqCheck(pile2)
    freqCheck(pile3)
    freqCheck(pile4)
