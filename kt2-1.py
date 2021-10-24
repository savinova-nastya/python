import re
from functools import reduce

text = open('text.txt', encoding='utf-8').read()  # подкрепление тексового файла

string = text
print('Следующие слова в тексте: ', re.findall(r"[\w']+", string))

text1 = re.sub(r'[^\w\s]', '', text)
words = text1.split()
otvet1 = len(words)
print('Кол-во слов в тексте :', otvet1)
letter_count_per_word = {w: len(w) for w in words}

file = open("text.txt", encoding="utf-8")
s = reduce(lambda a, b: a + b, file.readlines())
sentences = filter(lambda a: a != "", re.split('[!.?]', s))
otvet3 = len(list(sentences)) - 1
print('Кол-во предложений в тексте: ', otvet3)


def count_words(s):
    return (len(s.strip().split(" ")))


pattern = re.compile(r'([А-ЯA-Z]((т.п.|т.д.|пр.|г.)|[^?!.\(]|\([^\)]*\))*[.?!])')
file = open("text.txt", encoding="utf-8")
data = file.read()
ar = []
for i, sent in enumerate(pattern.findall(data)):
    k = (i + 1, sent[0])
    ar.append(k)
    words = sent[0].split()
    otvet4 = len([x for x in data if x in ',.!?'])
    print('Номер предложения: {} {}'.format(i + 1, sent[0]))
    print('Колличество слов в предложении:', len(words))
print('Колличество букв в словах :', letter_count_per_word)

print('Колличество знаков препинания : ', otvet4)

import pickle

output = dict(Всего_слов_в_тексте=otvet1, Всего_предложений_в_тексе=otvet3, Предложения=ar,
              Кол_во_букв=letter_count_per_word, Кол_во_знаков_препинания=otvet4)
with open("text.bin", 'wb') as file:
    pickle.dump(output, file)

with open("text.bin", 'rb') as file:
    output2 = pickle.load(file)
print("Вывод:", output2)

ok = False
while not ok:
    try:
        n = int(input("Введите n - количество предложений в абзаце: "))
        if n < 1:
            raise Exception
        ok = True
    except Exception as e:
        print("Необходимо ввести натуральное число!", end=" ")

paragraphs = [[]]
for sentences in sentences:
    if len(paragraphs[-1]) < n:
        paragraphs[-1].append(sentences)
    else:
        paragraphs.append([sentences])

paragraphs.sort(key=lambda paragraph: len([words for sentences in paragraph for words in sentences.split()]))
print(*paragraphs, sep="\n")

text = "\n".join([" ".join(paragraph) for paragraph in paragraphs])

with open("resultText.txt", mode="w") as file:
    print(text, file=file)
