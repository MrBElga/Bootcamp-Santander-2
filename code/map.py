port_services = {
    21: "FTP",        # Serviço de transferência de arquivos
    22: "SSH",        # Secure Shell (acesso remoto seguro)
    23: "Telnet",     # Protocolo de acesso remoto inseguro
    25: "SMTP",       # Serviço de envio de emails
    53: "DNS",        # Serviço de tradução de nomes de domínio
    80: "HTTP",       # Serviço de transferência de hipertexto (web)
    110: "POP3",      # Serviço de recebimento de emails
    143: "IMAP",      # Serviço de recebimento de emails com suporte a pastas
    443: "HTTPS",     # Protocolo seguro de transferência de hipertexto
    3306: "MySQL",    # Banco de dados MySQL
    3389: "RDP",      # Remote Desktop Protocol (Acesso remoto ao Windows)
    5432: "PostgreSQL",  # Banco de dados PostgreSQL
    6379: "Redis"     # Banco de dados Redis
}

def enumerate_services(ports):
    services = []
    for port in ports:

        if port in port_services:
            services.append(port_services[port])
        else:
            services.append("Desconhecido")

    return services

def main():
    ports_input = input()  
    ports = list(map(int, ports_input.strip().split(',')))
    print(enumerate_services(ports))
if __name__ == "__main__":
    main()
