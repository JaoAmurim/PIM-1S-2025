import json
import hashlib
import os

ARQUIVO_USUARIOS = 'usuarios.json'
ARQUIVO_QUIZ = 'quiz.json'

# Função para limpar as informações do terminal
def limpar_terminal():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def carregar_usuarios():
    if os.path.exists(ARQUIVO_USUARIOS):
        with open(ARQUIVO_USUARIOS, 'r') as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return {}
    return {}

def salvar_usuarios(usuarios):
    with open(ARQUIVO_USUARIOS, 'w') as f:
        json.dump(usuarios, f, indent=4)

def hash_senha(senha):
    return hashlib.sha256(senha.encode()).hexdigest()

def cadastrar():
    limpar_terminal()  # Limpa antes de cadastrar
    usuarios = carregar_usuarios()
    usuario = input("Digite um nome de usuário: ")

    if usuario in usuarios:
        print("Usuário já existe.")
        return

    senha = input("Digite uma senha: ")
    usuarios[usuario] = hash_senha(senha)
    salvar_usuarios(usuarios)
    print("Usuário cadastrado com sucesso!")

def login():
    limpar_terminal()  # Limpa antes de login
    usuarios = carregar_usuarios()
    usuario = input("Digite seu nome de usuário: ")
    senha = input("Digite sua senha: ")

    if usuario in usuarios and usuarios[usuario] == hash_senha(senha):
        limpar_terminal()
        print(f"\n✅ Login bem-sucedido! Bem-vindo, {usuario}!")
        menu_principal(usuario)
    else:
        print("❌ Usuário ou senha incorretos.")

def menu():
    while True:
        print("\n==== Sistema de Login ====")
        print("1. Cadastrar")
        print("2. Login")
        print("3. Sair")
        opcao = input("Escolha uma opção: ")
        
        limpar_terminal()  # Limpa assim que escolhe a opção

        if opcao == '1':
            cadastrar()
        elif opcao == '2':
            login()
        elif opcao == '3':
            print("Saindo...")
            break
        else:
            print("Opção inválida.")
            print(f"Você escolheu a opção {opcao}")

def menu_principal(usuario):
    while True:
        print(f"\n=== Menu Principal (Usuário: {usuario}) ===")
        print("1. Perfil")
        print("2. Matérias")
        print("3. Quiz")
        print("4. Logout")

        opcao = input("Escolha uma opção: ")
        limpar_terminal()  # Limpa após a escolha no menu principal

        if opcao == '1':
            menu_perfil(usuario)
        elif opcao == '2':
            mostrar_conteudos_materia()
        elif opcao == '3':
            escolher_quiz(usuario)
        elif opcao == '4':
            print("🔓 Logout realizado com sucesso.")
            break
        else:
            print("Opção inválida.")

def menu_perfil(usuario):
    usuarios = carregar_usuarios()
    resultados_quiz = carregar_resultados_quiz()

    while True:
        print(f"\n🔎 Perfil de {usuario}")
        print("1. Exibir Informações do Perfil")
        print("2. Alterar Senha")
        print("3. Histórico de Quizzes")
        print("4. Voltar")

        opcao = input("Escolha uma opção: ")
        limpar_terminal()  # Limpa ao escolher uma opção no menu perfil

        if opcao == '1':
            exibir_informacoes(usuario, usuarios)
        elif opcao == '2':
            alterar_senha(usuario, usuarios)
        elif opcao == '3':
            exibir_historico_quizzes(usuario, resultados_quiz)
        elif opcao == '4':
            break
        else:
            print("Opção inválida.")

def exibir_informacoes(usuario, usuarios):
    if usuario in usuarios:
        print(f"Nome de Usuário: {usuario}")
    else:
        print("Usuário não encontrado.")

# Função para alterar a senha
def alterar_senha(usuario, usuarios):
    limpar_terminal()
    senha_atual = input("Digite sua senha atual: ")
    if usuarios.get(usuario) == hash_senha(senha_atual):
        nova_senha = input("Digite a nova senha: ")
        confirmar_senha = input("Confirme a nova senha: ")
        if nova_senha == confirmar_senha:
            usuarios[usuario] = hash_senha(nova_senha)
            salvar_usuarios(usuarios)
            print("Senha alterada com sucesso!")
        else:
            print("As senhas não coincidem.")
    else:
        print("Senha atual incorreta.")
    input("\nPressione Enter para continuar...")
    limpar_terminal()

