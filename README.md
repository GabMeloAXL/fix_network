Fix Network Padrão (Windows)

Script simples em Python para automatizar três ações comuns de troubleshooting de rede no Windows:

Limpeza do cache DNS (ipconfig /flushdns)

Purga dos tickets Kerberos (klist purge)

Renovação do endereço IP (ipconfig /renew)

Ideal para chamados de suporte, máquinas em domínio ou rotinas rápidas de correção.

Uso
python fix_network.py

Requisitos

Windows

Python 3.x

Permissão administrativa (necessário para alguns comandos)

Código
import os

def fix_network_padrao():
    quebra_linha = "\n" * 3
    print(quebra_linha)
    os.system('ipconfig /flushdns')
    print(quebra_linha)
    os.system('klist purge')
    print(quebra_linha)
    os.system('ipconfig /renew')
    print(quebra_linha)

fix_network_padrao()

Notas

Útil como ferramenta rápida para suporte N1/N2.

Pode ser expandido com logs, menu interativo ou validação do sistema operacional.
