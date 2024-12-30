# CADASTRO DE USUÁRIOS
import hashlib

# Lista para armazenar usuários
usuarios = {}

def cadastrar_usuario():
    print("\n=== Cadastro de Usuário===")
    nome = input("Seu nome: ").strip()
    email = input("Seu email: ").strip()

    # verificar se ja existe email no 'armazem'
    for email in usuarios:
            print("email já cadastrado.")
            return
        
    senha = input("Sua senha: ")

    # armazenar os dados na lista
    usuarios[email] = {
        'nome': nome,
        'senha': senha
    }

    print("\nUsuario cadastrado.")

def mostrar_usuarios():
    if not usuarios:
        print("Não tem usuarios cadastrados.")
        return
    
    print("Usuários cadastrados: ")
    for email, dados in usuarios.items():
        print(f"Email: {email} \nNome: {dados['nome']}")

# Menu

while True:
    print("\nMenu:")
    print("\n1. Cadastrar usuário")
    print("2. Mostrar usuários")
    print("3. Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        cadastrar_usuario()
    elif opcao == '2':
        mostrar_usuarios()
    elif opcao == '3':
        print("Saindo...")
        break
    else:
        print("Opção inválida. Tente novamente.")