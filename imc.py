# exercício de cálculo de IMC (Índice Massa Corporal)

input("---Cálculo IMC---");

peso = float(input("Qual seu peso? "));
altura = float(input("E sua altura? "));

imc = peso / (altura ** 2);

if imc < 18.5:
    categoria = "você está abaixo do peso, cuidado!"
elif 18.5 <= imc <= 24.9:
    categoria = "voce está com peso normal, parabéns!"
elif 25 <= imc <= 29.9:
    categoria = "você está com sobre peso, cuidado!"
elif 30 <= imc <= 34.9:
    categoria = "você está OBESO."
else:
    categoria = "morreu já..."

print(f"Seu IMC é: {imc:.2f}")
print(f"Categoria: {categoria}")
print("Obrigado!")