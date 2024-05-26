nome = "Odair Gabriel"
idade = 48 
peso = 73.50
estudando = True

#Lista Mutaveis
Lista = [nome, idade, peso, estudando]
Lista2 = ["Odair Gabriel", 25, 73.50, True]

#Tuplas, Sao Imutaveis
tupla = ("Johann gabriel ", 13, 75.7, False)

print(Lista)
print(Lista2)
print(tupla)

dicionario = {
    "nome": "Odair Gabriel",
    "idade": 25,
    "peso": 80.50,
    "estudando": True
    
}
print(dicionario)

dicionario2 = {
    "nome": nome,
    "idade": idade,
    "peso": peso,
    "estudando": estudando
    
}