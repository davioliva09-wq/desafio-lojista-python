produtos = []

for i in range(3):
    preco = float(input(f"Produto {i+1}: "))
    produtos.append(preco)

print(produtos)

total = sum(produtos)

print('total: ', total)

desconto = (total/10)

print("valor total: ", total, "você tem ", desconto , "de desconto")

frete = float(input("Digite o valor do frete: "))
print("Frete:", frete)

if total > 1000:
    comissao = total * 0.30
    
elif total >= 500 and total <= 1000:
    comissao = total * 0.15
    
else:
    comissao = total * 0.05

print(f"Comissão do vendedor : {comissao:.2f}")

print(f"""
valor da compra: {total:.2f}
valor descontado: {desconto:.2f}
valor do frete: {frete:.2f}
total pago: {(total - desconto + frete):.2f}
""")