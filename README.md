# Conversão de Imagem Colorida para Tons de Cinza e Binária
Este projeto implementa um algoritmo simples em Python para processar imagens no formato PPM (P3). Ele realiza a conversão de uma imagem colorida para:

1. Níveis de cinza (valores entre 0 e 255).
2. Imagem binária (apenas valores 0 e 255), representando preto e branco.
   
Tudo isso é feito sem o uso de bibliotecas externas de manipulação de imagens, demonstrando os fundamentos de processamento de imagens.

# Funcionalidades
* Conversão para Tons de Cinza: Baseada na fórmula de luminância para calcular a intensidade de brilho.
* Conversão para Binária: A partir de um limiar, define quais pixels serão pretos (0) ou brancos (255).
* Compatível com o Formato PPM (P3): Trabalha com imagens de texto padrão para simplificar a manipulação.

# Estrutura do Projeto
_carregar_imagem(caminho):_ Carrega uma imagem no formato PPM (P3), ignorando comentários e extraindo os dados dos pixels.
_salvar_imagem(caminho, largura, altura, max_valor, imagem):_ Salva uma imagem no formato PPM (P3).
_converter_para_cinza(imagem):_ Transforma os pixels coloridos da imagem em tons de cinza.
_converter_para_binaria(imagem, limiar=127):_ Converte uma imagem em tons de cinza para binária, utilizando um limiar ajustável (padrão: 127).

# Pré-requisitos
Python 3.6 ou superior.
Imagem de entrada no formato PPM (P6).

# Como Usar
Clone o repositório:

~~~~
git clone https://github.com/seu_usuario/Reducao-Dimensionalidade-em-Imagens-para-Redes-Neurais.git
cd Reducao-Dimensionalidade-em-Imagens-para-Redes-Neurais
~~~~
Coloque uma imagem no formato PPM (P6) na mesma pasta do código e nomeie-a como imagem.ppm.

Execute o código:
~~~~
python main.py
~~~~
Verifique os resultados:

 <div style="display: flex; justify-content: center; gap: 10px;">
        <img src="https://github.com/Luizgustavo0109/Reducao-Dimensionalidade-em-Imagens-para-Redes-Neurais/blob/main/table.jpg" alt="Imagem Original" style="width: 30%;">
        <img src="https://github.com/Luizgustavo0109/Reducao-Dimensionalidade-em-Imagens-para-Redes-Neurais/blob/main/imagem_cinza.png" alt="Imagem em Tons de Cinza" style="width: 30%;">
        <img src="https://github.com/Luizgustavo0109/Reducao-Dimensionalidade-em-Imagens-para-Redes-Neurais/blob/main/imagem_binaria.png" alt="Imagem Binária" style="width: 30%;">
    </div>


> A imagem convertida para tons de cinza será salva como imagem_cinza.ppm.
> A imagem binarizada será salva como imagem_binaria.ppm.

# Observações
> O formato PPM (P6) é um formato simples, ideal para aprendizado, mas menos eficiente para aplicações práticas. Você pode usar ferramentas como GIMP ou ImageMagick para converter outras imagens para este formato.
> Certifique-se de que o arquivo de entrada siga o padrão do formato PPM (P6), incluindo a especificação do tipo, dimensões e valor máximo.

# Contribuições
Sinta-se à vontade para abrir issues ou enviar pull requests para melhorias e correções.

# Licença
Este projeto está licenciado sob a licença MIT. Consulte o arquivo LICENSE para mais informações.