# Função para exibir o histórico de quizzes
def exibir_historico_quizzes(usuario, resultados_quiz):
    limpar_terminal()
    if usuario in resultados_quiz:
        print(f"\n📊 Histórico de Quizzes de {usuario}:")
        for materia, resultados in resultados_quiz[usuario].items():
            print(f"\n{materia}:")
            print("=" * 50)  # Linha de separação para clareza
            for i, resultado in enumerate(resultados, 1):
                print(f"  Quiz {i}: {resultado} acertos")
            print("=" * 50)  # Linha de separação após cada matéria
    else:
        print("Você ainda não realizou nenhum quiz.")
    input("\nPressione Enter para continuar...")
    limpar_terminal()

def mostrar_conteudos_materia():
    while True:
        limpar_terminal()
        print("\n📖 Escolha a matéria para estudar:")
        print("1. Pensamento Lógico em Python")
        print("2. Redes de Computadores")
        print("3. CiberSegurança")
        print("4. Matemática")
        print("5. Voltar")
        escolha = input("Opção: ")
        limpar_terminal()

        if escolha == '1':
            aula_pensamento_logico()
        elif escolha == '2':
            aula_redes_de_computadores()
        elif escolha == '3':
            aula_ciberseguranca()
        elif escolha == '4':
            aula_matematica()
        elif escolha == '5':
            break
        else:
            print("Opção inválida.")
            input("\nPressione Enter para continuar...")

def aula_pensamento_logico():
    while True:
        limpar_terminal()
        print("\n📘 Aula de Pensamento Lógico em Python - Escolha o nível:")
        print("1. Fácil")
        print("2. Médio")
        print("3. Difícil")
        print("4. Voltar")
        nivel = input("Nível: ")
        limpar_terminal()

        if nivel == '1':
            print("\n🔹 Pensamento Lógico - Nível Fácil:")
            print("- Conceitos básicos de lógica: variáveis, operadores lógicos.")
            print("- Exemplo: if, else, while em Python.")
            print("- Exemplo: Operadores AND, OR, NOT.")
        elif nivel == '2':
            print("\n🔸 Pensamento Lógico - Nível Médio:")
            print("- Estruturas de repetição e decisão mais complexas.")
            print("- Exemplo: Laços aninhados, uso de funções.")
        elif nivel == '3':
            print("\n🔴 Pensamento Lógico - Nível Difícil:")
            print("- Algoritmos recursivos e estruturas de dados básicas.")
            print("- Exemplo: Implementação de funções recursivas.")
        elif nivel == '4':
            break
        else:
            print("Opção inválida.")

        input("\nPressione Enter para voltar.")
        limpar_terminal()


def aula_redes_de_computadores():
    while True:
        limpar_terminal()
        print("\n📙 Aula de Redes de Computadores - Escolha o nível:")
        print("1. Fácil")
        print("2. Médio")
        print("3. Difícil")
        print("4. Voltar")
        nivel = input("Nível: ")
        limpar_terminal()

        if nivel == '1':
            print("\n🔹 Redes - Nível Fácil:")
            print("- Conceitos básicos: O que é rede, tipos de rede (LAN, WAN).")
            print("- Equipamentos básicos: roteador, switch.")
        elif nivel == '2':
            print("\n🔸 Redes - Nível Médio:")
            print("- Protocolos comuns: TCP/IP, DHCP, DNS.")
            print("- Endereçamento IP e máscara de sub-rede.")
        elif nivel == '3':
            print("\n🔴 Redes - Nível Difícil:")
            print("- Conceitos avançados: VLANs, VPNs, roteamento avançado.")
            print("- Segurança em redes: firewalls, IDS/IPS.")
        elif nivel == '4':
            break
        else:
            print("Opção inválida.")

        input("\nPressione Enter para voltar.")
        limpar_terminal()


