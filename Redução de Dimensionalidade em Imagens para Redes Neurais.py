# Função para carregar uma imagem PPM simples
def carregar_imagem(caminho):
    with open(caminho, 'rb') as arquivo:
        header = arquivo.readline().strip()  # Tipo PPM (P6)
        dimensoes = arquivo.readline().strip()  # Dimensões
        largura, altura = map(int, dimensoes.split())
        max_valor = int(arquivo.readline().strip())  # Valor máximo
        
        # Lê os pixels binários
        pixels = list(arquivo.read())
        
        return header, largura, altura, max_valor, pixels

# Função para converter a imagem para escala de cinza
def converter_para_cinza(largura, altura, pixels):
    escala_cinza = []
    for i in range(0, len(pixels), 3):
        r, g, b = pixels[i], pixels[i+1], pixels[i+2]
        # Fórmula de luminância perceptiva
        cinza = int(0.3 * r + 0.59 * g + 0.11 * b)
        escala_cinza.append(cinza)
    return escala_cinza

# Função para binarizar a imagem
def binarizar_imagem(escala_cinza, limiar=128):
    binarizada = []
    for valor in escala_cinza:
        binarizada.append(255 if valor >= limiar else 0)
    return binarizada

# Função para salvar a imagem como PGM (grayscale)
def salvar_imagem_pgm(caminho, largura, altura, max_valor, pixels):
    with open(caminho, 'w') as arquivo:
        arquivo.write("P2\n")
        arquivo.write(f"{largura} {altura}\n")
        arquivo.write(f"{max_valor}\n")
        for i in range(0, len(pixels), largura):
            linha = ' '.join(map(str, pixels[i:i+largura]))
            arquivo.write(linha + '\n')

# Caminho da imagem de entrada e saída
# Subtitua pelo caminho da sua imagem
caminho_entrada = "imagem.ppm"
caminho_saida_cinza = "imagem_cinza.ppm"
caminho_saida_binaria = "imagem_binaria.ppm"

# Executa as transformações
header, largura, altura, max_valor, pixels = carregar_imagem(caminho_entrada)
imagem_cinza = converter_para_cinza(largura, altura, pixels)
imagem_binaria = binarizar_imagem(imagem_cinza)

# Salva as imagens processadas
salvar_imagem_pgm(caminho_saida_cinza, largura, altura, max_valor, imagem_cinza)
salvar_imagem_pgm(caminho_saida_binario, largura, altura, max_valor, imagem_binaria)

print("Transformações realizadas com sucesso!")

