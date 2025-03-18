def funcao (a, b):
    print(f'A mensagem é: {a}. O número é: {b}')
mensagem=(str(input('Digite qualquer frase:')))
numero=(int(input('Digite qualquer número:')))
def main ():
    funcao(mensagem, numero)
main()

def multiplicacao(c, d):
    resultado = c * d
    return resultado

def main():
    v1 = int(input('Digite o primeiro valor:'))
    v2 = int(input('Digite o segundo valor:'))
    r1 = multiplicacao(v1, v2)
    print(f'O resultado da multiplicação é: {r1}')
main()

