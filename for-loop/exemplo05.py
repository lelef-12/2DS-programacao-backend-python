


# For loop com if (condicional)
sucesso = False
for numero in range(3):
    print("Tentativa")
    if sucesso: # Dentro da variavel 'sucesso' está o valor booleano (true oyu false)
        print("Sucesso!, meu jovem.")
        break
else:
    print("Todas as 3 tentativas falharam!!!")