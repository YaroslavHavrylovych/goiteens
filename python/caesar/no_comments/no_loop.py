ALPHABET = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',\
                'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',\
                'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',\
                'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')
ORIGINAL_WORD = "Test"  
KEY = 3 
crypted_word = [] 

print("ORIGINAL_WORD= " + ORIGINAL_WORD) 
print("ORIGINAL_WORD as list = " + str(list(ORIGINAL_WORD))) 

letter = ORIGINAL_WORD[0] 
index = ALPHABET.index(letter) 
new_index = index + KEY 
crypted_word.append(ALPHABET[new_index]) 
print("encrypted_word = " + str(crypted_word))

letter = ORIGINAL_WORD[1] 
index = ALPHABET.index(letter)
new_index = index + KEY
crypted_word.append(ALPHABET[new_index])
print("encrypted_word = " + str(crypted_word))

letter = ORIGINAL_WORD[2] 
index = ALPHABET.index(letter)
new_index = index + KEY
crypted_word.append(ALPHABET[new_index])
print("encrypted_word = " + str(crypted_word))

letter = ORIGINAL_WORD[3] 
index = ALPHABET.index(letter)
new_index = index + KEY
crypted_word.append(ALPHABET[new_index])
print("encrypted_word = " + str(crypted_word))
