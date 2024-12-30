# Exercício de contagem de vogal

def contar_vogais(frase):
    vogais = 'aeiouAEIOU';
    contador = 0

    for letra in frase:
        if letra in vogais:
            contador += 1;

    return contador;

def contar_consoantes(frase):
    consoantes = 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'
    contador2 = 0

    for letra in frase:
        if letra in consoantes:
            contador2 += 1;

    return contador2;


frase_usuario = input("Qual seu nome?: ")

numero_vogais = contar_vogais(frase_usuario)
numero_consoantes = contar_consoantes(frase_usuario)

print(f"Seu nome tem: {numero_vogais} vogais e {numero_consoantes} consoantes.")

