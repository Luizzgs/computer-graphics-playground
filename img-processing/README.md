## Implementação

### 1. [Processamento de Cores](cores/script.py)
Utilizei a biblioteca numpy para realizar o processamento e conversão de cores.
    * ```r, g, b = rgb[:,:,0], rgb[:,:,1], rgb[:,:,2]``` separa as cores em três canais
    * ```np.stack([r, g, b], axis=2)``` junta os canais de cores.
    * ```r, g, b = rgb[:,:,0], rgb[:,:,1], rgb[:,:,2] gray = 0.2989 * r + 0.5870 * g + 0.1140 * b``` Faz a conversão para tons de cinza, utilando a formula padrão.
    

### 2. [Filtros](filtros/script.py)


### 3. [Transformação](transformacao/script.py)


