print("========================================")
print("   ARKETECH - SIMULADOR DE CRÉDITO")
print("========================================")
 
# Entrada de dados
renda = float(input("Digite a renda mensal da empresa (R$): "))
emprestimo = float(input("Digite o valor do empréstimo solicitado (R$): "))
 
# Verificação dos valores informados
if renda <= 0 or emprestimo <= 0:
    print("\nErro: a renda e o empréstimo devem ser maiores que zero.")
 
# Regra 1: Aprovação do crédito
elif emprestimo <= renda * 3:
    print("\nStatus: CRÉDITO APROVADO!")
    print("O empréstimo foi aprovado automaticamente.")
 
# Regra 2: Análise do crédito
elif emprestimo <= renda * 5:
    print("\nStatus: EM ANÁLISE!")
    print("O empréstimo precisa de uma avaliação adicional.")
 
# Regra 3: Recusa do crédito
else:
    print("\nStatus: CRÉDITO RECUSADO!")
    print("O valor solicitado ultrapassa o limite permitido.")
 
print("========================================")
print("Obrigado por utilizar o simulador ArkeTech!")