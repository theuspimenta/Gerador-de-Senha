import random
import string

def gerar_senha(comprimento, incluir_especiais=True):
    caracteres = string.ascii_letters + string.digits
    if incluir_especiais:
        caracteres += string.punctuation

    senha = ''.join(random.choice(caracteres) for _ in range(comprimento))
    return senha

# Exemplo de uso
comprimento_senha = 12
incluir_especiais = False  # Altere para False se não quiser caracteres especiais
senha_gerada = gerar_senha(comprimento_senha, incluir_especiais)
print("Senha Gerada:", senha_gerada)
