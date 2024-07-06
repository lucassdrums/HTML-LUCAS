def calcularMedia(valor1, valor2):
    return  (valor1 + valor2) /2

def calcularConceito(valor):

    if valor >= 9:
        return "O"
    elif valor > 7 and valor <= 8.9:
        return "B"
    elif valor > 5 and valor <= 6.9:
        return "S"
    else:
        return "I"
    
def main():
    nota1 = float(input("Digite o primeira nota "))
    nota2 = float(input("Digite o segunda nota "))
    #print("Sua nota é: O")
#elif media > 7 and media <= 8.9:
    #print("Sua nota é: B")
#elif media > 5 and media <= 6.9 :
    #print("Sua nota é:  S")
#else:
    #print("Sua nota é: I")
    media = calcularMedia(nota1, nota2)
    print(calcularConceito(media))

main()
#if media >=9:
    #print("Sua nota é: O")
#elif media > 7 and media <= 8.9:
    #print("Sua nota é: B")
#elif media > 5 and media <= 6.9 :
    #print("Sua nota é:  S")
#else:
    #print("Sua nota é: I")
