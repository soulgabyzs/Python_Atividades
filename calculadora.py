def add(x, y):
    """Função para adicionar dois números"""
    return x + y


def subtract(x, y):
    """Função para subtrair dois números"""
    return x - y


def multiply(x, y):
    """Função para multiplicar dois números"""
    return x * y


def divide(x, y):
    """Função para dividir dois números"""
    if y == 0:
        return "Erro! Divisão por zero."
    return x / y


def main():
    print("Selecione a operação:")
    print("1 - Adição")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")

    while True:
        choice = input("Escolha entre (1,2,3 ou 4): ")

        if choice in ['1', '2', '3', '4']:
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))

            if choice == '1':
                print(f"{num1} + {num2} = {add(num1, num2)}")

            elif choice == '2':
                print(f"{num1} - {num2} = {subtract(num1, num2)}")

            elif choice == '3':
                print(f"{num1} * {num2} = {multiply(num1, num2)}")

            elif choice == '4':
                print(f"{num1} / {num2} = {divide(num1, num2)}")

            next_calculation = input("Deseja realizar outra operação? (S/N): ")
            if next_calculation.lower() != 'S':
                break
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()
