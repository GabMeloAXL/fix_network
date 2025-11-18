# Fix Network Padrão

Script simples em Python para resolver problemas comuns de rede no Windows.  
Ele faz três ações clássicas de “reset básico” que geralmente resolvem 90% dos problemas de conexão:

- Limpa o cache DNS (`ipconfig /flushdns`)
- Remove tickets Kerberos (`klist purge`)
- Renova o IP da máquina (`ipconfig /renew`)

Ideal para uso rápido no dia a dia de suporte.

---

# Como funciona

O script executa automaticamente os comandos do Windows via `os.system()` e adiciona quebras de linha para deixar a saída mais limpa no terminal.

```python
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
