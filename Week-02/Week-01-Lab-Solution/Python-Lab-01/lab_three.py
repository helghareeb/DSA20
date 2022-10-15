# بسم الله الرحمن الرحيم


def generate_multiplication(j):
    res = []
    for i in range(1, j + 1):
        inner_res = []
        for z in range(1, i + 1):
            inner_res.append(z * i)
        res.append(inner_res)
    return res

j = input('Enter Multiplication: ')
print(generate_multiplication(int(j)))
