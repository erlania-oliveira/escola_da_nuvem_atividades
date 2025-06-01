'''Crie um programa que verifique se uma senha é forte. Uma senha forte deve ter pelo menos 8 caracteres e conter pelo menos um número. O programa deve continuar pedindo senhas até que uma válida seja inserida ou o usuário digite 'sair'.'''
while True:
    senha = input("Digite a senha ou 'sair' para encerrar:")

    if senha.lower()=="sair":
        print("O programa foi encerrado.")
        break
    if len(senha)<8:
        print("Senha fraca. A senha precisa conter pelo menos 8 caracteres.")
        continue
    if not any (caractere.isdigit() for caractere in senha):
        print("Senha fraca. A senha precisa conter pelo menos 1 número.")
        continue
    if not any (caractere.isalpha() for caractere in senha):
        print("Senha fraca. A senha precisa conter pelo menos 1 letra.")
        continue
    print("Senha forte")
    break
