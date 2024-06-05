## Implementação

### 1. [Processamento de Cores](cores/script.py)
Utilizei a biblioteca numpy para realizar o processamento e conversão de cores.
    * `r, g, b = rgb[:,:,0], rgb[:,:,1], rgb[:,:,2]` separa as cores em três canais
    * `np.stack([r, g, b], axis=2)` junta os canais de cores.
    * `r, g, b = rgb[:,:,0], rgb[:,:,1], rgb[:,:,2] gray = 0.2989 * r + 0.5870 * g + 0.1140 * b` Faz a conversão para tons de cinza, utilando a formula padrão.
    

### 2. [Filtros](filtros/script.py)
Foi utilizada a imagem `cria.png` para realizar a conversão de espaço de cores. A imagem foi convertida para os espaços de cores `Cinza` através da função `cv2.cvtColor()` e para `Binário` através da função `cv2.threshold()`. Além disso, foi feita manualmente a limiarização para `Binário`, transformando os pixels com valor maior que 127 para 255 (branco) e com valor menor para 0 (preto).

### 3. [Transformação](transformacao/script.py)
Foi utilizada a imagem `tigre.png` para a aplicação de filtros. Foram aplicados os filtros `Média` e `Mediana` através da passagem de um elemento estruturante de 3x3 pela imagem.

