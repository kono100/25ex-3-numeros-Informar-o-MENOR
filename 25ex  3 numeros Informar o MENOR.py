

#25. Elabore um programa que leia 3 valores inteiros e informe qual é o MENOR.
a = int(input("Digite o primeiro valor:"))
b = int(input("Digite o segundo valor:"))
c = int(input("Digite o terceiro valor:"))

menor = a
if b < c and b < a:
    menor = b
if c < b and c < a:
    menor = c

print(f"\nO menor número digitado foi {menor}\n")