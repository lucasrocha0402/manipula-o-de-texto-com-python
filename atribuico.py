frase = '    Aprenda Python  '
# o python cria blocos para guardar cada caractre, e esses quadrados recebem indice um numero 
# sequencial para caber todos os dados da frase 

# fatiamento: fatiar uma string é conseguir pegar pedaços da string 
# [] é um identificador para um componente em python chamado de lista 
# a lista de indice começa em 0, ou seja a contagem é 0, 1 , 2, 3, 4
# fatiando a cadeia de indice usando frase[9:13] ira aparecer apenas de 9 a 12 cortando o 13
# range o ultimo valor não entra na contagem
# frase[9:21:2] vai mostrar de 9 até 20 porem pulando de 2 em 2 indices
# frase[:5] ele vai começar do caractere 0 e vai até a letra 5 de indice
# frase[15: ele vai começar do 15 e vai ate o 20 mostrando tudo que tem do 15 ao 20
# frase[9::3] ele vai pegar do indice 9 ate o ultimo pois não tem um numero no meio e vai pular de 3 em 3 indices

# Análise com cadeia de texto: com que letra começa, primeira palavra
# len(frase) qual o comprimento da frase 21 caracter
# frase.count('o') count serve para contar quantas vezes aparece o 'o' minusculo, 0,13, fazendo a contagem já com o fatiamento
# frase.find('deo') em que indice começou o deo
# frase.find('android) se colocar dentro do find o valor de uma string que não existe ele retorna um -1
# usando o 'Curso" in frase voce vai saber se existem a palavra desejada
# transformação usando metodo frase.replace('Python','Android') replace troca a palavra que contem na frase por outra
# Não substitui na string
# frase.upper() colocar em maiuscula a frase toda, e se tiver alguma letra maiuscula ele mantem
# frase.lower() coloca em minusculo a frase toda, e se tiver alguma minuscula mantem
# frase.capitalize() capitalaze transforma toda em minuscula e apenas a primeira letra vira maiuscula
# frase.title() vai ver quantas palavras tem e vai transfrormar todas as primeiras letras das palavras em maiuscula
# frase.strip() vai excluir os espaços que não são necessario como no inicio da frase ou no final
# frase.rstrip() vai tratar todo o lado direito e mantendo o da esquerda se houver
# frase.lstrip() vai tratar todo o lado da esquerda e manter o da direita se houver
# frase.split() #estudar split, vi ococorrer uma divisão aonde tver espaço, refazendo os indices, e gerar um novo indice de acordo com as palavras
# '-'join.(frase) gerar uma string unica com - para separar as strings
print(frase.strip())