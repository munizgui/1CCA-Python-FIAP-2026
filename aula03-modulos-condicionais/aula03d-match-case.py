#imagina um prorama... que recebe a escolha dp usuario
#escolha_usiario
# 0 --> sair do progama
# 1 -> entrar no prorama
# -> erro!

escolha_usuario = 0

match escolha_usuario:
    case 0:
        print('Sair do programa')
    case 1:
        print('Entrar no programa')
    case _:
        print('erro')
