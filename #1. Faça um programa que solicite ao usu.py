#1. Faça um programa que solicite ao usuário o valor do litro de combustível (ex. 5,20) e quanto em dinheiro ele deseja abastecer (ex. 50,00). Calcule quantos litros de combustível o usuário obterá com esses valores.

def qnt_abstecera(valor, litros):
    resultado = valor // litros
    return resultado

saldo_abastecer = float(input("informe o valor que deseja abastecer: R$ "))
qnt_litros = float(input("Informe o valor do litro: "))
resultado = qnt_abstecera(saldo_abastecer, qnt_litros)
print(f"A quantidade de litros de combustível que você irá abastecer será: R$ {resultado}")