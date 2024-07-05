nome = input("Qual é o seu nome? ")


#nome = nome.strip() #strip executa os espaços de uma string

#nome = nome.capitalize()#transforma a primeira letra em Maiuscula
#nome = nome.strip().title #Quantos espaços estiver eles vai mudar sempre a primeira letra

#imprime uma mensagem na tela

#print("Hello,"  end="")
#print(nome)
#print('Ola, "amigo"')
#print(f"Ola,  {nome}")
#print("Ola," + nome)
primeiro, sobrenome = nome.split(" ")

print(f"Ola, {nome}")
print(sobrenome)

