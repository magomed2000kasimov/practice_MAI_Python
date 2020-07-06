def calculate(data, findall):
    matches = findall(r"([abc])([+-]?=)([a,b,c]?)([+-]?\d+)?")  # Если придумать хорошую регулярку, будет просто
    for v1, s, v2, n in matches:  # Если кортеж такой структуры: var1, [sign]=, [var2], [[+-]number]
        # Если бы могло быть только =, вообще одной строкой все считалось бы, вот так:
        if len(s) == 1:
            if len(v2) == 0:
                data[v1] = int(n)
            else:
                if len(n) != 0:
                    data[v1] = data.get(v2) + int(n)
                else:
                    data[v1] = data.get(v2)
        else:
            if s[0] == '+':
                if len(v2) == 0:
                    data[v1] += int(n)
                else:
                    if len(n) != 0:
                        data[v1] += data.get(v2) + int(n)
                    else:
                        data[v1] += data.get(v2)
            else:
                if len(v2) == 0:
                    data[v1] -= int(n)
                else:
                    if len(n) != 0:
                        data[v1] -= data.get(v2) + int(n)
                    else:
                        data[v1] -= data.get(v2)


    return data








