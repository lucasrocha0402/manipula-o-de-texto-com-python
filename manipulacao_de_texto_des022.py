nome = input('digite seu nome: ')

nomeMaiusculo = nome.upper()

nomeMinusculo = nome.lower()

nomeSemEspaco = nome.strip()

nomeformatado = nomeSemEspaco.replace(" ", "")

contadorDeLetra = len(nomeformatado)


print(f'Aqui está seu nome em maiusculo:{nomeMaiusculo}, aqui o seu nome em minusculo: {nomeMinusculo}, quantas letras tem: {contadorDeLetra} letras ')