'''

Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos
são do imposto de renda, que depende do salário bruto (conforme tabela abaixo) e 3% para
o Sindicato e que o FGTS corresponde a 11% do salário bruto, mas não é descontado
(é a empresa que deposita.) e 10% que é descontado do INSS. O salário líquido corresponde
ao salário bruto menos os descontos.
O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.

Desconto do IR;
a. Salário Bruto ate R$900,00 (inclusive) – Isento;
b. Salário Bruto de R$ 1500, 00 (inclusive) – desconto de 5%;
c. Salario bruto até R$ 2500,00 (Inclusive) – desconto de 10%;
d. Salário bruto acima de 2500 – Desconto de 20%.

Imprima na tela as informações, dispostas conforme o exemplo abaixo,
no exemplo valor da hora é 5 e a quantidade de horas é 220.

Salário bruto (5 * 220)   : R$   1100,00
( – ) IR (5%)   :   R$55,00
( – ) INSS ( 10% )   :   R$110,00
( – ) Sindicato(3%)   :   R$33,00
FGTS ( 11%)    :    R$121,00
Total de descontos   :   R$198,00
Salário Líquido     :    R$902,00

'''

# pedindo ao usuário o valor da hora e a quantidade de horas trabalhadas no mês
valor_hora = int(input('Digite o valor da sua hora: R$'))
qtd_horas = int(input('Digite a quantidade de horas trabalhadas no mês: '))

print('\n---------- FOLHA DE PAGAMENTO ----------\n')

# calculando e imprimindo salário bruto
salario_bruto = valor_hora * qtd_horas
print(f'Salário bruto : R${salario_bruto:.2f}\n')

# calculando e imprimindo imposto renda
if salario_bruto <= 900:
    print('( - ) IR ( ISENTO ) : R$0')
elif salario_bruto > 900 and salario_bruto <= 1500:
    ir = salario_bruto - (salario_bruto * 0.95)
    print(f'( - ) IR ( 5% ) : R${ir:.2f}')
elif salario_bruto > 1500 and salario_bruto <= 2500:
    ir = salario_bruto - (salario_bruto * 0.9)
    print(f'( - ) IR ( 10% ) : R${ir:.2f}')
elif salario_bruto > 2500:
    ir = salario_bruto - (salario_bruto * 0.8)
    print(f'( - ) IR ( 20% ) : R${ir:.2f}')

# calculando e imprimindo inss
inss = salario_bruto - (salario_bruto * 0.9)
print(f'( - ) INSS ( 10% ) : R${inss:.2f}')

# calculando e imprimindo sindicato
sindicato = salario_bruto - (salario_bruto * 0.97)
print(f'( - ) Sindicato ( 3% ) : R${sindicato:.2f}')

# calculando e imprimindo fgts
fgts = salario_bruto - (salario_bruto * 0.89)
print(f'( - ) FGTS ( 11% ) : R${fgts:.2f}')

# calculando e imprimindo descontos
desconto = ir + inss + sindicato
print(f'Total de descontos (IR + INSS + Sindicato): R${desconto:.2f}\n')

# calculando e imprimindo salario liquido
salario_liquido = salario_bruto - desconto
print(f'Salário líquido : R${salario_liquido:.2f}')
