nome_completo = input("Digite o nome completo: ")

partes_nome = nome_completo.split()
primeiro_nome = partes_nome[0]

partes_nome = nome_completo.split()
segundo_nome = ' '.join(partes_nome[1:])

print(f"O seu primeiro nome é {primeiro_nome} e seu segundo nome é {segundo_nome}")