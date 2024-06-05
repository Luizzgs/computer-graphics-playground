from PIL import Image
import numpy as np

def carregar_imagem(caminho):
    imagem = Image.open(caminho).convert("L")  # Converte para tons de cinza
    return np.array(imagem)

def filtro_media(imagem, ksize=3):
    pad_size = ksize // 2
    imagem_padded = np.pad(imagem, pad_size, mode='constant', constant_values=0)
    output = np.zeros_like(imagem)
    
    kernel = np.ones((ksize, ksize)) / (ksize * ksize)
    
    for i in range(imagem.shape[0]):
        for j in range(imagem.shape[1]):
            output[i, j] = np.sum(imagem_padded[i:i+ksize, j:j+ksize] * kernel)
    
    return output

def filtro_mediana(imagem, ksize=3):
    pad_size = ksize // 2
    imagem_padded = np.pad(imagem, pad_size, mode='constant', constant_values=0)
    output = np.zeros_like(imagem)
    
    for i in range(imagem.shape[0]):
        for j in range(imagem.shape[1]):
            output[i, j] = np.median(imagem_padded[i:i+ksize, j:j+ksize])
    
    return output


def salvar_imagem(imagem, caminho):
    imagem_pil = Image.fromarray(np.uint8(imagem))
    imagem_pil.save(caminho)

if __name__ == "__main__":
    caminho_imagem = './image.png'  
    imagem_cinza = carregar_imagem(caminho_imagem)
    
    imagem_media = filtro_media(imagem_cinza, ksize=5) 
    salvar_imagem(imagem_media, 'imagem_media.jpg')

    imagem_mediana = filtro_mediana(imagem_cinza, ksize=5)
    salvar_imagem(imagem_mediana, 'imagem_mediana.jpg')
