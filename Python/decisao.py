x= int (input("Digite o Primeiro valor"))
y= int (input("Digite o Segundo valor"))

#vai converter o numero que é string para inteiro.

if x < y:
    print("x é menor do que y")
elif x > y:
    print("x é maior do que y")
else:
    print("x e y são iguais")

if x < y or x > y:
    print("x e y sao diferente")
    
if x == y or y == y:
    print("x e y sao iguais")