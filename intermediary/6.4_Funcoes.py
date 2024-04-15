a = 4
b = 6
c = 9


def soma_mult(a, b, c=0):
    if c == 0:
        return a * b
    else:
        return a + b + c


if __name__ == "__main__":
    res = soma_mult(a, b, c)

    print(res)
