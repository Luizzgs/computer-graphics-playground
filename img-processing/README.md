# Processamento básico de imagens
Este documento descreve a implementação de filtros e transformações de imagem utilizando Python, sem o uso da biblioteca OpenCV. As bibliotecas utilizadas são Pillow e NumPy para manipulação de imagens.

## Execução
Para rodar o script, somente ir na pasta de cada script e executar 
`python script.py`



## Funções Implementadas
### Separar Canais RGB

```python
def separar_canais(rgb):
    r, g, b = rgb[:,:,0], rgb[:,:,1], rgb[:,:,2]
    return r, g, b
```

Esta função separa os canais R, G e B de uma imagem RGB, retornando três arrays separados.

### Juntar Canais RGB

```python
def juntar_canais(r, g, b):
    return np.stack([r, g, b], axis=2)
```
Esta função junta três arrays de canais R, G e B em uma única imagem RGB.

### Conversão de RGB para Tons de Cinza

```python
def tons_de_cinza(rgb):
    r, g, b = rgb[:,:,0], rgb[:,:,1], rgb[:,:,2]
    gray = 0.2989 * r + 0.5870 * g + 0.1140 * b
    return gray
```
A função converte uma imagem RGB para tons de cinza utilizando a fórmula de luminância perceptual.

### Conversão de Tons de Cinza para Preto e Branco

```python
def cinza_para_pb(imagem_cinza, limiar=128):
    pb = (imagem_cinza > limiar) * 255
    return pb
```
Esta função converte uma imagem em tons de cinza para preto e branco utilizando um valor de limiar. Pixels acima do limiar são convertidos para branco e abaixo para preto.

### Filtro da Média

```python
def filtro_media(imagem, ksize=3):
    pad_size = ksize // 2
    imagem_padded = np.pad(imagem, pad_size, mode='constant', constant_values=0)
    output = np.zeros_like(imagem)
    
    kernel = np.ones((ksize, ksize)) / (ksize * ksize)
    
    for i in range(imagem.shape[0]):
        for j in range(imagem.shape[1]):
            output[i, j] = np.sum(imagem_padded[i:i+ksize, j:j+ksize] * kernel)
    
    return output
```

Aplica um filtro da média para suavização da imagem. Utiliza um kernel de tamanho especificado (ksize) para calcular a média dos pixels na vizinhança.

### Filtro da Mediana

```python
def filtro_mediana(imagem, ksize=3):
    pad_size = ksize // 2
    imagem_padded = np.pad(imagem, pad_size, mode='constant', constant_values=0)
    output = np.zeros_like(imagem)
    
    for i in range(imagem.shape[0]):
        for j in range(imagem.shape[1]):
            output[i, j] = np.median(imagem_padded[i:i+ksize, j:j+ksize])
    
    return output
```

Aplica um filtro da mediana para redução de ruído na imagem. Utiliza um kernel de tamanho especificado (ksize) para calcular a mediana dos pixels na vizinhança.

### Girar Imagem 90 Graus

```python
def girar_90_graus(imagem):
    return np.rot90(imagem, -1)
```
Gira a imagem 90 graus no sentido horário.

### Inverter Imagem Horizontalmente

```python
def inverter_horizontal(imagem):
    return np.fliplr(imagem)
```
Inverte a imagem horizontalmente (espelhamento horizontal).

### Inverter Imagem Verticalmente

```python
def inverter_vertical(imagem):
    return np.flipud(imagem)
```
Inverte a imagem verticalmente (espelhamento vertical).
