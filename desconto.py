preco= 99.90
desconto = 0.1

resultado = preco - (preco*desconto)

print(resultado)

#condicionais 

if resultado < 50:
    print("O produto está barato!")
elif resultado < 100:
    print("O produto está com um preço razoável.")
else:
    print("O produto está caro.")