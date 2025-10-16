 #1 Lista vacia del 1 al 50
for var in range(1,51):
    print(var)

#2 lista vacia multiplos de 5 del 2 al 50
lista=[]
for i in range(2,51):
    if i%5==0:
        lista.append(i)
print(lista)        

#3 Imprimir triángulo de asteriscos
for i in range(1,11):
    print("*" * i)

#4 Para que sirve el ciclo while
#El ciclo while se repite mientras la condición sea verdadera.
#Su estructura es:
#while condición:

#Programa que imprima los números del 1 al 10
numero= 1
while numero <=10:
    print(numero)
    numero +=1
