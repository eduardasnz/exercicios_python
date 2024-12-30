import random
import os

# Lista de palavras para o jogo
palavras = ["maria", "antonio", "jose", "carlos", "jorge", "marcia"]

# Python escolhe uma palavra aleatória
palavra_secreta = random.choice(palavras).lower()

# Variáveis do jogo
letras_descobertas = ["_"] * len(palavra_secreta)  # Representação inicial da palavra incompleta
tentativas_restantes = 6
letras_erradas = []

# Loop do jogo
while tentativas_restantes > 0 and "_" in letras_descobertas:
    os.system("cls" if os.name == "nt" else "clear")  # Limpa a tela
    print("BEM-VINDO AO JOGO DA FORCA")
    print(f"\nA palavra tem {len(palavra_secreta)} letras.")
    print(f"Palavra: {' '.join(letras_descobertas)}")
    print(f"Letras erradas: {', '.join(letras_erradas)}")
    print(f"Tentativas restantes: {tentativas_restantes}")
    print("DICA = NOME DE PESSOA")
    print("\n---------------------------------")
    
    letra = input("Digite uma letra: ").lower()

    if letra in palavra_secreta:
        print("Você acertou uma letra!")
        # Atualiza a palavra incompleta
        for i in range(len(palavra_secreta)):
            if palavra_secreta[i] == letra:
                letras_descobertas[i] = letra
    elif letra in letras_erradas or letra in letras_descobertas:
        print("Você já tentou essa letra.")
    else:
        print("Letra incorreta!")
        letras_erradas.append(letra)
        tentativas_restantes -= 1

# Verifica o resultado final
os.system("cls" if os.name == "nt" else "clear")  # Limpa a tela antes do resultado final
if "_" not in letras_descobertas:
    print("\nParabéns, você venceu! 🎉")
else:
    print("\nVocê perdeu! 😢")
    print(f"A palavra era: {palavra_secreta}")
