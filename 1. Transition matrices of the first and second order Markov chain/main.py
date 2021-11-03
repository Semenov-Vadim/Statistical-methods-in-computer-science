import math  # для использования log2


def deleteWaste(s: str):
    """
    возвращает слово без лишних символов
    """
    for t in s:
        #if t in ":;\"\\/[](){}_><1234567890@#$%^&*_+=-~|,.!?":
        if t in ":;\"\\/[](){}_><1234567890@#$%^&*_+=-~|":  # без учета уже убранных символов
            s = s.replace(t, '')
    return s


def getTokens(book_name: str) -> list:
    tokens = []
    f = open(book_name)
    max_len_token = 16

    for line in f:
        # есть вероятность, что два слова будут разделяться не пробелом, а одним из следующих символов: .,!?
        line = line.replace('.', ' ')
        line = line.replace(',', ' ')
        line = line.replace('!', ' ')
        line = line.replace('?', ' ')
        line = line.lower().split()

        for i in range(len(line)):
            line[i] = deleteWaste(line[i])

        # убираем пустые слова в строке
        newLine = []
        for i in range(len(line)):
            if line[i] != "":
                newLine.append(line[i])
        line = newLine

        # убираем слишком длинные слова
        newLine = []
        for i in range(len(line)):
            if len(line[i]) <= max_len_token:
                newLine.append(line[i])
        line = newLine

        # после обработки строка может стать пустой, пропускаем ее
        if not line:
            continue

        for i in line:
            tokens.append(len(i))

    f.close()
    return tokens


def markov_1(tokens: list):
    d = {}
    len_tokens = len(tokens)

    for c in tokens:
        d[c] = {}

    d = dict(sorted(d.items()))

    for key1 in d:
        for key2 in d:
            d[key1][key2] = 0
        d[key1]['P.C'] = 0  # Р.С. — прогностическая способность

    for i in range(len_tokens):
        if i+1 < len_tokens:
            d[tokens[i]][tokens[i+1]] += 1

    for key1 in d:
        sum_values = 0
        shenn = 0  # индекс Шеннона (энтропии)

        for key2 in d[key1]:
            sum_values += d[key1][key2]

        for key2 in d[key1]:
            d[key1][key2] /= sum_values
            if d[key1][key2] != 0:
                shenn += (d[key1][key2] * math.log2(d[key1][key2]))

        d[key1]['P.C'] = 1 - (-shenn / math.log2(len(d[key1]) - 1))

    print('Цепь маркова первого порядка:')
    for c in d:
        print(c, ':', d[c])


def markov_2(tokens: list):
    d = {}
    len_tokens = len(tokens)

    for c in tokens:
        d[c] = {}

    d = dict(sorted(d.items()))

    for key1 in d:
        for key2 in d:
            d[key1][key2] = {}
            for key3 in d:
                d[key1][key2][key3] = 0
            d[key1][key2]['P.C'] = 0  # Р.С. — прогностическая способность

    for i in range(len_tokens):
        if i+2 < len_tokens:
            d[tokens[i]][tokens[i+1]][tokens[i+2]] += 1

    for key1 in d:
        for key2 in d:
            sum_values = 0
            shenn = 0  # индекс Шеннона (энтропии)
            for key3 in d[key1][key2]:
                sum_values += d[key1][key2][key3]

            for key3 in d[key1][key2]:
                if sum_values != 0:
                    d[key1][key2][key3] /= sum_values
                if d[key1][key2][key3] != 0:
                    shenn += (d[key1][key2][key3] * math.log2(d[key1][key2][key3]))
            d[key1][key2]['P.C'] = 1 - (-shenn / math.log2(len(d[key1][key2]) - 1))

    print('Цепь маркова второго порядка:')
    for key1 in d:
        for key2 in d:
            print('(', key1, ',', key2, ') :', d[key1][key2])


if __name__ == "__main__":
    my_book_name = "Crime And Punishment.txt"
    my_tokens = getTokens(my_book_name)
    print('Количество токенов: ', len(my_tokens), '\n')

    markov_1(my_tokens)
    print('\n\n\n')
    markov_2(my_tokens)