def aula_ciberseguranca():
    while True:
        limpar_terminal()
        print("\n📗 Aula de CiberSegurança - Escolha o nível:")
        print("1. Fácil")
        print("2. Médio")
        print("3. Difícil")
        print("4. Voltar")
        nivel = input("Nível: ")
        limpar_terminal()

        if nivel == '1':
            print("\n🔹 CiberSegurança - Nível Fácil:")
            print("- Conceitos básicos: senhas seguras, autenticação.")
            print("- Exemplo: Como criar uma senha forte.")
        elif nivel == '2':
            print("\n🔸 CiberSegurança - Nível Médio:")
            print("- Ataques comuns: phishing, malware.")
            print("- Como proteger sistemas contra ataques.")
        elif nivel == '3':
            print("\n🔴 CiberSegurança - Nível Difícil:")
            print("- Criptografia, firewalls avançados e políticas de segurança.")
            print("- Exemplo: Uso de VPN, análise de logs de segurança.")
        elif nivel == '4':
            break
        else:
            print("Opção inválida.")

        input("\nPressione Enter para voltar.")
        limpar_terminal()


def aula_matematica():
    while True:
        limpar_terminal()
        print("\n📘 Aula de Matemática - Escolha o nível:")
        print("1. Fácil")
        print("2. Médio")
        print("3. Difícil")
        print("4. Voltar")
        nivel = input("Nível: ")
        limpar_terminal()

        if nivel == '1':
            print("\n🔹 Matemática - Nível Fácil:")
            print("- Operações básicas: Adição (+), Subtração (-), Multiplicação (x), Divisão (÷)")
            print("- Exemplo de adição: 7 + 3 = 10")
            print("- Exemplo de subtração: 10 - 4 = 6")
            print("- Exemplo de multiplicação: 5 x 2 = 10")
            print("- Exemplo de divisão: 8 ÷ 2 = 4")
        elif nivel == '2':
            print("\n🔸 Matemática - Nível Médio:")
            print("- Expressões numéricas com parênteses e ordem de operações.")
            print("- Primeiro resolvemos parênteses, depois multiplicações/divisões, e por último somas/subtrações.")
            print("- Exemplo: (3 + 2) x 4 = 20")
            print("- Exemplo: 5 + 2 x 3 = 11 (multiplica primeiro: 2 x 3 = 6, depois soma: 5 + 6 = 11)")
        elif nivel == '3':
            print("\n🔴 Matemática - Nível Difícil:")
            print("- Potenciação: multiplicar um número por ele mesmo várias vezes.")
            print("- Raiz quadrada: descobrir qual número multiplicado por ele mesmo dá aquele valor.")
            print("- Problemas com várias etapas.")
            print("- Exemplo de potência: 2³ = 2 x 2 x 2 = 8")
            print("- Exemplo de raiz quadrada: √81 = 9")
        elif nivel == '4':
            break
        else:
            print("Opção inválida.")

        input("\nPressione Enter para voltar.")
        limpar_terminal()

def escolher_quiz(usuario):
    limpar_terminal()
    print("\n🧠 Escolha a matéria do Quiz:")
    print("1. Pensamento Lógico em Python")
    print("2. Redes de Computadores")
    print("3. CiberSegurança")
    print("4. Matemática")
    print("5. Voltar")

    escolha = input("Digite o número da matéria: ")
    limpar_terminal()

    if escolha == '1':
        escolher_dificuldade("Pensamento Lógico em Python", usuario)
    elif escolha == '2':
        escolher_dificuldade("Redes de Computadores", usuario)
    elif escolha == '3':
        escolher_dificuldade("CiberSegurança", usuario)
    elif escolha == '4':
        escolher_dificuldade("Matemática", usuario)
    elif escolha == '5':
        return
    else:
        print("Opção inválida.")
        input("\nPressione Enter para continuar...")
        limpar_terminal()

