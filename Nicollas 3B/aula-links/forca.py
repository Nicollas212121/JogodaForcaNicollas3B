import random
import os

# 1. Dicionário de palavras separadas por temas
TEMAS = {
    "Tecnologia": ["python", "algoritmo", "software", "hardware", "nuvem", "binario"],
    "Jogos": ["minecraft", "fortnite", "roblox", "console", "aventura", "estrategia"],
    "Escola": ["professor", "biblioteca", "estudar", "caderno", "geografia", "caneta"],
    "Filmes": ["avatar", "coringa", "vingadores", "interestelar", "matrix", "shrek"]
}

def limpar_tela():
    """Limpa o terminal dependendo do sistema operacional."""
    os.system('cls' if os.name == 'nt' else 'clear')

def escolher_palavra():
    """Escolhe um tema e uma palavra aleatória dentro dele."""
    tema = random.choice(list(TEMAS.keys()))
    palavra = random.choice(TEMAS[tema])
    return tema, palavra

def mostrar_palavra(palavra, letras_acertadas):
    """Mostra a palavra ocultando as letras não descobertas."""
    return " ".join([letra if letra in letras_acertadas else "_" for letra in palavra])

def jogar():
    tema, palavra_secreta = escolher_palavra()
    letras_acertadas = set()
    letras_tentadas = set()
    vidas = 6
    pontos = 0

    while vidas > 0:
        limpar_tela()
        print("=" * 45)
        print(f"       JOGO DA FORCA - TEMA: {tema.upper()}")
        print("=" * 45)
        
        exibicao = mostrar_palavra(palavra_secreta, letras_acertadas)
        print(f"\nPalavra: {exibicao}")
        print(f"Tentativas: {', '.join(sorted(letras_tentadas))}")
        print(f"Vidas: {'❤️ ' * vidas} ({vidas})")
        print(f"Pontos: {pontos}")
        print("-" * 45)

        # Verifica se o jogador venceu (se não houver mais '_' na exibição)
        if "_" not in exibicao:
            print(f"\n🏆 PARABÉNS! VOCÊ VENCEU!")
            print(f"A palavra era: {palavra_secreta.upper()}")
            print(f"Pontuação final: {pontos + (vidas * 20)}") # Bônus por vidas restantes
            break

        letra = input("Digite uma letra: ").lower().strip()

        # Validações
        if len(letra) != 1 or not letra.isalpha():
            input("Aviso: Digite apenas uma única letra! [Enter]")
            continue

        if letra in letras_tentadas:
            input(f"Aviso: Você já tentou a letra '{letra}'. [Enter]")
            continue

        letras_tentadas.add(letra)

        if letra in palavra_secreta:
            letras_acertadas.add(letra)
            pontos += 10
        else:
            vidas -= 1
            pontos = max(0, pontos - 5) # Evita pontos negativos
            print(f"❌ Errou! A letra '{letra}' não existe.")

    if vidas == 0:
        limpar_tela()
        print("=" * 45)
        print("💀 FIM DE JOGO!")
        print(f"A palavra era: {palavra_secreta.upper()}")
        print(f"Pontuação final: {pontos}")
        print("=" * 45)

if __name__ == "__main__":
    jogar()