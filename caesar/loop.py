#Початок скопійовано з минулої теми (де рішення без циклу)
ALPHABET = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',\
                'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',\
                'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',\
                'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')
ORIGINAL_WORD = "Test"
KEY = 3
crypted_word = []
print("ORIGINAL_WORD = " + ORIGINAL_WORD)
print("ORIGINAL_WORD as list = " + str(list(ORIGINAL_WORD)))

length = len(ORIGINAL_WORD) #в змінну length запишемо довжину слова

for i in range(length):
    letter = ORIGINAL_WORD[i] #в змінну letter запишемо i-ту  букву слова
    index = ALPHABET.index(letter) #в змінну index запишемо позиція букви у алфавіті
    new_index = index + KEY #збільшуємо індекс букви на 3 (KEY) позиції і записуємо в new_index
    crypted_word.append(ALPHABET[new_index]) #додаємо до спику нову, вже зашифровану, букву
    print("crypted_word = " + str(crypted_word)) #виводимо слово з новою зашифрованою буквою
