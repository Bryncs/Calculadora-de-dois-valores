def mensagem_de_erro() -> bool:
    print('O valor inserido não é válido')
    resposta = input('Digite "SIM" se deseja tentar novamente: ')
    return resposta.upper() == "SIM"

def seleciona_operacao() -> int:
    while True:
        print('Qual operação você deseja realizar?')
        try:
            operacao = int(input('''
            Digite o número de uma das opções abaixo:
            1 - Adição
            2 - Subtração
            3 - Multiplicação
            4 - Divisão
            Resposta: '''))
            
            if 1 <= operacao <= 4:
                return operacao
            print(f'O valor {operacao} não é uma opção válida')
        except ValueError:
            print('Por favor, digite um número válido.')
        
        if not mensagem_de_erro():
            print('Finalizando o código')
            raise SystemExit

def calcula_valores(operacao: int) -> tuple[float, str, float, float]:
    while True:
        print('Digite dois valores para realizarmos o cálculo')
        try:
            num_1 = float(input('Digite o primeiro valor: '))
            num_2 = float(input('Digite o segundo valor: '))

            if operacao == 4 and num_2 == 0:
                print('Erro: Divisão por zero!')
                if not mensagem_de_erro():
                    raise SystemExit
                continue

            calculos = {
                1: ('+', num_1 + num_2),
                2: ('-', num_1 - num_2),
                3: ('*', num_1 * num_2),
                4: ('/', num_1 / num_2),
            }
            operador, resultado = calculos[operacao]
            return resultado, operador, num_1, num_2

        except ValueError:
            if not mensagem_de_erro():
                raise SystemExit

def calculadora():
    while True:
        operacao = seleciona_operacao()
        resultado, operador, num_1, num_2 = calcula_valores(operacao)
        print(f'\nO resultado da sua operação {num_1} {operador} {num_2} é: {resultado}\n')
        
        reiniciar = input('Digite "SIM" se deseja realizar mais um cálculo: ')
        if reiniciar.upper() != "SIM":
            print('Finalizando o código')
            break

if __name__ == "__main__":
    calculadora()
