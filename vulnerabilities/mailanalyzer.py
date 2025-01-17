# Função para verificar se o corpo do e-mail contém palavras suspeitas de phishing
def verificar_phishing(mensagem):
    palavras_suspeitas = ["ganhe", "prêmio", "urgente", "desconto", "click", "promoção"]
    mensagem = mensagem.lower()
    for palavra in palavras_suspeitas:
        if palavra in mensagem:
            return "Phishing"
    return "Seguro"

email_usuario = input().strip()

resultado = verificar_phishing(email_usuario)

print(f"Classificação: {resultado}")
