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