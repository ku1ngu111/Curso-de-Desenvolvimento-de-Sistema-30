internet = float(input("Digite a velocidade da internet em Mbps: "))

if internet >= 200:
    print("Internet muito rápida")
elif internet >= 50:
    print("Internet rápida")
else:
    print("Internet lenta")
