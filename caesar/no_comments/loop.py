ALPHABET = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',\
                'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',\
                'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',\
                'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')
ORIGINAL_WORD = "Test"
KEY = 3
crypted_word = []
print("ORIGINAL_WORD = " + ORIGINAL_WORD)
print("ORIGINAL_WORD as list = " + str(list(ORIGINAL_WORD)))

length = len(ORIGINAL_WORD) 

for i in range(length):
    letter = ORIGINAL_WORD[i] 
    index = ALPHABET.index(letter) 
    new_index = index + KEY 
    crypted_word.append(ALPHABET[new_index]) 
    print("crypted_word = " + str(crypted_word)) 
