personagens = ["Frodo", "Sam", "Legolas", "Gandalf", "Ginly", "Smeagol", "Bilbo"]

especies = ["Hobbit", "Hobbit","Hobbit", "Mago", "Anao", "Hobbit", "Hobbit"]


#crie uma lista colocando as seguintes informaçoes: Apresentar o Menu (incluindo: incluir,listar) Digite incluindo: (nome, endereço, telefone)

personagens = [ 
                {

                "Nome":"Frodo",
                "Especie":"Hobbit",
                "local":"Condado" 
                },  {

                "Nome":"Sam",
                "Especie":"Hobbit",
                "local":"Condado" 
                },

                {

                "Nome":"Legolas",
                "Especie":"Elfo",
                "local":"Valfenda" 
                }


                ]

#personagens = {"Frodo":"Hobbit",
#                "Sam":"Hobbit", 
 #               "Legolas":"Elfo",
  #              "Smeagol":"Hobbit",
      #          "Bilbo":"Hobbit"
       #         }

for personagem in personagens:
    print(personagem["Nome"],personagem["Especie"])