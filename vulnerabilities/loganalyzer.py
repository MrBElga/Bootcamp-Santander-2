# Função para detectar tentativas de invasão em registros de log
def detectar_invasao(registros):
    usuario_atual = None
    tentativas_consecutivas = 0
    invasor_detectado = None

    for registro in registros:

        id_usuario, status = registro.split(":")
        if id_usuario == usuario_atual:
            if status == "falha":
                tentativas_consecutivas += 1
                # Verifica se excedeu 3 falhas consecutivas
                if tentativas_consecutivas > 3:
                    invasor_detectado = id_usuario
                    break
            else:
                tentativas_consecutivas = 0  # Reseta se for sucesso
        else:
            # Se o usuário mudou, verifica se o anterior excedeu o limite
            if tentativas_consecutivas > 3:
                invasor_detectado = usuario_atual
                break
            # Atualiza para o novo usuário
            usuario_atual = id_usuario
            tentativas_consecutivas = 1 if status == "falha" else 0

    # Verifica o último usuário após o loop
    if tentativas_consecutivas > 3 and not invasor_detectado:
        invasor_detectado = usuario_atual

    return invasor_detectado if invasor_detectado else "Nenhum invasor detectado"

# Função principal para executar o programa
def main():
    entrada = input("Digite os registros de log separados por vírgula: ")
    registros = [registro.strip() for registro in entrada.split(",")]
    resultado = detectar_invasao(registros)
    print(resultado)

if __name__ == "__main__":
    main()
