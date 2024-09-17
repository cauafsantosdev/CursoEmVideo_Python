# Elabore um programa que calcule o valor a ser pago por um produto, considerando seu preço normal e condição de pagamento: à vista no dinheiro ou pix tem 10% de desconto; à vista no cartão tem 5% de desconto; em até 2x no cartão é cobrado preço normal; 3x ou mais tem 20% de juros

v = float(input("Digite o valor do produto: R$"))
p = int(input("\nDigite 1 se o pagamento for à vista em dinheiro\nDigite 2 se o pagamento for à vista no cartão\nDigite 3 se o pagamento for em 2x no cartão\nDigite 4 se o pagamento for em 3x ou mais no cartão\n-> "))

if p == 1:
    print(f"\nCustará R${v - (v * 10 / 100):.2f}")
elif p == 2:
    print(f"\nCustará R${v - (v * 5 / 100):.2f}")
elif p == 3:
    print(f"\nCustará R${v:.2f}")
elif p == 4:
    print(f"\nCustará R${v + (v * 20 / 100):.2f}")
else:
    print("\nOpção inválida")
