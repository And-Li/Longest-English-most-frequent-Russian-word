text = open(input("Enter file's name:"), 'r').read()


#  Убираем все знаки препинания из теста:
def change_text(text):
    for item in '!"\'#$%&()*+-,/:;<=>?@[\\]^_{|}~':
        text = text.replace(item, "")
    return text.split()


#  Выдаёт только слова длиннее 3-х симвлолов:
def long_enough(text):
    list_of_words_long_enough = []  # пустой список, куда будем скаладывать слова, длиннее 3-х букв
    frequency_of_copies = {}  # пустой словарь для складывания пар "слово": количество упоминаний
    for item in text.split():
        if len(item) >= 3:
            list_of_words_long_enough.append(item)  # перебираем слова, складываем те, которые длинее 3-х букв в список
    for item in list_of_words_long_enough:
        counter_of_copies = frequency_of_copies.get(item, 0)  # слово пишется в словарь с ключём
        frequency_of_copies[item] = counter_of_copies + 1  # при повторении слова - ключ+1
    max_value = max(frequency_of_copies.values())  # выбирает максимальное значение из словаря
    final_dict = {k: v for k, v in frequency_of_copies.items() if v == max_value}  # выбирает пару ключ:значение с макс. значением
    return final_dict


#  Выдаёт английское самое длинное слово:
def english_words(text):
    list_of_english_words = []  # пустой список, куда будут добавляться англ. слова
    alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    for item in text.split():  # работает, но не совсем так: добавляет слово столько раз, сколько в нём англ. букв
        for char in item:
            if char in alphabet:
                list_of_english_words.append(item)
    list_max = max(list_of_english_words, key=len)  # Выводим самое длинное
    return list_max


print(change_text(text))
print(long_enough(text))
print("The longest english word is", english_words(text))