def quiz_pensamento_logico(usuario, dificuldade):
    if dificuldade == "Fácil":
        perguntas = [
            ("O que significa 'if' em Python?", "se"),
            ("Como se cria uma variável em Python?", "nome_da_variavel = valor"),
            ("Qual operador representa 'e' lógico?", "and"),
            ("Qual comando usamos para mostrar algo na tela?", "print"),
            ("Qual símbolo indica comentário em Python?", "#")
        ]
    elif dificuldade == "Médio":
        perguntas = [
            ("Como se faz um loop que repete 5 vezes?", "for i in range(5):"),
            ("Qual é a saída de: print(2 + 3 * 4)?", "14"),
            ("O que faz a função 'len()'?", "retorna o tamanho"),
            ("Como você define uma função em Python?", "def nome_funcao():"),
            ("Qual estrutura condicional verifica múltiplas condições?", "elif")
        ]
    elif dificuldade == "Difícil":
        perguntas = [
            ("O que é uma lista em Python?", "uma coleção ordenada"),
            ("Explique o conceito de 'recursão'.", "função que chama a si mesma"),
            ("Como capturar exceções em Python?", "try e except"),
            ("Para que serve o 'lambda'?", "função anônima"),
            ("O que significa 'PEP 8'?", "guia de estilo para Python")
        ]
    executar_quiz(perguntas, "Pensamento Lógico em Python", usuario, dificuldade)


def quiz_redes_computadores(usuario, dificuldade):
    if dificuldade == "Fácil":
        perguntas = [
            ("O que é um endereço IP?", "identificação de um dispositivo"),
            ("Qual o protocolo usado para navegar na web?", "HTTP"),
            ("O que significa Wi-Fi?", "conexão sem fio"),
            ("O que é um roteador?", "dispositivo que encaminha pacotes"),
            ("Qual a função do DNS?", "resolver nomes para IP")
        ]
    elif dificuldade == "Médio":
        perguntas = [
            ("O que faz o protocolo TCP?", "controle de conexão confiável"),
            ("Qual a diferença entre LAN e WAN?", "LAN é rede local, WAN é rede ampla"),
            ("O que é uma máscara de sub-rede?", "divide redes em sub-redes"),
            ("Explique o que é DHCP.", "atribui IPs automaticamente"),
            ("Qual porta padrão do HTTPS?", "443")
        ]
    elif dificuldade == "Difícil":
        perguntas = [
            ("O que é NAT?", "tradução de endereços de rede"),
            ("Qual o protocolo para transferência segura de arquivos?", "SFTP"),
            ("O que é um ataque DoS?", "negação de serviço"),
            ("Explique o que é VLAN.", "rede local virtual"),
            ("O que faz o protocolo ICMP?", "controle e mensagens de erro")
        ]
    executar_quiz(perguntas, "Redes de Computadores", usuario, dificuldade)


def quiz_ciberseguranca(usuario, dificuldade):
    if dificuldade == "Fácil":
        perguntas = [
            ("O que é um vírus de computador?", "programa malicioso"),
            ("Para que serve uma senha forte?", "proteger contas"),
            ("O que é phishing?", "golpe por e-mail ou mensagem"),
            ("O que significa HTTPS?", "protocolo seguro para web"),
            ("O que é firewall?", "proteção para a rede")
        ]
    elif dificuldade == "Médio":
        perguntas = [
            ("O que é autenticação multifator?", "mais de uma forma de verificação"),
            ("Explique o que é ransomware.", "sequestro de dados para pedir resgate"),
            ("Para que serve a criptografia?", "proteger dados"),
            ("O que é engenharia social?", "manipulação para obter informações"),
            ("O que é um certificado digital?", "identificação segura na internet")
        ]
    elif dificuldade == "Difícil":
        perguntas = [
            ("O que é um ataque de força bruta?", "tentativa exaustiva de senhas"),
            ("Explique o conceito de 'zero trust'.", "não confiar em nada dentro ou fora da rede"),
            ("O que é um exploit?", "código que aproveita vulnerabilidades"),
            ("Para que serve o protocolo SSL/TLS?", "segurança na comunicação"),
            ("O que é um worm?", "vírus que se replica sozinho")
        ]
    executar_quiz(perguntas, "CiberSegurança", usuario, dificuldade)


