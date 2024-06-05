from PIL import Image
import numpy as np

def carregar_imagem(caminho):
    imagem = Image.open(caminho)
    return np.array(imagem)

def girar_90_graus(imagem):
    return np.rot90(imagem, -1)

def inverter_horizontal(imagem):
    return np.fliplr(imagem)

def inverter_vertical(imagem):
    return np.flipud(imagem)

def salvar_imagem(imagem, caminho):
    imagem_pil = Image.fromarray(imagem)
    imagem_pil.save(caminho)

if __name__ == "__main__":
    caminho_imagem = './image.png'  
    imagem = carregar_imagem(caminho_imagem)
    
    imagem_girada = girar_90_graus(imagem)
    salvar_imagem(imagem_girada, 'imagem_girada_90_graus.png')

    imagem_invertida_h = inverter_horizontal(imagem)
    salvar_imagem(imagem_invertida_h, 'imagem_invertida_horizontal.png')

    imagem_invertida_v = inverter_vertical(imagem)
    salvar_imagem(imagem_invertida_v, 'imagem_invertida_vertical.png')
