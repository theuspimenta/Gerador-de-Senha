import random
import string

def gerar_senha(comprimento):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    senha = ''.join(random.choice(caracteres) for i in range(comprimento))
    return senha

# Exemplo de uso
comprimento_senha = 12
senha_gerada = gerar_senha(comprimento_senha)
print("Senha Gerada:", senha_gerada)