def quiz_matematica(usuario, dificuldade):
    if dificuldade == "Fácil":
        perguntas = [
            ("Quanto é 2 + 2?", "4"),
            ("Quanto é 5 - 3?", "2"),
            ("Quanto é 3 + 1?", "4"),
            ("Quanto é 6 x 1?", "6"),
            ("Quanto é 9 ÷ 3?", "3")
        ]
    elif dificuldade == "Médio":
        perguntas = [
            ("Quanto é 7 + 5?", "12"),
            ("Quanto é 9 x 6?", "54"),
            ("Quanto é 81 dividido por 9?", "9"),
            ("Quanto é 15 - 7?", "8"),
            ("Quanto é 8 x 7?", "56")
        ]
    elif dificuldade == "Difícil":
        perguntas = [
            ("Quanto é a raiz quadrada de 144?", "12"),
            ("Qual o resultado de (3^3) + 1?", "28"),
            ("Quanto é 100 dividido por 2 vezes 3?", "150"),
            ("Qual o valor de 2 elevado a 5?", "32"),
            ("Quanto é 45% de 200?", "90")
        ]
    executar_quiz(perguntas, "Matemática", usuario, dificuldade)


def escolher_dificuldade(materia, usuario):
    limpar_terminal()
    print(f"\n📈 Escolha a dificuldade de {materia}:")
    print("1. Fácil")
    print("2. Médio")
    print("3. Difícil")
    print("4. Voltar")

    escolha = input("Digite o número da dificuldade: ")
    limpar_terminal()

    if escolha == '1':
        dificuldade = "Fácil"
    elif escolha == '2':
        dificuldade = "Médio"
    elif escolha == '3':
        dificuldade = "Difícil"
    elif escolha == '4':
        return
    else:
        print("Opção inválida.")
        input("\nPressione Enter para continuar...")
        limpar_terminal()
        return

    if materia == "Pensamento Lógico em Python":
        quiz_pensamento_logico(usuario, dificuldade)
    elif materia == "Redes de Computadores":
        quiz_redes_computadores(usuario, dificuldade)
    elif materia == "CiberSegurança":
        quiz_ciberseguranca(usuario, dificuldade)
    elif materia == "Matemática":
        quiz_matematica(usuario, dificuldade)
    else:
        print("Matéria não encontrada.")
        input("\nPressione Enter para continuar...")

import time  # se ainda não estiver no topo

def executar_quiz(perguntas, materia, usuario, dificuldade):
    limpar_terminal()
    print(f"\n📘 Quiz de {materia} - {dificuldade}")
    acertos = 0

    for i, (pergunta, resposta_certa) in enumerate(perguntas, 1):
        resposta = input(f"{i}. {pergunta} ").strip().lower()
        print("⏳ Verificando resposta...")
        time.sleep(1.5)

        if resposta == resposta_certa.lower():
            print("✅ Correto!")
            acertos += 1
        else:
            print(f"❌ Errado. A resposta certa era: {resposta_certa}")
        time.sleep(1)

    print("\n📊 Calculando resultado...")
    time.sleep(2)
    print(f"\n🎉 Você acertou {acertos} de {len(perguntas)} perguntas em {materia} - {dificuldade}!")

    input("\nPressione Enter para continuar...")
    limpar_terminal()

    registrar_resultado(usuario, f"{materia} - {dificuldade}", acertos)

# Função para carregar dados dos quizzes
def carregar_resultados_quiz():
    if os.path.exists(ARQUIVO_QUIZ):
        with open(ARQUIVO_QUIZ, 'r') as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return {}
    return {}

# Função para salvar dados dos quizzes
def salvar_resultados_quiz(resultados):
    with open(ARQUIVO_QUIZ, 'w') as f:
        json.dump(resultados, f, indent=4)

# Função para registrar um resultado no arquivo
def registrar_resultado(usuario, materia, pontuacao):
    resultados = carregar_resultados_quiz()
    if usuario not in resultados:
        resultados[usuario] = {}
    if materia not in resultados[usuario]:
        resultados[usuario][materia] = []
    resultados[usuario][materia].append(pontuacao)
    salvar_resultados_quiz(resultados)


# Iniciar o programa
menu()