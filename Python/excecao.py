#exceptions

#try
#ecept
while True:
    try:
        x = int(input("Digite um valor para x "))

        print(f"x é {x}")
        
    except ValueError:
        print("x nao é um numero!")
    else:
        break