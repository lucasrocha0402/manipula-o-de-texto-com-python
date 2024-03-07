fraseUsuario = input("Digite a frase: ")

fraseMinuscula = fraseUsuario.lower()

quantosA = fraseMinuscula.count('a')

posicaoA = fraseMinuscula.find('a')

ultimaA = fraseMinuscula.rfind('a')

print(f" Existem {quantosA} a na frase, aparece na {posicaoA} e na {ultimaA} como ultima")