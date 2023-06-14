a = 0
b = 0
c = 0
d = 5
n_linhas = int(input("Insira quantidade de linhas na matriz: "))
while n_linhas <= 0:
    print("Você só pode usar numeros maiores que 0")
    lista_user = int(input("insira o Tamanho novamente: "))
tam_lista  = int(input("Insira o tamanho da lista: "))
lista_user = 0
Matriz = []
Lista = []
while tam_lista <= 0:
    print("Você só pode usar numeros maiores que 0")
    tam_lista = int(input("Insira o Tamanho novamente: "))
for i in range(tam_lista):
    lista_user = int(input("Insira valores inteiros entre -10 e 5: "))
    while lista_user < -10:
        print("Você só pode usar numeros maiores que -10")
        lista_user = int(input("Tente inserir os valores inteiros entre -10 e 5 novamente: "))
    while lista_user > 5:
        print("Você só pode usar numeros maiores que 5")
        lista_user = int(input("Tente inserir os valores inteiros entre -10 e 5 novamente: "))
    Lista.append(lista_user)
print("----Lista----")
for i in range(len(Lista)):
    print(Lista[i])
print("--------")
Matriz.append(Lista)
print("----Matriz----")
for i in range(len(Lista)):
    l = []
    b += 1
    for j in range(n_linhas):
        a = Lista[j]
        c = a * b
        l.append(c)
    Matriz.append(l)
print(Matriz)
for i in range(len(Matriz)):
    for j in range(n_linhas):
        if j == i:
            if Matriz[i][j-1] < d:
                d = Matriz[i][j-1]
print("O menor valor acima da diagonal é ",d)