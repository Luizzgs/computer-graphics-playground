import cv2
import numpy as np
from PIL import Image

def carregar_imagem(caminho):
    imagem = Image.open(caminho)
    return np.array(imagem)

def salvar_imagem(imagem, caminho):
    imagem_pil = Image.fromarray(np.uint8(imagem))
    imagem_pil.save(caminho)

def separar_canais(rgb):
    r, g, b = rgb[:,:,0], rgb[:,:,1], rgb[:,:,2]
    return r, g, b

def juntar_canais(r, g, b):
    return np.stack([r, g, b], axis=2)

def tons_de_cinza(rgb):
    r, g, b = rgb[:,:,0], rgb[:,:,1], rgb[:,:,2]
    gray = 0.2989 * r + 0.5870 * g + 0.1140 * b
    return gray

def cinza_para_pb(imagem_cinza, limiar=128):
    pb = (imagem_cinza > limiar) * 255
    return pb

if __name__ == '__main__':
    caminho_imagem = './image.png'  # Substitua pelo caminho da sua imagem
    imagem = carregar_imagem(caminho_imagem)
    imagem_vermelho, imagem_verde, imagem_azul = separar_canais(imagem)
    imagem_completa = juntar_canais(imagem_vermelho, imagem_verde, imagem_azul)
    imagem_cinza = tons_de_cinza(imagem)
    imagem_preto_branco = cinza_para_pb(imagem_cinza)
    
    salvar_imagem(imagem_vermelho, 'imagem_vermelho.jpg')
    salvar_imagem(imagem_verde, 'imagem_verde.jpg')
    salvar_imagem(imagem_azul, 'imagem_azul.jpg')
    salvar_imagem(imagem_completa, 'imagem_completa.jpg')
    salvar_imagem(imagem_cinza, 'imagem_cinza.jpg')
    salvar_imagem(imagem_preto_branco, 'imagem_preto_branco.jpg')

