import unicodedata

def remover_acentos(texto):
    texto_normalizado = unicodedata.normalize('NFD', texto)
    texto_sem_acentos = ''.join(
        char for char in texto_normalizado
        if unicodedata.category(char) != 'Mn'
    )
    return texto_sem_acentos

if __name__ == "__main__":
    entrada = input("Digite um texto com acentos: ")
    resultado = remover_acentos(entrada)
    print("Texto sem acentos:", resultado)