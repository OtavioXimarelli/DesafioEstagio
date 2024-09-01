def fibonacci(num):
    if num < 0:
        raise ValueError("O numero não pode ser negativo")

    a, b = 0, 1
    while a < num:
        a, b = b, a + b
    return a


def check_num(num):
    fib_num = fibonacci(num)
    return fib_num == num


if __name__ == "__main__":
    num = int(input("Digite o numero desejado: "))
    if check_num(num):
        print(f"{num} está presente na sequência Fibonacci")
    else:
        print(f"{num} não está presente na sequência Fibonacci")
