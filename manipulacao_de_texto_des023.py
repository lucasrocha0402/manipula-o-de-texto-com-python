def ler_numero():
    while True:
        try:
            numero = int(input("Digite um número de 0 a 9999: "))
            if 0 <= numero <= 9999:
              return numero
            else: 
              print("Numero fora do intervalo permitido. Tente novamente")
        except ValueError:
              print('Entrada invalida digite apenas números.')
def imprimir_digitos(numero):
    milhar = numero // 1000
    centena = (numero % 1000) // 100
    dezena = (numero % 100) //10
    unidade = numero % 10

    print("Milhar", milhar)
    print("Centena", centena)
    print("Dezena", dezena)
    print("Unidade", unidade)

def main():
    numero = ler_numero()
    imprimir_digitos(numero)

if __name__ == "__main__":
    main()