# що нам потрібно для того, щоб зашифрувати слово?
# 1. Алфавіт 
# 2. Слово, яке шифруватимемо
# 3. Ключ, який вказує на скільки позицій ми зсуватимемо літеру
# ...

#Алфавіт. Шифруватимемо слово, що складається з великої і маленьких літер латиниці 
#а отже, наш алфавіт міститиме всі великі і маленькі літери латиниці.
ALPHABET = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',\
                'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',\
                'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',\
                'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')

# Слово, яке ми шифруватимемо
ORIGINAL_WORD = "Test"  
# В мові програмування Python, строка - це масив літер. Тобто ORIGINAL_WORD не дуже відрізняється від ALPHABET (і те і те - масив літер)
# Ми можемо прочитати кожну літеру окремо (по її індексу/номеру). 
# Наприклад: отримати першу букву можна за виразом ORIGINAL_WORD[0], другу - ORIGINAL_WORD[1] і т.д.
# Але ми не можемо таким чином переписати букву, тобто ORIGINAL_WORD[0] = "A" написати не дозволено,
# саме через це ми будемо використовувати коснтрукцію список (а не строку), щоб шифрувати слово

#Ключ шифрування (кількість позицій на яку ми зсуватимемо кожну літеру). Нехай ми зсуватимемо кожну літеру на 3 позиції. 
KEY = 3 

crypted_word = [] #створюємо список, де збережемо потім зашифроване слово

print("ORIGINAL_WORD= " + ORIGINAL_WORD) #виведе на консоль те, що міститься в нашому масиві
print("ORIGINAL_WORD as list = " + str(list(ORIGINAL_WORD))) #виведе на консоль те, що міститься в нашому масиві


### ШИФРУВАННЯ ###

letter = ORIGINAL_WORD[0] #в нову змінну letter записуємо першу букву слова (T)
index = ALPHABET.index(letter) #в змінну index записуємо позицію цієї літери у алфавіті
new_index = index + KEY #збільшуємо індекс літери на 3 (KEY) позиції і записуємо в new_index
crypted_word.append(ALPHABET[new_index]) #змінюємо першу літеру слова, на вже зашифровану
print("encrypted_word = " + str(crypted_word))

#далі ми не створюємо нових змінних, а користуємось вже існуючими і повторюємо ті ж кроки для
#кожної наступної літери

letter = ORIGINAL_WORD[1] # літера 'e'
index = ALPHABET.index(letter)
new_index = index + KEY
crypted_word.append(ALPHABET[new_index])
print("encrypted_word = " + str(crypted_word))

letter = ORIGINAL_WORD[2] # літера 's'
index = ALPHABET.index(letter)
new_index = index + KEY
crypted_word.append(ALPHABET[new_index])
print("encrypted_word = " + str(crypted_word))

letter = ORIGINAL_WORD[3] # літера 't'
index = ALPHABET.index(letter)
new_index = index + KEY
crypted_word.append(ALPHABET[new_index])
print("encrypted_word = " + str(crypted_word))
