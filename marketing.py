print("Olá, deixe aqui sua avaliação para nos ajudar:")
print("1 - PERFEITO")
print("2 - SATISFATÓRIO")
print("3 - RUIM")

Avaliação = int(input("Deixe aqui sua avaliação(1 , 2 ou 3): "))
#RESULTADOS DAS AVALIAÇÕES
if Avaliação == 1:
    resultado = "PERFEITO"
elif Avaliação == 2:
    resultado = "SATISFATÓRIO"
elif Avaliação == 3:    
    resultado = "RUIM"
else:  resultado = "AVALIAÇÃO INVÁLIDA"
    
#RESULTADO FINAL(agradecimentos)
print("Sua avaliação foi: ", resultado)
print("Obrigada pelo feedback!")
